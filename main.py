import webapp2
import cgi

form = '''
<form method="post"">
	Wha is you birthday?
	<br>

	<label>
	Month
	<input type="text" name="month" value="%(month)s">
	</label>

	<label>
	Day
	<input type="text" name="day" value="%(day)s">
	</label>

	<label>
	Year
	<input type="text" name="year" value="%(year)s">
	</label>



	<div style="color: red">%(error)s</div>

	<input type="submit">
</form>
'''
months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']


def valid_month(month):
    if month.capitalize() in months:
        return month.capitalize()


def valid_day(day):
    if day.isdigit() and int(day) in range(1, 31):
        return int(day)
    else:
        return None


def valid_year(year):
    if year.isdigit() and int(year) in range(1900, 2020):
        return int(year)
    else:
        return None

def escape_html(s):
    s = cgi.escape(s, quote = True)
    return s


class MainPage(webapp2.RequestHandler):
    def write_form(self, error="", month="", day="", year=""):
        self.response.out.write(form % {"error": escape_html(error),
                                        "month": escape_html(month),
                                        "day": escape_html(day),
                                        "year": escape_html(year)})

    def get(self):
        self.write_form()

    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)

        if not (month and day and year):
            self.write_form("Data isn't valid!", user_month, user_day, user_year)
        else:
            self.redirect("/thanks")


class Thanks(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Thanks, data is valid")

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/thanks', Thanks)], debug=True)


