string_letters = str(input("Enter string here: "))
# appended_str = []
rvs = string_letters[::-1]

# for i in string_letters:
#     appended_str.append(i)
#
# print(appended_str)
if string_letters == rvs:
    print("palindrome")
else:
    print("not palindrome")
