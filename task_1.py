from datetime import datetime


def get_days_from_today(date):
    try:
        datetime_from_past = datetime.strptime(date, "%Y-%m-%d")
        current_date = datetime.now()
        return current_date.toordinal() - datetime_from_past.toordinal()
    except ValueError:
        print("Incorrect data, must be in format 'year-month-day', try again")
