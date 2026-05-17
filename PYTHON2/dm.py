#Even or odd
n = int(input())
if (n%2==0):
    print(f"{n} is even")
else:
    print(f"{n} is odd")
print("code is succesfully executed")
#numb is +ve,-ve,zero
n = int(input("Enter the number :"))
if (n<0):
     print(f"{n} is negative")
elif (n>0):
    print(f"{n} is positive")
else:
    print(f"{n} is zero")
print("code is succesfully executed")
#Leap Year
y = int(input("Enter a year:"))
if ((y%4==0 and y%100 != 0) or y%400==0 ):
        print(f"{y} is  a leap year")
else:
        print(f"{y} is not a leap year")

print("code is succesfully executed")
#Palindrome
x = input("Enter the string:")
r = x[::-1]
if x == r:
    print(f"{x} is a palindrome")
else:
    print(f"{x} is not a palindrome")
#calculator
a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
c = ((input("Enter the operator:")))
if c == "+":
  print("a+b=",a+b)
elif c == "-":
  print("a-b=",a-b)
elif c == "*":
  print("a*b=",a*b)
elif c == "/":
  print("a/b=",a/b)
else:
    print("Nothing")
#Anagrams
x = input("Enter a string:")
y = input("Enter a string:")
z = sorted(x)
v = sorted(y)
s = len(x)
d = len(y)
if z == v:
   if s == d:
       print("Two strings are anagrams")
else:
    print("They are not anagrams")
print("code is succesfully run")
#Armstrong
s = int(input("Enter a number"))
a = s
digit = len(str(s))
sum = 0
while a > 0:
    d = a%10
    sum+= d**digit
    a //= 10
if s == sum:
   print("Armstrong number")
else:
    print("Not a armstrong number")
#prime number
n = int(input("Enter a number: "))

if n <= 1:
    print(f"{n} is neither prime number nor composite numbers")
else:
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} is not a prime number")
            break
    else:
        print(f"{n} is a prime number")
print(f"Code is successfully executed")
