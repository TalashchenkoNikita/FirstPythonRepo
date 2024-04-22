import re


def normalize_phone(phone_number):
    normalize_phone_number = re.sub("/D", "", phone_number)
    if normalize_phone_number[0] == "0":
        normalize_phone_number = "+38" + normalize_phone_number
    else:
        normalize_phone_number = "+" + normalize_phone_number
    return normalize_phone_number
