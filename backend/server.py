import datetime
import json
import time

import flask
import flask_login
from pyodbc import Row

import db
from werkzeug.security import check_password_hash, generate_password_hash
import uuid
import flask_cors

'''
---SUGGESTIONS---
1. Set cors header: app.config['CORS_HEADERS'] = 'Content-Type'
2. Add CORS(app, resources={r"/*": {"origins": "*"}})
3. To allow cookies to be sent cross-origin: CORS(app, supports_credentials=True)
4. https://stackoverflow.com/questions/71109384/cookies-not-being-sent-with-axios
5. Cors Options: https://stackoverflow.com/questions/52549079/does-axios-support-set-cookie-is-it-possible-to-authenticate-through-axios-http
---FRONTEND ----
- timer unit test failing --> could need to reset timer to 0 after doing acceptance tests
- acceptance test could  be failing because passwords hashed/new security
'''


class customJSON(flask.json.provider.JSONProvider):

    def dumps(self, obj, **kwargs):
        return json.dumps(obj, **kwargs, default=str)

    def loads(self, s: str or bytes, **kwargs):
        return json.loads(s, **kwargs)


app = flask.Flask(__name__)
app.json = customJSON(app)

app.config["SECRET_KEY"] = uuid.uuid4().hex  # reset secret key each time the server starts
app.config['SESSION_COOKIE_HTTPONLY'] = False

print(app.config)
# instantiate flask login manager
flask_login.config.COOKIE_HTTPONLY = False
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

flask_cors.CORS(app, supports_credentials=True)


# tell flask how to load a user from a flask request and from its session
class User(flask_login.UserMixin):
    pass


# loads user from session
@login_manager.user_loader
def user_loader(username):
    selection = db.getUser(username)
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
    session = request.headers['session']
    username = flask_login.login_manager.session.get(session)
    # check database for username
    selection = db.getUser(username)
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
    # grab the username from the header
    if flask.request.get_json(force=True) is not None:
        # username header exists
        username = flask.request.get_json(force=True)['username']
        password = flask.request.get_json(force=True)['password']
        # check db for username and password
        # selection is a list of rows (SHOULD BE LENGTH 1)
        selection = db.getUser(username)

        if selection is None:
            # username not in database
            # be ambiguous for security reasons
            response = "Bad Request: Invalid Username or Password", 401
            return response
        else:
            # selection returned
            # grab values for username and password from db
            uname = selection.username
            pword = selection.password

            if uname == username and pword == password:
                user = User()
                user.id = username
                flask_login.login_user(user)
                print(flask.session)

                resp = flask.make_response()
                resp.status_code = 200
                resp.data = 'Logged In'
                resp.headers.add_header('key', 'val')
                resp.headers.add_header('key2', 'val2')
                resp.access_control_allow_headers = ['key', 'key2', 'Set-Cookie']
                resp.headers.set('Access-Control-Expose-Headers', 'key, key2, Set-Cookie')
                resp.headers.set("Access-Control-Allow-Credentials", True)

                # redirect to homepage
                return resp
            else:
                # invalid password
                # send 401 bad request response
                # be ambiguous for security reasons
                response = "Bad Request: Invalid Username or Password", 401
                return response
    else:
        # send 400 bad request response
        response = "Bad Request: Missing required JSON", 400
        return response


# logout api request
@app.route("/api/logout", methods=["POST"])
@flask_login.login_required
def logout():
    # just delete the cookie from the users browser
    # and log out the user
    flask_login.logout_user()
    resp = flask.make_response()
    resp.delete_cookie('session')
    resp.data = "Logged Out"
    resp.status_code = 200
    return resp


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
    if res is not None:
        # print(username, " increased ", classname, "'s study time by: ", t, " seconds")
        return "Time for class updated successfully", 200
    else:
        return "Bad Request: No class found", 400


# returns the data for a single class of classname: 'classname'
@app.route("/api/class/<classname>", methods=["GET"])
@flask_login.login_required
def getClass(classname):
    username = flask_login.current_user.get_id()
    res = db.getSingleClass(username, classname)
    if res is None:
        # no class found
        return "Bad Request: No class found", 400
    else:
        return {"result": parse_row(res)}, 200


# converts a list of rows into a list of dictionaries
def parse_rows(rows):
    res = []
    if rows is not None:
        for row in rows:
            res.append(dict(zip([t[0] for t in row.cursor_description], row)))
    return res


# converts a row into a dictionary
def parse_row(row):
    return dict(zip([t[0] for t in row.cursor_description], row))


# returns a list of tasks associated with 'classname'
@app.route("/api/class/<classname>/task", methods=["GET"])
@flask_login.login_required
def all_tasks(classname):
    username = flask_login.current_user.get_id()
    res = db.getSingleClass(username, classname)
    if res is None:
        # no class found
        return "Bad Request: No class found", 400
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
    if res is not None and res.is_complete == 0:
        res = db.completeClass(username, classname)
        return "Class completed", 200
    elif res is None:
        return "Bad Request: Class not found", 404
    else:
        return "Bad Request: Class already completed", 400


# updates the metadata for class: 'classname', any missing metadata remains the same
@app.route("/api/class/<classname>/update_meta", methods=["POST"])
@flask_login.login_required
def classMeta(classname):
    username = flask_login.current_user.get_id()
    req = flask.request.get_json(force=True)
    res = db.getSingleClass(username, classname)

    if res is None:
        return "Bad Request: No class found", 400

    # since json attributes are optional, only update if they're given
    if 'breakdown' not in req.keys():
        breakdown = res.breakdown
    else:
        breakdown = req['breakdown']

    if 'sectionnum' not in req.keys():
        sectionnum = res.section
    else:
        sectionnum = req['sectionnum']

    if 'classroom' not in req.keys():
        classroom = res.classroom
    else:
        classroom = req['classroom']

    if 'prof' not in req.keys():
        prof = res.prof_Name
    else:
        prof = req['prof']

    if 'prof_email' not in req.keys():
        prof_email = res.prof_Email
    else:
        prof_email = req['prof_email']

    if 'prof_phone' not in req.keys():
        prof_phone = res.prof_Phone
    else:
        prof_phone = req['prof_phone']

    if 'prof_office' not in req.keys():
        prof_office = res.prof_Office
    else:
        prof_office = req['prof_office']

    if 'prof_hours' not in req.keys():
        prof_hours = res.prof_Hours
    else:
        prof_hours = req['prof_hours']

    # update metadata
    res = db.editClassMeta(username, classname, sectionnum, classroom, prof, prof_email, prof_phone, prof_office,
                           prof_hours)
    # update breakdown
    res = db.addClassBreakdown(username, classname, breakdown)
    return 'Class Meta updated successfully', 200


# creates a new task for the current user for the class: 'classname'
@app.route("/api/class/<classname>/newtask", methods=["POST"])
@flask_login.login_required
def newtask(classname):
    req = flask.request.get_json(force=True)
    username = flask_login.current_user.get_id()

    # since json attributes are optional, only update if they're given
    if 'weight' not in req.keys():
        # use undef weight
        weight = -1
    else:
        weight = req['weight']

    if 'deadline' not in req.keys():
        # use undef deadline
        deadline = None
    else:
        deadline = req['deadline']
    if 'task_goal' not in req.keys():
        # use default
        task_goal = 'A'
    else:
        task_goal = req['task_goal']
    # add task to class
    res = db.addTask(username, classname, req['taskname'], weight, deadline, task_goal)
    if res is None:
        return "Bad Request: No class found", 400
    else:
        return "Successfully added task", 200


# creates new class associated with logged-in user
@app.route('/api/newclass', methods=["POST"])
@flask_login.login_required
def newclass():
    req = flask.request.get_json(force=True)
    username = flask_login.current_user.get_id()
    # classname and timeslot are required
    if 'classname' not in req.keys() or 'timeslot' not in req.keys() or 'courseCode' not in req.keys():
        return "Bad Request: JSON missing required value(s)", 400
    else:
        res = db.addClass(username, req['classname'], req['timeslot'], req['courseCode'])
        if res is None:
            return "Error", 400
        return "Added Class", 200


# returns a list of classes associated with logged-in user
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
    elif res is None:
        # no classes found
        return {"result": []}, 200


# get specific task: 'taskname'
@app.route('/api/class/<classname>/task/<taskname>', methods=["GET"])
@flask_login.login_required
def get_task(classname, taskname):
    username = flask_login.current_user.get_id()
    res = db.getTaskID(username, classname, taskname)
    if res is None:
        # no class found
        return "Bad Request: No task found", 400
    else:
        return {"result": parse_row(res)}, 200


# modify the name, weight, and/or deadline of a task
@app.route('/api/class/<classname>/task/<taskname>/edit', methods=["POST"])
@flask_login.login_required
def edit_task(classname, taskname):
    username = flask_login.current_user.get_id()
    req = flask.request.get_json(force=True)

    # attributes are optional, so keep the same if they're not given
    if 'newname' not in req.keys():
        newname = ""
    else:
        newname = req['newname']
    if 'newdeadline' not in req.keys():
        newdeadline = ""
    else:
        newdeadline = req['newdeadline']
    if 'newweight' not in req.keys():
        newweight = ""
    else:
        newweight = req['newweight']
    if 'eGoal' not in req.keys():
        eGoal = 'A'
    else:
        eGoal = req['eGoal']

    db.editTask(username, classname, taskname, newname, newdeadline, newweight, eGoal)
    return "Task edited", 200


# delete a task
@app.route('/api/class/<classname>/task/<taskname>/delete', methods=["POST"])
@flask_login.login_required
def delete_task(classname, taskname):
    username = flask_login.current_user.get_id()
    res = db.removeTask(username, classname, taskname)
    return "Task removed", 200


# edit a class's name, and/or timeslot
@app.route('/api/class/<classname>/edit', methods=["POST"])
@flask_login.login_required
def edit_class(classname):
    username = flask_login.current_user.get_id()
    req = flask.request.get_json(force=True)

    # attributes are optional, so keep the same if not given
    if 'newname' not in req.keys():
        newname = ""
    else:
        newname = req['newname']
    if 'newtime' not in req.keys():
        newtime = ""
    else:
        newtime = req['newtime']

    db.editClassReqData(username, classname, newname, newtime)
    return "Class edited", 200


# deletes a class
@app.route('/api/class/<classname>/delete', methods=["POST"])
@flask_login.login_required
def delete_class(classname):
    username = flask_login.current_user.get_id()
    res = db.removeClass(username, classname)
    return "Class removed", 200


# marks a task as complete by setting the grade value
@app.route('/api/class/<classname>/task/<taskname>/complete', methods=["POST"])
@flask_login.login_required
def complete_task(classname, taskname):
    username = flask_login.current_user.get_id()
    req = flask.request.get_json(force=True, silent=True)
    # if grade isn't given
    if req is None or 'grade' not in req.keys():
        grade = 0
    else:
        grade = req['grade']

    cls = db.getClassID(username, classname)
    task = db.getTaskID(username, classname, taskname)
    if cls is None or task is None:
        return "Bad Request: Class or task not found", 400
    res = db.completeTask(username, classname, taskname, grade)
    return "Completed Task Successfully", 200


# returns all the complete tasks for class: 'classname'
@app.route('/api/class/<classname>/done_tasks', methods=["GET"])
@flask_login.login_required
def get_done_tasks(classname):
    username = flask_login.current_user.get_id()
    res = db.getCompleteTasksForClass(username, classname)
    if type(res) is Row:
        print(parse_row(res))
        return {"result": parse_row(res)}, 200
    elif type(res) is list:
        print(parse_rows(res))
        return {"result": parse_rows(res)}, 200
    else:
        # no done tasks
        return {"result": []}, 200


# calculates a letter grade via the class's grade breakdown and the done tasks
# sends the letter grade and a message
@app.route('/api/class/<classname>/grade', methods=["GET"])
@flask_login.login_required
def grade(classname):
    messages = {"A+": "What the heck?! I am shocked, astounded, and flabbergasted right now!",
                "A": "Wow! You're doing amazing!",
                "B+": "Keep up the good work!",
                "B": "Hey, that's pretty good!",
                "C+": "You're doing OK!",
                "C": "Remember: 'C's get degrees!",
                "D": "You can do better than that, I believe in you!",
                "F": "Uh oh."}
    username = flask_login.current_user.get_id()
    # print(username)
    # get <classname> class, process grade breakdown
    res = db.getSingleClass(username, classname)
    # print(res)
    if res is not None and res.breakdown is not None:
        breakdown = json.loads(res.breakdown)
    else:
        return "Bad Request: Class not found, or class has no grade breakdown", 400
    # get <classname> completed tasks, process their grades
    comp_tasks = db.getCompleteTasksForClass(username, classname)
    # print(comp_tasks)
    if comp_tasks is None:
        return {"result": "-", "message": "You haven't got any grades yet."}, 200
    total_weight = 0
    total_grade = 0
    for t in comp_tasks:
        # task is gradable
        if t.task_Weight != -1:
            # print('----', t.task_Weight)
            total_weight = total_weight + t.task_Weight
            total_grade = total_grade + t.task_grade * t.task_Weight
    if total_weight > 100:
        print(username, classname, "has a total task weight > 100%!")
        return "Server Error", 500
    if total_weight == 0:
        # realistically, should never occur, b/c 'comp_tasks is None' check, but I've been wrong before so...
        return {"result": "-", "message": "You haven't got any grades yet."}, 200
    class_grade = total_grade / total_weight
    # return letter grade based on breakdown and done task grades
    # print(classname, "has a grade of: ", class_grade)
    for k in breakdown.keys():
        # print(eval(breakdown[k])[0] / 100, " < ", str(class_grade), " <= ", eval(breakdown[k])[1] / 100)
        if eval(breakdown[k])[0] < class_grade <= eval(breakdown[k])[1]:
            return {"result": k, "message": messages[k]}, 200
    print(username, "didn't find grade range for", classname)
    return "Server Error: Grade range wasn't found", 500


# for debugging
@app.before_request
def log_request():
    # print(flask.request.headers)
    # print(flask.request.get_json(force=True))
    return None
