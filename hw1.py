""" Напишите программу, которая принимает на вход координаты двух точек 
и находит расстояние между ними в 2D пространстве. 
Пример: - A (3,6); B (2,1) -> 5,09 - A (7,-5); B (1,-1) -> 7,21 """


def intNum(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = int(input(f"Enter the coordinate for {xy[i]}: "))
                a.append(number)
                is_OK = True
            except ValueError:
                print("You wrong. Enter whole numbers!")
    return a


def calculateLengthSegment(a, b):
    lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return lengthSegment


print("Enter point the 'A' coordinates") 
pointA = intNum(2)
print("Enter point the 'B' coordinates")
pointB = intNum(2)

print(f"Cut length: {format(calculateLengthSegment(pointA, pointB), '.3f')}")