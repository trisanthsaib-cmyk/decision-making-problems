#factorial
n = int(input())
fact = 1
for i in range(1,n+1):
    fact = fact*i
print(fact)
#Reverse Number
n = int(input())
reverse = 0
while n>0:
    d = n%10
    reverse = reverse*10+d
    n = n//10
print(reverse)
#Sum of a digits of a number
n = int(input())
sum = 0
while n>0:
    d = n%10
    sum = sum+d
    n = n//10
print(sum)
#palindrome
n = int(input())
x = n
reverse = 0
while n>0:
    d = n%10
    reverse = reverse*10+d
    n = n//10
print(reverse)
if x == reverse:
    print("palindrome")
else:
    print("Not a palindrome")
#Multiplication
n = int(input("Enter a number:"))
i = 1
while i<=10:
    print(f"{n}x{i}={n*i}")
    i+=1
#Sum Of natural numbers
n = int(input("Enter a number:"))
i = 1
sum = 0
while i<=n:
    sum = sum+i
    i+=1
print(f"{sum}")