import datetime

month_to_number = {'January': 1,
                   'February': 2,
                   'March': 3,
                   'April': 4,
                   'May': 5,
                   'June': 6,
                   'July': 7,
                   'August': 8,
                   'September': 9,
                   'October': 10,
                   'November': 11,
                   'December': 12}
number_to_month = ['January',
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
class Date:
    def __init__(self, year=0, month=0, day=0):
        self.year = year
        self.month = month
        self.day = day
    def set(self, year=0, month=0, day=0):
        self.year = year
        self.month = month
        self.day = day
    def set_current(self, year=0):
        self.year = datetime.datetime.now().year
        self.month = datetime.datetime.now().month
        self.day = datetime.datetime.now().day
    def to_string(self):
        return str(self.year) + '/' + str(self.month) + '/' + str(self.day)
    def to_dict(self):
        return {'year': self.year, 'month': self.month, 'day': self.day}
current_date = Date()
current_date.set_current()
def to_date(dict):
    tmp = Date(dict["year"], dict["month"], dict["day"])
    return tmp
