import webapp2

form = '''
<form method="post"">
	Wha is you birthday?
	<br>

	<label>
	Month
	<input type="text" name="month">
	</label>

	<label>
	Day
	<input type="text" name="day">
	</label>

	<label>
	Year
	<input type="text" name="year">
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


class MainPage(webapp2.RequestHandler):
	def write_form(self, error=""):
		self.response.out.write(form % {"error": error})

    def get(self):
        self.write_form()

    def post(self):
    	user_month = valid_month(self.request.get('month'))
    	user_day = valid_day(self.request.get('day'))
    	user_year = valid_year(self.request.get('year'))	
    	 
    	if not (user_month and user_day and user_year):
    		self.write_form("Data isn't valid!")
    	else:
    		self.response.out.write("Thanks, data is valid")


              




app = webapp2.WSGIApplication([('/', MainPage)], debug=True)


