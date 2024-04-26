import pytest
from calculator import Calculator #из файла calculator импортируй класс

calculator = Calculator()

@pytest.mark.skip #декоратор для пропуска теста
def test_sum_positive_nums():
    calculator = Calculator()
    res = calculator.sum(4, 5)
    assert res == 9

@pytest.mark.skip(reason="починить тест позже") #указали параметр и причину
def test_sum_positive_nums():
    calculator = Calculator()
    res = calculator.sum(4, 5)
    assert res == 9

@pytest.mark.xfail
def test_sum_positive_nums():
    calculator = Calculator()
    res = calculator.sum(4, 5)
    assert res == 9  

@pytest.mark.positive_test #создали собственную маркировку
def test_sum_positive_nums():
    calculator = Calculator()
    res = calculator.sum(4, 5)
    assert res == 9  
# def test_sum_positive_nums(): #создали ранее в этом степе
#     calculator = Calculator()
#     res = calculator.sum(4, 5)
#     assert res == 9

# def test_sum_negative_nums(): #создали ранее в этом степе
#     calculator = Calculator()
#     res = calculator.sum(-6, -10)
#     assert res == -16

# def test_sum_positive_and_negative_nums(): #создали ранее в этом степе
#     calculator = Calculator()
#     res = calculator.sum(-6, 6)
#     assert res == 0

# def test_sum_float_nums(): #проверка сложения десятичных дробей
#     calculator = Calculator()
#     res = calculator.sum(5.6, 4.3)
#     res = round(res, 1)  
#     assert res == 9.9

# def test_sum_zero_nums(): #проверка сложения целого числа и нуля
#     calculator = Calculator()
#     res = calculator.sum(10, 0)
#     assert res == 10

# def test_div_positive(): #проверка деления чисел
#     calculator = Calculator()
#     res = calculator.div(10, 2)
#     assert res == 5

# def test_div_by_zero(): #проверка деления на ноль
#     calculator = Calculator()
#     res = calculator.div(10, 0)
#     assert res == None 

# def test_avg_empty_list(): #проверка нахождения среднего для пустого списка
#     calculator = Calculator()
#     numbers = []
#     res = calculator.avg(numbers)
#     assert res == 0

# def test_avg_positive(): #проверка нахождения среднего для списка
#     calculator = Calculator()
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
#     res = calculator.avg(numbers)
#     assert res == 5

# calculator.sum

# #Проверка сложения положительных чисел
# res = calculator.sum(4, 5)
# assert res == 9

# #Проверка сложения отрицательных чисел\
# res = calculator.sum(-6, -10)
# assert res == -16

# #Проверка сложения отрицательного и положительного чисел
# res = calculator.sum(-6, 6)
# assert res == 0

# #Проверка сложения десятичных дробей
# # res = calculator.sum(5.6, 4.3)
# # print(res)
# # assert res == 9.9
# res = calculator.sum(5.6, 4.3) #Python посчитает сумму
# res = round(res, 1) #округлит ее до одного знака после запятой
# print(res) #напечатает сумму
# assert res == 9.9 #сравнит с предполагаемым значением

# #Проверка сложения числа и нуля
# res = calculator.sum(10, 0)
# assert res == 10

# #Проверка деления чисел
# res = calculator.div(10, 2)
# assert res == 5

# #Проверка нахождения среднего арифметического
# numbers = []
# res = calculator.avg(numbers)
# assert res == 0
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5] #сумма чисел будет = 50
# res = calculator.avg(numbers)
# print(res)
# assert res == 5 #среднее арифметическое равно 50/10

# #Проверка деления на ноль
# res = calculator.div(10, 0)
# assert res == None

# def test_sum_positive_nums():
#     calculator = Calculator()
#     res = calculator.sum(4, 5)
#     assert res == 9

# def test_sum_negative_nums(): #поменяли название теста
#     calculator = Calculator()
#     res = calculator.sum(-6, -10) #поменяли параметры
#     assert res == -16 #поменяли ожидаемую сумму

# def test_sum_positive_and_negative_nums(): #поменяли название теста
#     calculator = Calculator()
#     res = calculator.sum(-6, 6) #поменяли параметры
#     assert res == 0 #поменяли ожидаемую сумму

# #pytest и ошибки в тестах
# def test_sum_negative_nums():
#     calculator = Calculator()
#     res = calculator.sum(-6, -10)
#     assert res == -234567 #заменили число на ошибочное