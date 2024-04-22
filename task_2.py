import random


def get_numbers_ticket(min, max, quantity):
    lottery_numbers = set()
    while len(lottery_numbers) < quantity:
        random_number = random.randint(min, max)
        lottery_numbers.add(random_number)
    return sorted(lottery_numbers)