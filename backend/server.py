import flask
import flask_login
from pyodbc import Row

import db
from werkzeug.security import check_password_hash, generate_password_hash
import uuid
import flask_cors

app = flask.Flask(__name__)
app.secret_key = uuid.uuid4().hex  # reset secret key each time the server starts

# instantiate flask login manager
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

flask_cors.CORS(app)

# mock persistence layer
users = {"testuser": {"username": "testuser", "password": "123"}}


# for debug
def setTest(boo):
    app.config["TESTING"] = boo


# tell flask how to load a user from a flask request and from its session
class User(flask_login.UserMixin):
    pass


def user_check(username):
    if app.testing:
        selection = users[username]
    else:
        selection = db.getUser(username)
    return selection


# loads user from session
@login_manager.user_loader
def user_loader(username):
    print("u loader")
    selection = db.getUser(username)
    if app.testing:
        uname = selection['username']
    else:
        uname = selection.username
    if uname == username:
        user = User()
        user.id = username
        return user
    else:
        return None


# loads user from flask request
@login_manager.request_loader
def request_loader(request):
    print("req loader")
    username = request.get_json(force=True)['username']
    # check database for username
    selection = db.getUser(username)
    if app.testing:
        uname = selection['username']
    else:
        uname = selection.username
    if uname == username:
        user = User()
        user.id = username
        return user
    else:
        return None


# deal with unauthorized access attempts
@login_manager.unauthorized_handler
def unauthorized_handler():
    return "Unauthorized", 401


# login api request
@app.route("/api/login", methods=["POST"])
def login():
    # print("attempting login")
    # grab the username from the header
    # print(flask.request.get_json())
    if flask.request.get_json(force=True) is not None:
        # username header exists
        username = flask.request.get_json(force=True)['username']
        password = flask.request.get_json(force=True)['password']
        # print(username)
        # print(password)
        # check db for username and password
        # selection is a list of rows (SHOULD BE LENGTH 1)
        selection = db.getUser(username)

        if selection is None:
            # not in database
            response = "Bad Request: User not found in database", 400
            print("no user")
            return response
        else:
            # selection returned
            # grab values for username and password from db
            print("yes user")
            if app.testing:
                uname = selection['username']
                pword = selection['password']
            else:
                uname = selection.username
                pword = selection.password

            if uname == username and pword == password:
                user = User()
                user.id = username
                flask_login.login_user(user)
                print("logged in: ", username)
                # redirect to homepage
                # flask.redirect("../../frontend/index.html", 200)
                return "Logged In", 200
            else:
                # invalid password
                # send 401 bad request response
                print("failed login: ", username)
                print("Incorrect password")
                response = "Incorrect Password", 401
                return response
    else:
        # send 400 bad request response
        print("login missing json")
        response = "Bad Request: Missing required JSON", 400
        return response


# logout api request
@app.route("/api/logout", methods=["POST"])
@flask_login.login_required
def logout():
    flask_login.logout_user()
    return "Logged Out", 200


# create a new user
@app.route("/api/newuser", methods=["POST"])
def newuser():
    username = flask.request.get_json(force=True)['username']
    password = flask.request.get_json(force=True)['password']
    # check database for already existing user with the same name
    selection = db.getUser(username)
    if selection is None:
        # if there are no existing users with that username in the db...
        # create a new account with the username and password
        db.createAccount(username, password)
        user = User()
        user.id = username
        flask_login.login_user(user)
        return "Account created", 200
    else:
        return "Account already exists with username", 400


# increases the study_time attribute for 'classname' by 'added' seconds
@app.route("/api/class/<classname>/update_time", methods=["POST"])
@flask_login.login_required
def update_time(classname):
    # updates the time studied for a class
    username = flask_login.current_user.get_id()
    t = flask.request.get_json(force=True)['added']
    res = db.addStudyTime(username, classname, t)
    print(username, " increased ", classname, "'s study time by: ", t, " seconds")
    return "Time for class updated successfully", 200


# returns the data for a single class of classname: 'classname'
@app.route("/api/class/<classname>", methods=["GET"])
@flask_login.login_required
def getClass(classname):
    username = flask_login.current_user.get_id()
    res = db.getSingleClass(username, classname)
    if res is None:
        # no class found
        return {"result": "Bad Request: No class found"}, 400
    else:
        return {"result": parse_row(res)}, 200


def parse_rows(rows):
    res = []
    for row in rows:
        res.append(dict(zip([t[0] for t in row.cursor_description], row)))
    return res


def parse_row(row):
    return dict(zip([t[0] for t in row.cursor_description], row))


# returns a list of tasks assocaited with 'classname'
@app.route("/api/class/<classname>/task", methods=["GET"])
@flask_login.login_required
def all_tasks(classname):
    username = flask_login.current_user.get_id()
    res = db.getSingleClass(username, classname)
    if res is None:
        # no class found
        return {"result": "Bad Request: No class found"}, 400
    else:
        res = db.getTaskList(username, classname)
        # need to parse
        return {"result": parse_rows(res)}, 200


# sets the is_complete attribute of 'classname' to true
@app.route("/api/class/<classname>/complete", methods=["POST"])
@flask_login.login_required
def completeClass(classname):
    username = flask_login.current_user.get_id()
    res = db.getSingleClass(username, classname)
    if res is not None and res.is_Complete == 0:
        res = db.completeClass(username, classname)
        return "Class completed", 200
    elif res is None:
        return "Class not found", 404
    else:
        return "Bad Request: Class not found, or class already completed", 400


# updates the metadata for class: 'classname', any missing metadata remains the same
@app.route("/api/class/<classname>/update_meta", methods=["POST"])
@flask_login.login_required
def classMeta(classname):
    username = flask_login.current_user.get_id()
    req = flask.request.get_json(force=True)
    res = db.getSingleClass(username, classname)

    if 'sectionnum' not in req.keys():
        sectionnum = res.sectionnum
    else:
        sectionnum = req['sectionnum']

    if 'classroom' not in req.keys():
        classroom = res.classroom
    else:
        classroom = req['classroom']

    if 'prof' not in req.keys():
        prof = res.prof
    else:
        prof = req['prof']

    if 'prof_email' not in req.keys():
        prof_email = res.prof_email
    else:
        prof_email = req['prof_email']

    if 'prof_phone' not in req.keys():
        prof_phone = res.prof_phone
    else:
        prof_phone = req['prof_phone']

    if 'prof_office' not in req.keys():
        prof_office = res.prof_office
    else:
        prof_office = req['prof_office']

    if 'prof_hours' not in req.keys():
        prof_hours = str(res.prof_hours)
    else:
        prof_hours = req['prof_hours']

    res = db.editClassMeta(username, classname, sectionnum, classroom, prof, prof_email, prof_phone, prof_office,
                           prof_hours)
    if res is not None:
        return 'Class Meta updated successfully', 200
    else:
        return 'Bad Request: Failed to find class', 400


# creates a new task for the current user for the class: 'classname'
@app.route("/api/class/<classname>/newtask", methods=["POST"])
@flask_login.login_required
def newtask(classname):
    req = flask.request.get_json(force=True)
    username = flask_login.current_user.get_id()

    if 'weight' not in req.keys():
        # use undef weight
        weight = -1
    else:
        weight = req['weight']

    res = db.addTask(username, classname, req['taskname'], weight, req['deadline'])
    if res is None:
        return "Bad Request: Class given doesn't exist", 400
    else:
        return "Successfully added task", 200


@app.route('/api/newclass', methods=["POST"])
@flask_login.login_required
def newclass():
    req = flask.request.get_json(force=True)
    username = flask_login.current_user.get_id()
    if 'classname' not in req.keys() or 'timeslot' not in req.keys():
        return "Bad Request: JSON missing required value(s)", 400
    else:
        res = db.addClass(username, req['classname'], req['timeslot'])
        return "Added Class", 200


# returns a list of classes associated with logged in user
@app.route("/api/class", methods=["GET"])
@flask_login.login_required
def all_classes():
    username = flask_login.current_user.get_id()
    res = db.getClasses(username)
    # converts Row/Rows objects into jsonify parsable dictionaries
    if type(res) is list:
        return {"result": parse_rows(res)}, 200
    elif type(res) is Row:
        return {"result": parse_row(res)}, 200


# get specific task: 'taskname'
@app.route('/api/class/<classsname>/task/<taskname>', methods=["GET"])
@flask_login.login_required
def get_task(classname, taskname):
    username = flask_login.current_user.get_id()
    res = db.getTaskID(username, classname, taskname)
    if res is None:
        # no class found
        return {"result": "Bad Request: No task found"}, 400
    else:
        return {"result": parse_row(res)}, 200


@app.route('/api/class/<classsname>/task/<taskname>/complete', methods=["POST"])
@flask_login.login_required
def complete_task(classname, taskname):
    username = flask_login.current_user.get_id()
    req = flask.request.get_json(force=True)
    if 'grade' not in req.keys():
        return "Bad Request: Missing required JSON value(s)", 400
    else:
        res = db.completeTask(username, classname, taskname, req['grade'])
        if res is None:
            return "Bad Request", 400
        else:
            return "Completed Task Successfully", 200


# returns all the complete tasks for class: 'classname'
@app.route('/api/class/<classname>/done_tasks', methods=["GET"])
@flask_login.login_required
def get_done_tasks(classname):
    username = flask_login.current_user.get_id()
    res = db.getCompleteTasksForClass(username, classname)
    if type(res) is Row:
        return {"result": parse_row(res)}, 200
    else:
        return {"result": parse_rows(res)}, 200


# for debugging
@app.before_request
def log_request():
    # print(flask.request.headers)
    # print(flask.request.get_json(force=True))
    return None
