#Hello there! I'm AjANSH, and this file is me learning Python. These are all the little programs and experiments i made during my journey of learning Python.
#All of them are turned to comments, just remove the '#' or the ''' or the """ from the programs, and they should be good to go.

#print("Welcome to Python")

'''rose = 100
print(rose)'''

'''rose = 100
flower = rose
print(flower)'''

'''total_marks = 500
print(total_marks)'''

#num= (input("Enter a number:"))

#This program adds two numbers

'''num1 =input('Enter first number:')
num2 =input('Enter second number:')


sum = int (num1) + int (num2)


print("The sum is:",sum)'''

#This program calculates area and perimeter of rectangle

'''l = float(input('Enter length:'))
b = float(input('Enter breadth:'))
area = l*b
perimeter = 2* (l+b)

print("The area of the rectangle is:",area)
print("The perimeter of the rectangle is:",perimeter)'''

'''num = int(input("Enter any number: "))
if num >= 0:
    print("Positive or Zero")
else:
    print("Negative number")'''

'''marks = int (input("Enter your marks: "))
if marks > 90:
    print("Excellent")
elif marks > 75:
    print("Very Good")
elif marks > 60:
    print("Good")
elif marks > 50:
    print("Need to work harder")
else:
    print("Poor, work very hard to score good marks")'''

'''num1 = int (input("Enter first number: "))
num2 = int (input("Enter second number:"))
num3 = int (input("Enter third number:"))
if num1 > num2:
    if num1 > num3:
        print("Num1 is greatest:", num1)
    else:
        print("Num3 is greatest:", num3)
else:
    if num2 > num3:
        print("Num2 is greatest:", num2)
    else:
        print("Num3 is greatest:", num3)'''

'''for x in range(0, 5) :
    print("AjANSH Is Cool")'''

'''Str = "AjANSH Is Cool"
for word in Str:
    print ("Letter is: ", word)'''

'''i=0
while i<5:
    print("AjANSH Is Cool")
    i=i+1'''

'''a = 25
b = 50
while a < 30 and b < 70:
    a = a + 1
    b = b + 1
    print(a, b)'''

'''for letter in 'Python' :
    if letter == 'h':
        break
    print(letter)'''

'''for letter in 'Python' :
    if letter == 'h':
        continue
    print(letter)'''

#This program calculates discount

'''Price = int(input("Enter the price: "))
if Price > 10000:
    print("Discount is 30%")
elif Price > 5000:
    print("Discount is 20%")
else:
    print("Discount is 10%")'''

#This program tells whether the given number is odd or even

'''num = int(input("Enter a number: "))
mod = num % 2
if mod != 0:
    print("This is an odd number")
else:
    print("This is an even number")'''

#This program tells the multiplication table of any number given

'''num = int(input("Enter a number: "))
for i in range(1, 11):
    print (num,'x', i, '=', num*i)'''

#This program can add natural numbers

'''num = int(input("Enter a number: "))
sum = 0
i = 1
while i <= num:
    sum = sum + i
    i = i+1
print("The sum is", sum)'''

a=0
while a<5:
     print (a)
     a+=1
     if a == 2:
          break