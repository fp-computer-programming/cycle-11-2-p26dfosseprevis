total = 0
while 1:
    num = int(input("Give me a number: "))
    if num == -1:
        break
    total += num
print (total)

#---------------------------------------------------------------

list = input("give me a list (seperate numbers with commas): ").split(",")
print (list)
for number in list:
    number = int(number)
    if number % 3 != 0:
        continue
    print (number)