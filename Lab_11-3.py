#lab 11_3

import random as ran

print("Lets play number guess!")
num = ran.randint(1,100)
print(num)
win = False
while win != True:
    ask = int(input("whats your guess: "))
    if ask == num:
        win = True
    elif ask > num:
        print("less")    
    else:
        print("higher")    
print("good job")


