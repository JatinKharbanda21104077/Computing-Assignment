#ques1
#pyhton program to find average of 3 numbers
#take input
num1=float(input('Enter first number: '))
num2=float(input('Enter second number: '))
num3=float(input('Enter third number: '))
#calculate average
avg=(num1 + num2 +num3)/3
#result
print(avg)

#ques 2
#pyhton program to compute person's income tax
#input gross income
grossinc=float(input('Enter your gross income: '))
#input number of dependents
dependents=float(input('Enter number of dependents: '))
taxableincome=grossinc-10000-(dependents*3000)
tax=(20*taxableincome)/100
print(tax)

#ques 3
#python program to store different data type in list
#input
name=input('Enter your name: ')
gender=input('Your Gender(M for male , F for female , U for unknown):')
SID=input('Enter your SID: ')
CourseName=input('Enter your course name: ')
CGPA=float(input('Enter your CGPA: '))
student=[SID,name,gender,CourseName,CGPA]
print(student)

#ques 4
#Write a python program to enter marks of 5 students into a list and display
#them in sorted manner.
num1=float(input('Enter marks of student 1: '))
num2=float(input('Enter marks of student 2: '))
num3=float(input('Enter marks of student 3: '))
num4=float(input('Enter marks of student 4: '))
num5=float(input('Enter marks of student 5: '))
marks=[num1,num2,num3,num4,num5]
print(marks)

#ques 5
#5-a
color1=['Red','Green','White','Black','Pink','Yellow']
print(color1)
color1.pop(3)
print(color1)

#5-b
color2=['Red','Green','White','Black','Pink','Yellow']
color2[3:5]=['Purple']
print(color2)
