def find_evens(num_a,num_b):
    o = []
    ask = input("Do you want to enter your own numbers? (y/n)")[0]
    if ask == "y":
        num_a = input("num_1: ")
        num_b = input("num_2: ")
    for num in range(num_a,num_b):
        if num == int(num/2)*2:
            o .append(num)
    return o


print(find_evens(1,9))
print(find_evens(0, 2763))
