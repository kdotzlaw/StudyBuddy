import flask
import flask_login

app = flask.Flask(__name__)
app.secret_key = "secret string"  # TEMP, CHANGE THIS LATER (SERIOUSLY)

# instantiate flask login manager
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# mock persistance layer
users = {"testuser": {"password": "123"}}


# tell flask how to load a user from a flask request and from it's session

class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(username):
    if username not in users:
        return
    user = User()
    user.id = username
    return user


@login_manager.request_loader
def request_loader(request):
    username = request.form.get("username")
    if username not in users:
        return
    user = User()
    user.id = username
    return user


# deal with unauthorized access attempts
@login_manager.unauthorized_handler
def unauthorized_handler():
    return "Unauthorized", 401


@app.route("/")
def hello_world():
    return "<h1>hello world</h1>"


@app.route("/api/login", methods=["GET", "POST"])
def login():
    # send the user the login form
    if flask.request.method == 'GET':
        return '''
                   <form action='login' method='POST'>
                    <input type='text' name='username' id='username' placeholder='username'/>
                    <input type='password' name='password' id='password' placeholder='password'/>
                    <input type='submit' name='submit'/>
                   </form>
                   '''

    username = flask.request.form['username']
    if username in users and flask.request.form['password'] == users[username]['password']:
        user = User()
        user.id = username
        flask_login.login_user(user)
        return flask.redirect(flask.url_for('testlogin'))

    return 'Bad login'


@app.route("/api/logout")
@flask_login.login_required
def logout():
    flask_login.logout_user()
    return "Logged Out"


@app.route("/testlogin")
@flask_login.login_required
def testlogin():
    return "<h1>you're logged in</h1>"
>>>>>>> Stashed changes
