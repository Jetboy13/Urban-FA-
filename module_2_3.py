my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
while 0 < len(my_list):
    if my_list[a] > 0:
        print(my_list[a])
        a += 1
        if my_list[a] == 0:
            del my_list[a]
        continue
    break