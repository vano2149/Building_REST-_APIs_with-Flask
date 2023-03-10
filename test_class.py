"""
test_class.py file!
"""

class Date:
    def __init__(self, day = 0, month = 0, year = 0):
        self.day = day
        self.month = month
        self.year = year
    
    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('.'))
        date1 = cls(day, month, year)
        return date1

    def is_valid_date(date_as_string):
        if date_as_string.count(".") == 2:
            day, month, year = map(int, date_as_string.split('.'))
            return day<=31 and month<=12 and year<= 3999

    def string_to_db(self):
        return f"{self.year}-{self.month}-{self.day}"


if __name__ == "__main__":
    dates = [
        '30.12.2020',
        '30-12-2020',
        '01.01.2021',
        '12.31.2020'
    ]
    for string_date in dates:
        if Date.is_valid_date(string_date):
            date = Date.from_string(string_date)

            string_to_db = date.string_to_db()
            print(string_to_db)
        else:
            print(f"Неправильная дата или формат строки с датой!")