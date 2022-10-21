import test


def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

def calc(num1,num2,sign):
    '''num1 = int(input("Ведите первое число: "))
    num2 = int(input("Ведите второе число: "))
    sign = str(input("Введите знак операции: "))'''
    result = int(0)
    if sign == "+":
        result = num1 + num2
    elif sign == "-":
        result = num1 - num2
    elif sign == "/":
        result = num1 / num2
    elif sign == "*":
        result = num1 * num2

    return result

def is_sorted_from_min_to_max(array):
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            return False
    return True

def bubblesort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def main():
    '''arr = [2, 3, 5, 1, 2]
    print(arr)
    arr = bubblesort(arr)
    print(arr)
    fibonacci(4)
    #calc()

    data = list(fibonacci(3))
    print(data)'''


if __name__ == '__main__':
    main()