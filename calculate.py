import datetime as dt

class Record:
    def __init__(self, amount, date, comment):
        self.amount=amount
        self.date = dt.datetime.now()
        self.comment =comment

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
    def add_record(self,record):
        self.records.append(record)
    def get_today_stats(self):
        today_amount = 0
        for r in self.records:
            if r.date == dt.datetime.now().date():
                today_amount += r.amount
        return today_amount
    def get_today_cash_remained(self):
        return (self.limit - self.get_today_stats)



