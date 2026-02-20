        #VARIABLES AND BASIC OPERATIONS
#favorite color,lucky number,birth year
favorite_color="blue"
lucky_number=10
birth_year=2004
print(f"my favorite color is {favorite_color}, my lucky number is {lucky_number}, and l was born in {bin}.")

#sum , difference, product and quotient
number1=float(input("first_number:"))
number2=float(input("second_number:"))
sum=number1+number2
difference=number1-number2
product=number1*number2
quotient=number1/number2 
print(f"sum:{sum}")
print(f"product:{product}")
print(f"difference:{difference}")
print(f"quotient:{quotient}")

#celsius to fahrenheit converter
celsius=float(input("temperature in celsius:"))
fahrenheit=(celsius*9/5)+32
print(f"{celsius}c is equal to {fahrenheit}f")

            #STRING MANIPULATION
#full name in uppercase,lowercase,and titlecase
fullname=input("fullname:")
print(f"uppercase:{fullname.upper()}") 
print(f"lowercase:{fullname.lower()}")  
print(f"titlecase:{fullname.title()}")

#wordcount in a sentence
sentence=input("sentence:")
count=len(sentence.split())
print(f"wordcount:{count}")

#palindrome checker
word=input("word:")
if word==word[::-1] :
    print("the word is a palindrome.")
else:
    print("the word is not a palindrome.") 

            #CONDITIONALS
#grade calculator
score=float(input("score(0-100):"))
if score>=90:
    grade="A"
elif score>=80:
    grade="B"
elif score>=70:
    grade="C"
elif score>=60:
    grade="D"
else:
    grade="F"
print(f"your grade is :{grade}")

#age category
age=int(input("age:"))
if age<=12:
    category="child"
elif age<=19:
    category="teen"
elif age<=65:
    category="adult"
else:
    category="senior"
print(f"my age category is:{category}")

#number guessing game
import random
number=random.randint(1,10)
while True:
    guess=int(input("number between 1 and 10:"))
    if guess <number:
        print("too low!")
    elif guess >number:
        print("too high!")
    else:
        print("congratulations! you guessed the correct number.")
        break

            #LISTS AND BASIC LOOPS 
#fruit list
fruits=["orange","apple","banana","mango"]
for a,fruit in enumerate(fruits, start=1):
    print(f"{a}.{fruit}")

#largest and smallest numbers
numbers=[]
for i in range (5):
    num=float(input(f"number{i+1}:"))
    numbers.append(num)
print(f"largest number:{max(numbers)}")
print(f"smallest number:{min(numbers)}")

