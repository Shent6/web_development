import webapp2
import cgi
import re

form = '''
<form method="post">
    <label>
        Username
        <br>
        <input name="username" type="text" value="%(username)s">
    </label>
    <div style="color: red">%(username_error)s</div>

    <br>

    <label>
        Password
        <br>
        <input name="password" type="password" value="%(password)s">
    </label>
        <div style="color: red">%(password_validation_error)s</div>


    <br>

    <label>
        Verify password
        <br>
        <input name="verify" type="password" value="%(verify)s">
    </label>
    <div style="color: red">%(password_error)s</div>

    <br>

    <label>
        E-mail(Optional)
        <br>
        <input name="email" type="text" value="%(email)s">
    </label>

    <br>

    <input type="submit">

</form>
'''

def username_validation(username):
    USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    return USER_RE.match(username)

def password_validation(password):
    PASSWORD_RE = re.compile(r"^.{3,20}$")
    return PASSWORD_RE.match(password)


def escape_html(s):
    s = cgi.escape(s, quote = True)
    return s


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.out.write("Hello")


class SignUp(webapp2.RequestHandler):

    def write_form(self, username_error="", password_validation_error="", password_error="", username="", password="", verify="", email=""):
        self.response.out.write(form % {"username": username,
                                        "password": password,
                                        "verify": verify,
                                        "email": email,
                                        "username_error": username_error,
                                        "password_validation_error": password_validation_error,
                                        "password_error": password_error
                                        })

    def get(self):
        self.write_form()

    def post(self):
        user_username = self.request.get('username')
        user_password = self.request.get('password')
        user_verify = self.request.get('verify')
        user_email = self.request.get('email')

        escaped_username = escape_html(user_username)
        escaped_email = escape_html(user_email)

        username_error=""
        password_validation_error=""
        password_error=""

        if not username_validation(user_username):
            username_error="username is not valid"
        if not password_validation(user_password):
            password_validation_error="password is not valid"
        if password_validation(user_password) and user_password != user_verify:
            password_error="passwords dont match"

        if not username_validation(user_username) or not password_validation(user_password) or user_password != user_verify:
            self.write_form(username_error, password_validation_error, password_error, escaped_username)
        else:
            self.redirect("/unit2/welcome")

class Welcome(webapp2.RequestHandler):

    def get(self):
        self.response.out.write("Welcome")


app = webapp2.WSGIApplication([('/', MainPage),
                               ('/unit2/signup', SignUp),
                               ('/unit2/welcome', Welcome)], debug=True)