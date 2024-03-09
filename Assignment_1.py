# Write a programe to determine whether a person is eligible to vote.
A=int(input('enter your age'))
if (A < 18):
    print('not eligible for vote')
else:
    print('eligible for vote')

# Programe to print the largest of the two numbers.
b=int(input("enter the num 1"))
c=int(input('enter the num 2'))
if (b > c):
    print ('b is grater') 
else:
    print ('c is grater')

# Programe to print the largest of the three numbers.
b=int(input("enter the num 1"))
c=int(input('enter the num 2'))
d=int(input('enter the num 3'))
if (b > c) and (b > d):
    print ('The lagrgest num is',b)
elif (c > b) and (c > d):
    print('The lagrgest num is',c)
else:
    print ('The lagrgest num is',d)

# write a programe to find wheather the given numbers is even or odd
a=int(input('enter the num1'))
if (a % 2)== 0:
    print ('the num is even')
else:
    print('the num is odd')

# write a programe to find whether a given year is a leap or not
a=int(input('enter the num1'))
if (a % 4)== 0:
    print ('is leap year')
else:
    print('is not leap year')

# Programe that prompts the user to enter a number and then print its interval
n=int(input("enter the num"))
for i in range(n):
    print(i)
# Program that prompts the user to enter a number & then print its interval
n1=int(input("enter the number1"))
n2=int(input("enter the number2"))
for A in range (1,11):
    print(A)

# write a program to enter any characte. if the enteredcharacter is in lowercase then convert it into uppercase &
# if it is an uppercase character,then convert into lowercase.
Char=input("enter a char:")
if Char.isupper():
    print("Char is uppercase")
    conv_char=Char.lower()
    print("converted char is:",conv_char)
elif Char.islower():
    print("Char is lowercase")
    conv_char=Char.upper()
    print("converted char is:",conv_char)
else:
    print("please enter an alphabet char")

# Program to test whether a num entered by user is negative,positive or equal to zero
A= 10
num=int(input("enter the number"))
print(A==num)
print("num is equals to A")
print(A < num)
print("num is negative")
print(A > num)
print("num is negative")
print(num== 0)

# write a Program to determine whether character entered is vowel or not
Vowels= ["a","e","i","o","u"]
Char= input("enter the char:")
if (Char in Vowels):
    print("char is vowel")
else:
    print("char is not vowel")

# Students Results
Maths=40
Marathi=40
Science=20
English=20
Total=(Maths+Marathi+Science+English)
print("Total Marks:",Total)
# check here how to remove float from percentage 
percentage=(Total/400)*100 
print("Aggregate is:",percentage,"%")
if percentage >75:
    print("Distinction")
elif percentage >=60 and percentage <75:
    print("Frist Class")
elif percentage >=50 and percentage <60:
    print("Second Class")
elif percentage >=40 and percentage <50:
    print("Third Class")
else:
    print("Fail")