#Умова: N студентів отримали K яблук і розподілити їх між собою порівну. Неподілені яблука залишились у кошику. Скільки яблук отримає кожен студент? Скільки яблук залишиться в кошику?

#Програма отримує числа N і K. Вона повинна вивести два числа: відповіді на поставлені вище питання.

#Вхідні дані: 2 цілих числа.  Кожне число користувач вводить в окремому рядку.

#Вихідні дані: вивести два числа. Перше - кількість яблук у студента, друге - кількість яблук, що лишилось у кошику.

students = int(input('Enter number students: '))
apple = int(input('Enter number apples: '))

if students < apple:
    print('',0,'\n',apple)
else:
    print(' ',students//apple,'\n',students%apple)