# Задача 9: По данному целому неотрицательному n вычислите значение n!. N! = 1*2*3*...*N (произведение всех чисел от 1 до N) 
# 0! = 1. Решить задачу, используя цикл while
# input 5, output 120

'''
n = 5

factorial = 1
while n > 1:
    factorial *= n
    n -= 1

print(factorial)
'''

# Задача 11: Дано натуральное число A > 1. Определите, каким посчету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# Input: 5, Output: 6

'''
a = int(input())
if a == 0:
    print(0)
else:
    fib_prev, fib_next = 0, 1
    n = 2
    while fib_next <= a:

        if fib_next == a:
            print(n)
            break
        fib_prev, fib_next = fib_next, fib_prev + fib_next
        n += 1
    else:
        print(-1)
'''

# Задача 13:Уставшие от необычно теплой зимы, жители решили узнать,действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в который 
# среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел. Каждое число – среднесуточная температура в соответствующий день. Температуры – целые 
# числа и лежат в диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10, Output: 2

'''
n = 6
numbers = "-20 30 -40 50 10 -10".split(" ")

length = 0  # Текущая длина последовательности тёплых дней
max_length = 0  # Максимальная длина последовательности тёплых дней

for i in range(n):
    el = int(numbers[i])

    if el > 0:
        length += 1
    else:
        length = 0

    if length > max_length:
        max_length = length


print(max_length)
'''

# Задача 15:  Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,записанных на новой строчке каждое. 
# Здесь каждое число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9, Output: 1 9

'''
lst = list(map(int, input("Введите числа: ").split(" ")))
print(min(lst), max(lst))
'''