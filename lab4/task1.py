# import math
# def the_area_og_the_triangle(side1,side2,angle):
#     return 0.5*side1*side2*math.sin(angle)
#
# side1=float(input("Side1="))
# side2=float(input("Side2="))
# angle=float(input("Angle="))
#
# total=the_area_og_the_triangle(side1,side2,angle)
# print("Total={0}".format(total))
import math
a=float(input('Enter a = '))
b=float(input('Enter b = '))
angle=float(input("Angle="))
s=0.5*a*b*math.sin((math.pi * angle) / 180)
print("S={0}".format(s))


