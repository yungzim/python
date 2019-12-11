item = int(input("Enter: "))
itemlist = list(range(1, item+1))
rangelist = []

for i in itemlist:
    if item % i == 0:
        rangelist.append(i)
print(rangelist)
