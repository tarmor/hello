side1= float (input ("Insert side 1: "))
side2= float (input ("Insert side 2: "))
side3= float (input ("Insert side 3: "))

if  side1>(side2+side3) or side2 >(side1+side3) or side3>(side1+side2):
    print ("This is not triangle!")
elif side1==side2==side3:
    print ("It is a equilateral triangle!")
elif  (side1==side2 and side1!=side3) or (side2==side3 and side2!=side1) or (side3==side1 and side1!=side2):
    print ("It is a Isosceles triangle!")
elif side1!=side2!=side3:
    print ("It is a Scalene triangle!")

