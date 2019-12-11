import random

a = random.sample(range(1, 100), 16)
b = random.sample(range(1, 100), 20)
c = []

for i in a and b:
    if i in a and b:
        c.append(i)
print(c)
