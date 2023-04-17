import random


class Lottery:

    def __init__(self, numbers):
        self.numbers = numbers
        self.winner_numbers = []

    def calculate_numbers_lottery(self):
        count = 0
        while count < 5:
            number = random.randrange(1, 69)
            if number not in self.winner_numbers:
                self.winner_numbers.append(number)
                count += 1
        return self.winner_numbers

    def calculate_powerball_number(self):
        return random.randrange(1,26)

    def show_numbers(self):
        self.winner_numbers.sort()
        for number in self.winner_numbers:
            print(number, end=' ')
