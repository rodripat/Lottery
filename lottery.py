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

    def lottery_prizes(self, hits, mistery_ball):
        if hits == 5 and mistery_ball is True:
            return "Jackpot"
        elif hits == 5 and mistery_ball is False:
            return "1000000"
        elif hits == 4 and mistery_ball is True:
            return "50000"
        elif (hits == 4 and mistery_ball is False) or (hits == 3 and mistery_ball is True):
            return "100"
        elif(hits == 3 and mistery_ball is False) or (hits == 2 and mistery_ball is True):
            return "7"
        elif (hits == 1 and mistery_ball is True) or (hits == 0 and mistery_ball is True):
            return "4"
        else:
            return "No prizes this time."

    def show_numbers(self):
        self.winner_numbers.sort()
        for number in self.winner_numbers:
            print(number, end=' ')


