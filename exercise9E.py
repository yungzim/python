import random

lucky_number = random.randint(1,9)
guess_count = 0

while guess_count < 3:
    guess = int(input("Guess the lucky number 1 - 9: "))
    guess_count += 1
    if guess == lucky_number:
        print("Boom!!, That is correct!")
        break
else:
    print(f"you ran out of chances, the lucky number is {lucky_number}")




