def name_mulitplication(names):
    names = [input("name 1:"),input("name 2:"),input("name 3:"),input("name 4:"),input("name 5:")]
    letters_used = []
    for name in names:
        i = 0
        while i < len(name):
            if name[i] not in letters_used:
                print(name)
                letters_used.append(name[i])
                  
            i += 1
        letters_used = []      

name_mulitplication()                