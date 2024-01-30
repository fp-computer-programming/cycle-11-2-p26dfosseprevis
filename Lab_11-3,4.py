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


#Lab 11_4 


print("Fib time")
ask = int(input("how many?"))
i = 2
fib = [0,1]
while i < ask:
    fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])
    i += 1
print (fib) 
print (sum(fib))   