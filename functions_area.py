def area_circle(r):
    return 3.14*r*r


def area_rectangle(l, b):
    return l*b


def area_triangle(l, b):
    return 0.5*l*b


num = int(input("enter the number: "))
r = int(input("enter the radius if it is a circle"))
l = int(input("enter the length if it is a ractangle or a triangle"))
b = int(input("enter the breadth if it is a ractangle or a triangle"))

if (num == 1):
    print("this is a circle")
    area = area_circle(r)
elif (num == 2):
    print("this is a rectangle")
    area = area_rectangle(l, b)
elif (num == 3):
    print("this is a triangle")
    area = area_triangle(l, b)
print("the area is")
