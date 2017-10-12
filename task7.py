a = float(input('Введіть кількість хвилин: '))

if (a>1440):
   b = a%1440
else:
   b = a
x = int(b//60)
y = int(b%60)

print(x,':',y)