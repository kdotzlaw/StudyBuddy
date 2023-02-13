import flask
import flask_login
import db

app = flask.Flask(__name__)
app.secret_key = "secret string"  # TEMP, CHANGE THIS LATER (SERIOUSLY)

# instantiate flask login manager
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# mock persistence layer
users = {"testuser": [{"username": "testuser", "password": "123"}]}


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
    if len(selection) == 1 and selection[0]['username'] == username:
        user = User()
        user.id = username
        return user
    else:
        return None

# loads user from flask request
@login_manager.request_loader
def request_loader(request):
    username = request.form.get("username")
    # check database for username
    selection = user_check(username)
    if len(selection) == 1 and selection[0]['username'] == username:
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
    return flask.make_response(flask.render_template("../../frontend/index.html"))


# login api request
@app.route("/api/login", methods=["POST"])
def login():
    # grab the username from the header
    if flask.request.headers.get('username'):
        # username header exists
        username = flask.headers['username']
        # check db for username and password
        # selection is a list of rows (SHOULD BE LENGTH 1)
        selection = user_check(username)
        if len(selection) != 1:
            # multiple entries in database with same username (PROBLEM)
            response = flask.make_response(flask.render_template('server_error.html'), 500)
            return response
        else:
            # length of selection is correct
            # grab values for username and password from db
            db_username = selection[0]['username']
            db_password = selection[0]['password']
            if db_username == username and db_password == flask.headers['password']:
                user = User()
                user.id = username
                flask_login.login_user(user)
                return flask.make_response(flask.render_template("../../frontend/index.html"), 200)
            else:
                # invalid password
                # send 400 bad request response
                response = flask.make_response(flask.render_template('bad_request.html'), 400)
                return response
    else:
        # send 400 bad request response
        response = flask.make_response(flask.render_template('bad_request.html'), 400)
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
    username = flask.request.headers.get('username')
    password = flask.request.headers.get('password')
    # check database for already existing user with the same name
    selection = db.getUser(username)
    if len(selection) == 0:
        # if there are no existing users with that username in the db...
        # create a new account with the username and password
        db.createAccount(username, password)
        return "Account created", 200
    else:
        return "Account already exists with username", 400


@app.route("/testlogin")
@flask_login.login_required
def testlogin():
    return "<h1>you're logged in</h1>"
