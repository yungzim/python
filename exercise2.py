number1 = int(input("Enter random number here: "))
number2 = int(input("Enter second number: "))

# if number1 % number2 ==0:
#     print(f"the number {number1} is a multiple of 4")
if number1 % number2 == 0:
    print(f'{number1} divided by {number2} gives you {number1/number2} which is an even number')
else:
    print(f"{number1} / {number2} gives you {number1/number2}. an odd number")

