def turp(object):
    for arg in object:
        print(f'Слово - {arg}, его длина - {len(arg)}')

def lst(object):
    counter_letters = 0
    counter_numbers = 0
    for arg in object:
        if isinstance(arg, int):
            counter_numbers += 1
        if isinstance(arg, str):
            counter_letters += 1
    print(f'Букв в списке - {counter_letters}, цифр в списке - {counter_numbers}')

def number(object):
    counter_odd = 0
    for el in str(object):
        if int(el) % 2:
            counter_odd += 1
    print(f'Колличество нечетных цифр - {counter_odd}')

def string(object):
    counter_letters = 0
    for i in object.split():
        if i.isalfa():
            counter_letters += 1

    print(f'Колличество букв - {counter_letters}')

obj = 'rt48'

if isinstance(obj, tuple):
    turp(obj)
elif isinstance(obj, list):
    lst(obj)
elif isinstance(obj, int):
    number(obj)
elif isinstance(obj, str):
    string(obj)
else:
    print('Unknown type')


