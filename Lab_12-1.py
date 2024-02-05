def find_evens(num_a,num_b):
    o = [] #list inside def so every time function is called list is emptyed
    ask = input("Do you want to enter your own numbers? (y/n)")[0] #asks user for a confermation but only saves the first letter to avoid errors
    if ask == "y": #if user says yes lets them add their own numbers
        num_a = input("num_1: ")
        num_b = input("num_2: ")
    for num in range(num_a,num_b):# checks every number between the two numbers
        if num % 2 == 0: #adds number to list if meets even requirements 
            o .append(num)
    return o

#tests the function
print(find_evens(1,9))
print(find_evens(0, 2763))
