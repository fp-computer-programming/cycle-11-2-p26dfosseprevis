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


def is_palandrome(text):
    text = list(text)
    for i,letter in enumerate(text):
        if letter == " ":
            text.pop(i)
    print(text)
    textr = text
    textr.reverse
    return text == textr



print(find_evens(1,9))
print(find_evens(0, 2763))

print(is_palandrome("race car"))
print(is_palandrome("tacocat"))
print(is_palandrome("dont care"))