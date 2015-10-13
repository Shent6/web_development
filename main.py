import webapp2
import cgi

form = '''
<form method="post">
    <label>
    Username
    <br>
    <input name="username" type="text" value="%(username)s">
    </label>
    <br>

    <label>
    Password
    <br>
    <input name="password" type="text" value="%(password)s">
    </label>
    <br>

    <label>
    Verify password
    <br>
    <input name="verify" type="text" value="%(verify)s">
    </label>
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



def escape_html(s):
    s = cgi.escape(s, quote = True)
    return s


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.out.write("Hello")


class SignUp(webapp2.RequestHandler):

    def write_form(self, username="", password="", verify="", email=""):
        self.response.out.write(form % {"username": username,
                                        "password": password,
                                        "verify": verify,
                                        "email": email})

    def get(self):
        self.write_form()

    def post(self):
        user_text = self.request.get('text')

        rot_text = caesar(user_text)
        escaped_rot = escape_html(rot_text)
        self.write_form(escaped_rot)


app = webapp2.WSGIApplication([('/', MainPage),
                               ('/unit2/signup', SignUp)], debug=True)