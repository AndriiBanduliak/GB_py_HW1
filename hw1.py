'''4. Напишите программу, которая по заданному номеру четверти, показывает 
диапазон возможных координат точек в этой четверти (x и y). - x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3'''



X=int(input('Enter the x '))
Y=int(input('Enter the y '))
    
if X > 0 and  Y > 0:
    print("The point in the 1th quarter ")
elif X < 0 and Y > 0:
    print('The point in the 2nd quarter')
elif X <0 and Y < 0:
    print('The point in the 3rd quarter')
elif X > 0 and Y < 0:
    print('The point in the 4th quarter')
else:
    print("It's the center of the coordinates")