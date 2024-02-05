list = []
while 1:
    num = int(input("Give me a number: "))
    if num == -1:
        break
    list.append(num)
for number in list:
    number = int(number)
    if number % 3 != 0:
        continue
    print (number)