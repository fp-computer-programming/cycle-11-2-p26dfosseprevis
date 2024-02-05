list = [] #creates empty list

#creates a list useing given numbers
while 1:
    num = int(input("Give me a number: ")) # asks user for a number
    if num == -1: #ends list creation once you type -1
        break
    else: #adds number to list as long as its not -1
        list.append(num)

for number in list:#goes into list to check each number
    number = int(number)
    if number % 3 != 0: #skips print statement if programs detacts that num is not divisable by 3
        continue
    print (number)