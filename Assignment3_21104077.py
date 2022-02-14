#Answer 1

a=str(input("ENTER ANY STRING: ")) #taking string input from user
list=a.split() 
dict={} 
if list.__len__()==1:   
    for i in list[0]:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)   
else:                   
    for i in list:                   #checking the occurence
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
print("\n")


#Answer 2

Mon_30 = [4, 6, 9, 11]                     #Months with 30 days
Mon_31 = [1, 3, 5, 7, 8, 10, 12]           #Months with 31 days
def input_date():
    global day
    global month
    global year
    day = int(input("Please Enter The Day: "))
    month = int(input("Please Enter The Month: "))
    year = int(input("Please Enter The Year: "))
    if year>2025 or year<1800 or month<1 or month>12 or day<1 or day>31:
        print("Please Re-enter A Valid Date OR Only Enter A Year Between 1800 and 2025")
    if day > 28 and month == 2 and year%4 != 0:  #february has 28 days in non leap year
        print("Please Re-enter A Valid Date!!")
        input_date()
    elif ((day > 29 and month == 2) and (year%4 == 0 and year%100 != 0 or year%400 == 0)):  #leap year case
        print("Please Re-enter A Valid Date!!")
        input_date()
    elif day > 30 and month in Mon_30:
        print("Please Re-enter A Valid Date!!")
        input_date()
        #Now we will calculate the next day in every possible case
input_date()
if day == 28 and month == 2 and year%4 != 0:   
    day = 1
    month = 3
elif ((day == 28 and month == 2) and (year%4 == 0 and year%100 != 0 or year%400 == 0)):
    day += 1
elif ((day == 29 and month == 2) and (year%4 == 0 and year%100 != 0 or year%400 == 0)):
    day = 1
    month = 3
elif day == 30 and month in Mon_30:
    day = 1
    month += 1
elif day == 31:
    day = 1
    month += 1
else:
    day += 1
if month == 13:
    month = 1
    year += 1
print("Next Date Is: ", day,'/',month,'/',year)


#Answer 3

num=[5,14,36]
result=[]
for i in num:
    result.append((i,i**2))      #adding tuples of numbers and  its squares
print(result)



#Answer 4

grade=int(input("ENTER YOUR GRADE BETWEEN 4 TO 10: "))#taking grade input from user
if(grade>10 or grade<4):
    print("Error\nPLEASE ENTER CORRECT GRADE")  #grade is between 4 and 10
elif(grade==4):
    print("Your performance is poor ")
elif(grade==5):
    print("Your performace is Below Average")
elif(grade==6):
    print("Your performace is Average ")
elif(grade==7):
    print("Your performace is Good")
elif(grade==8):
    print("Your performance is Very Good ")
elif(grade==9):
    print("Your performance is Excellent")
else:
    print("Your performance is outstanding ")
print("\n")


#QUESTION 5

x = 6
for i in range(x):           #the pattern is in 6 lines
    for j in range(i):         
        print(' ', end='')           #adding spaces before alphabet according to pattern
    for j in range(2*(x-i)-1):
        print(chr(65 + j), end='')      #printing capital alphabets using ASCII table
    print()
print("\n")


#Answer 6

sid = int(input("Enter SID: ")) # taking input of name and sid from user
name = input("Enter Name: ")
students = {sid:name}

while True:
    wish = input("Do you want to enter another student details(Y or N): ").upper() #Ask whether to Enter details of another student or not
    if wish == 'Y':
        sid = int(input("Enter SID: "))
        name = input("Enter Name: ")
        students[sid] = name
    elif wish == 'N':
        break
    else:
     print('Invalid input!!!')

#a-part

print("a." ,students)  #student details

#b-part

print("b." ,{k:v for k,v in sorted(students.items(), key= lambda x:x[1])})   #sorting using names

#c-part

print("c." ,{k:v for k,v in sorted(students.items())}) #sorting using sid

#d-part

search = int(input("Please Enter SID Of The Student You Want To Search: " )) 
print("d. Student With The Given SID Is: " ,students[search])


#Answer 7
def fibonacci(n):    #making a fibonacci function
    if n==1 or n==0:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)   #using previos terms to find next term
m=int(input("Enter number of terms of series\n"))
sum=0
if m<1:
    print("Enter a valid number as term>=1")
else:
    for s in range(m):
        print(fibonacci(s))
        sum=sum+fibonacci(s)
avg=float(sum/m)
print("Average of this fibonacci is ",avg) #average of fibonacci
    
 
#Answer 8

Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}

# a part

A_Set = (Set1|Set2)-(Set1&Set2)  #all elements that are in Set1 and Set2 but not in both
print("a. ", A_Set)

# b part

B_Set = (Set1|Set2|Set3) - ((Set1&Set2)|(Set2&Set3)|(Set3&Set1))   #all elements that are in only one of the three sets Set1, Set2 and Set3
print("b. ", B_Set)

# c part

C_Set= ((Set1&Set2)|(Set1&Set3)|(Set3&Set2))-(Set1&Set2&Set3)      #of elements that are exactly two of the sets Set1, Set2 and Set3.
print("c. ",C_Set)

# d part
                                                                   #set of all integers in the range 1 to 10 that are not in Set1
D_Set = set()
for i in range(1, 11):
    if i not in Set1:
        D_Set.add(i)
print("d. ", D_Set)

# e part
                                                             #set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3.
E_Set = set()
for i in range(1, 11):
    if i not in Set1 and i not in Set2 and i not in Set3:
        E_Set.add(i)
print("e. ", E_Set)
