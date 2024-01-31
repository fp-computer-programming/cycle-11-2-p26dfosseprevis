def length_multiples(list):
    new_list = []
    for i,item in enumerate(list):
        new_list.append(item * i)
    return new_list    


print(length_multiples([1,2,3,4,5]) == [0, 2, 6, 12, 20])
print(length_multiples([1.7,1.6,3.3,9.3,4]) == [0.0, 1.6, 6.6, 27.900000000000002, 16])
print(length_multiples(["sean","greg","chara","jeff"]) == ['', 'greg', 'charachara', 'jeffjeffjeff'])
