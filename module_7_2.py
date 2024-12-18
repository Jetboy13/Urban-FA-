def custom_write(file_name, strings):

    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}
    for i, string in enumerate(strings, start=1):
        file.write(string + '\n')
        byte_position = file.tell()
        strings_positions[(i, byte_position)] = string

    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('../test.txt', info)

# Вывод результатов
for elem in result.items():
    print(elem)