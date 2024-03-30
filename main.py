from datetime import datetime, timedelta
import random
import re


def get_days_from_today(date):
    try:
        datetime_from_past = datetime.strptime(date, "%Y-%m-%d")
        current_date = datetime.now()
        return current_date.toordinal() - datetime_from_past.toordinal()
    finally:
        print("Incorrect data, must be in format 'year-month-day', try again")
        return None

def get_numbers_ticket(min, max, quantity):
    lottery_numbers = set()
    while len(lottery_numbers) < quantity:
        random_number = random.randint(min, max)
        lottery_numbers.add(random_number)
    return sorted(lottery_numbers)

def get_upcoming_birthdays(users):
    upcoming_birthdays_list = []
    current_date = datetime.now().date()
    for user in users:
        next_birthday_date = datetime.strptime(
            user.get("birthday"), "%Y.%m.%d").date().replace(year=current_date.year)
        if (next_birthday_date - current_date).days < 0:
            next_birthday_date = next_birthday_date.replace(
                year=current_date.year + 1)
        if (next_birthday_date - current_date).days < 7:
            birthday_person = {"name": user.get("name"),
                               "congratulation_date": next_birthday_date.strftime("%Y.%m.%d")}
            if next_birthday_date.weekday() >= 5:
                birthday_person.update({"congratulation_date":
                                        (next_birthday_date + timedelta(days=7-next_birthday_date.weekday())).strftime("%Y.%m.%d")})
            upcoming_birthdays_list.append(birthday_person)
    return upcoming_birthdays_list

def normalize_phone(phone_number):
    normalize_phone_number = re.sub("/D", "", phone_number)
    if normalize_phone_number[0] == "0":
        normalize_phone_number = "+38" + normalize_phone_number
    else:
        normalize_phone_number = "+" + normalize_phone_number
    return normalize_phone_number
