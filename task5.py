#Умова: Напишіть програму, яка зчитує ціле число і друкує його попереднє і наступне значення за форматом:

#The next number for the number 179 is 180.
#The previous number for the number 179 is 178.

#Вхідні дані: ціле число

#Вихідні дані: два рядки за наведеним у завдання форматом

a  = int(input('Enter int number: '))

print(' The next number for the number ',a,' is ',a+1,'\n','The previous number for the number ',a,' is ',a-1)