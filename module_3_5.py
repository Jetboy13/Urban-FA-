def get_multiplied_digits(number):
    str_number = str(number)
    i = int(str_number[0])
    if len(str_number) > 2:
        return i * get_multiplied_digits(int(str_number[1:]))
    else:
        return i

result = get_multiplied_digits(40203)
print(result)

result2 = get_multiplied_digits(402030)
print(result2)
