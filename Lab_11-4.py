print("Fib time")
ask = int(input("how many?"))
i = 2
fib = [0,1]
while i < ask:
    fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])
    i += 1
print (fib) 
print (sum(fib))   