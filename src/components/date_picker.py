from tkcalendar import Calendar

class Date_picker():
    def __init__(self, root, x, y):
        self.calendar = Calendar(root, selectmode="day")
        self.calendar.place(x= x, y=y)

    def date_calendar(self):
        return self.calendar.get_date()