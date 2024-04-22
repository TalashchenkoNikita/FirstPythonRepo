from datetime import datetime, timedelta


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
                                            (next_birthday_date + timedelta(
                                                days=7 - next_birthday_date.weekday())).strftime("%Y.%m.%d")})
            upcoming_birthdays_list.append(birthday_person)
    return upcoming_birthdays_list
