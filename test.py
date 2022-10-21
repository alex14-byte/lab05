import testing

# Граничные значения натуральные числа
def testFibonacci():
    n = list(testing.fibonacci(4))
    assert n == [1,1,2,3]
# Граичные значения знак "+,-,*,/" и если знак "/" то второе число не 0
def testCalc():
    n = testing.calc(1,2,"+")
    assert n == 3
# Граничные
def testSort():
    arr = [2, 3, 5, 1, 2]
    n = testing.bubblesort(arr)
    assert testing.is_sorted_from_min_to_max(arr) == True