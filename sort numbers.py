numbers = list(input("Введите последовательность целых чисел через пробел:").split(" "))
try:
    num_int = [int(x) for x in numbers]
except ValueError:
    exit("Ошибка: Введены символы кроме чисел или дробные числа")

if len(num_int) == 1:
    exit("Ошибка: В последовательности должно быть хотя бы 2 числа")

random_number = int(input("Введите любое число:"))


def sort(array):
    return array.sort()


sort(num_int)
print(num_int)


def binary_search(array, element, left, right):
    if left > right:
        return f"Индекс меньшего числа: {right}\nИндекс большего числа: {left}"

    middle = (right + left) // 2
    if array[middle] == element:
        if (middle - 1) == -1:
            return f"Индекс введенного числа: {middle}\nИндекс числа >= искомому числу: {middle + 1}"
        elif (middle + 1) == len(array):
            return f"Индекс меньшего числа: {middle - 1}\nИндекс искомого числа: {middle}"
        elif int(array[middle - 1]) < int(array[middle]):
            return f"Индекс меньшего числа: {middle - 1}\nИндекс искомого числа: {middle}\nИндекс числа >= искомому числу: {middle + 1}"
        else:
            for i in range(1, len(array) - 1):
                if int(array[middle - i]) < int(array[middle]):
                    return f"Индекс меньшего числа: {middle - i}\nИндекс искомого числа: {middle}\nИндекс числа >= искомому числу: {middle + 1}"
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


print(binary_search(num_int, random_number, 0, len(num_int)))
