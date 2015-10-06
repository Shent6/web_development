import webapp2
import cgi

form = '''
<form method="post">
    <label>
    ROT13
    <input type="text" name="text" value="%(text)s">
    </label>
    <br>
    <input type="submit">

</form>
'''


def caesar(text):
    a = ["a", "b" ,"c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    cypher = []
    for i in text:
        ind = a.index(i)
        try:
            bukva = a[ind+13]
        except:
            bukva = a[ind-13]

        cypher.append(bukva)
    return ''.join(cypher)


def escape_html(s):
    s = cgi.escape(s, quote = True)
    return s


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.out.write(form)


class Rot(webapp2.RequestHandler):

    def write_form(self, text=""):
        self.response.out.write(form % {"text": text})

    def get(self):
        self.write_form()

    def post(self):
        user_text = self.request.get('text')
        escaped_text = escape_html(user_text)
        rot_text = caesar(escaped_text)
        self.write_form(rot_text)


app = webapp2.WSGIApplication([('/', MainPage),
                               ('/unit2/rot13', Rot)], debug=True)