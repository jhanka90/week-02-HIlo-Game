import random
"""The card is: 9
Higher or Lower? [h/l] l
Next card was: 5
Your score is: 400
Play again? [y/n]

"""
class Hilo:

    def __init__(self):
        self.cards = 0
        self.score = 0

    def draw(self):
        self.cards1 = random.randint(1, 13)
        self.cards2 = random.randint(1, 13)
        self.points = self.cards + 1  

        score = 300
        card1 = self.cards1
        card2 = self.cards2  

        self.points = print(f"Your score is: {score}")
        print(f"The current card is {card1}")

        self.choice = input("Is the next card higher or lower? ")

        print(f"The next card is {card2}")

        if self.choice == "h" and card1 > card2:
            print("It is lower")
            score += -100
            print(f"Your score is: {score}")
        elif self.choice == "l" and card1 < card2:
            print("It was higher")
            score += -100
            print(f"Your score is: {score}")
        elif self.choice == "h" and card1 < card2:
            print("It is higher +100.")
            self.score += 100
            print(f"Your score is: {score}")
        elif self.choice == "l" and card1 > card2:
            print("It is lower +100")
            score += 100
            print(f"Your score is: {score}")
        else:
            score -= 75
        card1 = card2