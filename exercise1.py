name = input('What is your name: ')
age = int(input("What is your age: "))
turn_hundred = (2019 - age) + 100
random_number = int(input("Enter any number between 1 and 5: "))

result = f"hi {name} you will be turning 100 years old in {turn_hundred}. Enjoy! \n" * random_number

print(result)

