import flask
import flask_login

app = flask.Flask(__name__)
app.secret_key = 'kisumu_level_up'  #You can change this!

login_manager = flask_login.LoginManager()
login_manager.init_app(app)


users = {'ogol@lakehub.com': {'password': 'secret'}}

class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email

    user.is_authenticated = request.form['password'] == users[email]['password']

    return user

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized, Login first'


#main route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        return '''
               <form action='login' method='POST'>
                <input type='text' name='email' id='email' placeholder='email'/>
                <input type='password' name='password' id='password' placeholder='password'/>
                <input type='submit' name='submit'/>
               </form>
               '''

    email = flask.request.form['email']
    if flask.request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return flask.redirect(flask.url_for('protected'))

    return 'Bad login'


@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Welcome: ' + flask_login.current_user.id


@app.route('/logout')
def logout():
    flask_login.logout_user()
    return "Thank you. You've Logged out"

@app.route('/comment')
@flask_login.login_required
def comment():
    #return 'Welcome: ' + flask_login.current_user.id
    return '''
               <form action='comment' method='POST'>
                <input type='text' name='comment' id='comemnt' placeholder='Comment'/>
                <input type='submit' name='submit'/>
               </form>
               '''
    comments = {'comment' : flask.request.form['comment']}
    print(comments)

if __name__ == '__main__':
    app.run(debug=True, port=2020)
