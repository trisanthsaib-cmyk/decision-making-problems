#1) print Hello World
print("Hello, World!")
#2) Sum of two numbers
a = int(input("Enter the First Number:"))
b = int(input("Enter the Second Number:"))
c = a+b
print("Sum of two numbers is:",c)
#3) Area of Circle
r = int(input("Enter the radius value:"))
A = 3.14*r**2
print("Area of circle=",A)
#4) Swap two numbers without using temp
x = int(input("Enter the First Value:"))
y = int(input("Enter the Second Value:"))
x = x+y
y = x-y
x = x-y
print("Swap of two numbers without using temp:",x,y)
#5)Convert Celsius to Faherenheit
C = int(input("Enter the Celsius Value:"))
F = (9/5*(C) + 32)
print("Celsius to Faherenheit is:",F)
#6)Convert Celsius to Kelvin
C = int(input("Enter the Celsius Value:"))
K = 273+C
print(f"Celsius to Kelvin is {K}:")
#7) Swap two numbers with using temp
x = int(input("Enter the First Value:"))
y = int(input("Enter the Second Value:"))
temp = x
x = y
y = temp
print(f"swap of two numbers using temp:{x},{y}")
#8)Quadratic equation 
a = int(input("Give the a value:"))
b = int(input("Give the b value:"))
c = int(input("Give the c value:"))
d =(b**2-4*a*c)
r1 = ((-b+(d**0.5))/2*a)
r2 = ((-b-(d**0.5))/2*a)
print(f"Roots:{r1},{r2}")
#9)Currency converter
amount = int(input("Give the  amount value:"))
s = float(input("Give the euro value:"))
e = amount*s
print(f"Equivalent amount in EUR:{e}")