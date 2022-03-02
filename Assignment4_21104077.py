#QUESTION 1
print("Solution to Problem 1")
#n=number of discs
def Hanoi(n , from_rod , mid, to_rod):
	if n == 0:
		return
	Hanoi(n-1, from_rod, mid, to_rod)
	print("Move Disk ",n," from rod ",from_rod," to rod ",to_rod)
	Hanoi(n-1, mid, to_rod, from_rod)
#Calling the function for 3 discs
n = 3
Hanoi(n, 'A', 'C', 'B')                
print("\n")


#QUESTION 2
print("Solution to Problem 2")
from math import factorial, remainder
n=int(input("Enter the no. of rows in Pascal's Triangle: "))
#using recursive procedure
print("By Recursion Procedure:")          

def pascal_tri(n,length = n):
    if n == 0:
        return
    pascal_tri(n-1,length)
    print('  '*(length-n), end='')
    start = 1
    for i in range(1, n+1):
        print(start, end ='   ')
        start = start * (n - i) // i      #Binomial Coefficients
    print()
pascal_tri(n)
print("\n")
#using iterative procedure
print("By Iterative Method Procedure:")           

for i in range(n):
	for j in range(n-i+1):
		print(end=" ")

	for j in range(i+1):
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")      #nCr = n!/r!(n-r)!
	print()



#QUESTION 3
print("Solution to Problem 3")
int1, int2 = map(int,input("Enter 2 numbers: ").split())
Quotient = int1 // int2
Remainder = int1 % int2

#part-a
print("a. Checking if the quotient and remainder is a callable value or not.")
print(callable(Quotient))
print(callable(Remainder))

#part-b
if (Quotient == 0):
    print("(b) The quotient is zero")
if (Remainder == 0):
    print("(b) The reminder is zero")
if (Quotient != 0 and Remainder != 0):
    print("(b) All the values are non zero")

#part-c
partClist = [Quotient + 4, Remainder + 4, Remainder + 5, Quotient + 5, Remainder + 5, Quotient + 6, Remainder + 6]

result = []
for i in range(len(partClist)):
    if partClist[i] > 4:
        result.append(partClist[i])
print(f"(c) Filtered out numbers that are greater than 4 are : {result}")

#part-d
setresult = set(result)
print("(d) Set:",setresult)

#part-e
immutableSet = frozenset(setresult) #frozen Set is used to make the set immutable
print("(e) Immutable set:",immutableSet)

#part-f
print("(f) Hash value of the max value from the above set:", hash(max(immutableSet)))


#QUESTION 4
print("Solution to Problem 4")
#creating a class to assign values for name and roll nos.
class Student:
    def __init__(self, student_name,roll_no):
        self.name = student_name
        self.roll_no = roll_no
    
    def __del__(self):
        print("Object destroyed")
student1 = Student("Jatin", 21104077)
student2 = Student("Chiranjeev", 21104087)

print(f"The name of the student is {student1.name} and his/her SID is {student1.roll_no}.")
print(f"The name of the student is {student2.name} and his/her SID is {student2.roll_no}.")
del student1
print("\n")


#QUESTION 5
print("Solution to Problem 5:")
#creating class to store details of employees
class Employee:
    def __init__(self, emp_name, emp_salary):
        self.emp_name = emp_name
        self.emp_salary = emp_salary 
employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)

#Part-a
print("part-a")
employee1.emp_salary = 70000
print(f"The Updated Salary Of {employee1.emp_name} Is {employee1.emp_salary} ")

#Part-b
print("part-b")
del employee3
print("Deleting record of employee Viren")
print("\n")


#QUESTION 6
george=input("George's word: ").strip().lower()
barbie=input("Barbie's word: ").strip().lower()

def anagram(s):
    if s=="":
        return[s]
    else:
        ans=[]
        for w in anagram(s[1:]):
            for pos in range(len(w)+1):
                ans.append(w[:pos]+s[0]+w[pos:])
        return ans

correct_words=anagram(george)
if barbie in correct_words:
    print("true friendship")
else:
    print("fake friendship")
                          
