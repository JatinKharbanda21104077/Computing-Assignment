
#ASSIGNMENT-2

#Question 1
sentence="Python is a case sensitive language"
#a
print(len(sentence))
#b
print(sentence[::-1])
#c
c=sentence[10:27]
print(c)
#d
d=sentence.replace("a case sensitive","object oreinted")
print(d)
#e
e=sentence.find("a")
print(e)
#f
f=sentence.replace(" ","")
print(f)

#Question 2
name="Jatin Kharbanda"
sid= 21104077
department="Electrical Engineering"
cgpa=8.7
print("Hey,",name,"Here!","\nMy SID is",sid ,"\nI am from",department, "department and my CGPA is",cgpa)

#Question 3
a=56
b=10
#a part
print(a&b)
#b part
print(a|b)
#c part
print(a^b)
#d part
print(a<<2, b<<2)
#e part
print(a>>2, b>>4)

#Question 4
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
 
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
elif (num3>=num1) and (num3>=num1):
   largest = num3   


print("The largest number is",largest)

#Question 5
enter=str(input("type: "))
if "name" in enter:
    print("yes")
else:
    print("no")

#Question 6
side1=int(input("enter the length of first side:"))
side2=int(input("enter the length of second side:"))
side3=int(input("enter the length of third side:"))

if (side1+side2>side3) and (side2+side3>side1) and (side1+side3>side2):
    print("yes")
else:
    print("no")
