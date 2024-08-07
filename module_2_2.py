first = int(3)
second = int(7)
third = int(11)
print(first, second, third)
if first == second == third:
    print('3')
elif first == second or first == third or second == third:
    print('2')
else:
    print('0')