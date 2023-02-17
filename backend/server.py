import flask
import flask_login
import db
from werkzeug.security import check_password_hash, generate_password_hash
import uuid

app = flask.Flask(__name__)
app.secret_key = uuid.uuid4().hex  # reset secret key each time the server starts

# instantiate flask login manager
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# mock persistence layer
users = {"testuser": {"username": "testuser", "password": "123"}}


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
    selection = user_check(username)
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
    username = request.get_json()['username']
    # check database for username
    selection = user_check(username)
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


@app.route("/")
def hello_world():
    return "homepage", 200


# login api request
@app.route("/api/login", methods=["POST"])
def login():
    # print("attempting login")
    # grab the username from the header
    # print(flask.request.get_json())
    if flask.request.get_json() is not None:
        # username header exists
        username = flask.request.get_json()['username']
        password = flask.request.get_json()['password']
        # print(username)
        # print(password)
        # check db for username and password
        # selection is a list of rows (SHOULD BE LENGTH 1)
        selection = user_check(username)

        if selection is None:
            # not in database
            response = "Bad Request: User not found in database", 400
            return response
        else:
            # selection returned
            # grab values for username and password from db
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
                # redirect to homepage
                flask.redirect("../../frontend/index.html", 200)
                return "logged in", 200
            else:
                # invalid password
                # send 401 bad request response
                print("Incorrect password")
                response = "Incorrect Password", 401
                return response
    else:
        # send 400 bad request response
        response = "Bad Request: Missing required JSON", 400
        return response


# logout api request
@app.route("/api/logout", methods=["POST"])
@flask_login.login_required
def logout():
    flask_login.logout_user()
    return "Logged Out", 200


# create user api request
@app.route("/api/newuser", methods=["POST"])
def newuser():
    username = flask.request.get_json()['username']
    password = flask.request.get_json()['password']
    # check database for already existing user with the same name
    selection = db.getUser(username)
    if selection is None:
        # if there are no existing users with that username in the db...
        # create a new account with the username and password
        db.createAccount(username, password)
        return "Account created", 200
    else:
        return "Account already exists with username", 400


@app.route("/api/class/<classname>/update_time", methods=["POST"])
@flask_login.login_required
def update_time(classname):
    # updates the time studied for a class
    username = flask_login.current_user.get_id()
    t = flask.request.get_json()['added']
    res = db.addStudyTime(username, classname, t)
    print(username, " increased ", classname, "'s study time by: ", t, " seconds")
    return "Time for class updated successfully", 200


@app.route("/api/class/<classname>", methods=["GET"])
@flask_login.login_required
def getClass(classname):
    username = flask_login.current_user.get_id()
    res = db.getSingleClass(username, classname)
    if res is None:
        # no class found
        return "Bad Request: No class found", 400
    else:
        return res


@app.route("/api/class/<classname>/task")
@flask_login.login_required
def all_tasks(classname):
    username = flask_login.current_user.get_id()
    res = db.getSingleClass(username, classname)
    if res is None:
        # no class found
        return "Bad Request: No class found"
    res = db.getTaskList(username, classname)
    return res


@app.route("/api/class", methods=["GET"])
@flask_login.login_required
def all_classes():
    username = flask_login.current_user.get_id()
    res = db.getClasses(username)
    # auto calls jsonify and parses iterable of dictionaries
    return res


@app.route("/testlogin")
@flask_login.login_required
def testlogin():
    return "<h1>you're logged in</h1>"
