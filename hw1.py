'''3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и 
 выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
*Пример:*
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3'''

while True:
    print('X ≠ 0 и Y ≠ 0 ')
    x=int(input('Enter the number representing the coordinate X: '))
    y=int(input('Enter the number representing the coordinate Y: '))
    if not(y==0 or x==0):
        break
print('x=',x, 'y=',y, '-> ', end='')
if (x>0):
    if (y>0):
        print('1')
    else:
        print('4')
if (x<0):
    if (y>0):
        print('2')
    else:
        print('3')