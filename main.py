user_num = input('Введите число для поиска: ')
input_str = '2 3 4 6 1 5 9 8 7 22 45 98 223 556 4 7 8'


def binary_search(array, element, left, right):
    if left > right:
        try:
            return ('Введенное число отсутсвует в последовательности.\n'
                    'Ближайшие имеющиеся числа:\n'
                    f'{array[right]} <индекс [{right}]>,\n'
                    f'{array[left]} <индекс [{left}]>')
        except IndexError:
            return ('Введенное число отсутсвует в последовательности.\n'
                    'Ближайшее число:\n'
                    f'{array[right]} <индекс [{right}]>')
    middle = (right+left) // 2
    if array[middle] == element:
        return (f'Ваше число {array[middle]} найдено <индекс [{middle}]>\n'
                f'Предыдущее число {array[middle - 1]} '
                f'<индекс [{middle - 1}]>\n'
                f'Следующее число {array[middle + 1]} <индекс [{middle + 1}]>')
    elif element < array[middle]:
        return binary_search(array, element, left, middle-1)
    else:
        return binary_search(array, element, middle+1, right)


def qsort(array, left, right):
    middle = (left+right) // 2
    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)
    return array


def data_handler(user_number, data_str):
    try:
        user_number = int(user_number)
        array = list(map(int, data_str.split()))
        qsort(array, 0, len(array)-1)
        return binary_search(array, user_number, 0, len(array) - 1)
    except ValueError:
        return f'"{user_number}" не является числом.'


print(data_handler(user_num, input_str))
