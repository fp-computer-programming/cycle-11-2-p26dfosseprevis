def is_palandrome(text):
    text = list(text)
    for i,letter in enumerate(text):
        if letter == " ":
            text.pop(i)
    print(text)
    textr = text
    textr.reverse
    return text == textr


print(is_palandrome("race car"))
print(is_palandrome("tacocat"))
print(is_palandrome("dont care"))