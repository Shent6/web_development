import webapp2
import cgi

form = '''
<form method="post">
    <label>
    ROT13
    <br>
    <textarea name="text" type="text">%(text)s</textarea>
    </label>
    <br>
    <input type="submit">

</form>
'''


def caesar(text):
    a = ["a", "b" ,"c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    cap_a = [x.upper() for x in a]
    cipher = []
    for i in text:
        if i in a:
            ind = a.index(i)
            try:
                bukva = a[ind+13]
            except:
                bukva = a[ind-13]
            cipher.append(bukva)
        elif i in cap_a:
            ind = cap_a.index(i)
            try:
                bukva = cap_a[ind+13]
            except:
                bukva = cap_a[ind-13]
            cipher.append(bukva)
        else:
            bukva = i
            cipher.append(bukva)
    return ''.join(cipher)


def escape_html(s):
    s = cgi.escape(s, quote = True)
    return s


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.out.write("Hello")


class Rot(webapp2.RequestHandler):

    def write_form(self, text=""):
        self.response.out.write(form % {"text": text})

    def get(self):
        self.write_form()

    def post(self):
        user_text = self.request.get('text')

        rot_text = caesar(user_text)
        escaped_rot = escape_html(rot_text)
        self.write_form(escaped_rot)


app = webapp2.WSGIApplication([('/', MainPage),
                               ('/unit2/rot13', Rot)], debug=True)