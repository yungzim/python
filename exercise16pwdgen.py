import random

string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
password_length = 8
password = "".join(random.sample(string, password_length))

print(password)
