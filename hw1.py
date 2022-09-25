'''Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
*Пример:*
- 6 -> да
- 7 -> да
- 1 -> нет'''


day=int(input('Enter the number of the day: '))
if day >0 and day <6:
    print ('It is a work day :( ')
elif day >5 and day <8:
    print ("It's a weekend :) uhooo!!!")
else:
    print("You enter the wrong number!!!")
