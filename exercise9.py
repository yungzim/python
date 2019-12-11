lucky_number = 6
guess_count = 0

while guess_count < 3:
    guess = int(input("Guess the lucky number 0 - 9: "))
    guess_count += 1
    if guess == 6:
        print("That is correct!")
        break
else:
    print("you ran out of chances")


