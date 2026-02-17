# Find the output of the following Index: 
# 1.If  
name = '''Hi How are you?
Starterd learning python.
It's really interesting.''' 
print(name[::-2])
# Then what is the output of following code
print(name[:])
print(name[-10:-5]) #teres
print(name[3:12]) #How are y
print(name[12:3]) #empty string
print(name[5,6]) #it is used in tuple
print(name[-4:-12]) #(empty string)
print(name[::2]) #H o r o?Satr erigpto.I' elyitrsig
print(name[::-2]) 
# .nteen larst
# nhy nnaldert
# uyeawHi



# 2. 
L1 = ['a' , 'b', 20, 30, 't', 100, 300, 400, 'Happy', 'major']
print(L1[:])
print(L1[::3])
print(L1[::-2])

# d.How to extract  value “Happy” based on index and negative index
L1 = ['a' , 'b', 20, 30, 't', 100, 300, 400, 'Happy', 'major']
print(L1[8])

# e.How to check type of data in list at 4th position
print(type(L1[3]))

# f.Extract values for 100, 300, 400 
print(L1[5:8])

# 3.
l2 =[1,2,3,5,['a', 'b', 'work hard'],100 , 200, "Success"] 
print(l2[4]) #['a', 'b', 'work hard']
print(l2[1:5]) #[2,3,5,['a', 'b', 'work hard']]
print(l2[7]) #Success
print(l2[7][2]) #c
print(l2[7][2:]) #ccess
print(l2[ : 3]) #[1, 2, 3]
print(l2[3:]) #[5, ['a', 'b', 'work hard'], 100, 200, 'Success']


#4.From the above print l2 value ‘b’ must be changed to ‘BEE’
l2 =[1,2,3,5,['a', 'b', 'work hard'],100 , 200, "Success"]

l2[1] = 'BEE'
print(l2)

l2 = [1, 3, 5, ['a', 'b', 'work hard'], 100, 200, 'Success', {'insect': ['bee', 'moth'], 'bird': ['parrot', 'sparrow']}]
insect_info = l2[-1]['insect']
print(insect_info)

# 5.From print l2 “BEE” has to discard.
l2.remove("BEE")
print(l2)

# 6.In print l2 add a dictionary at the end 
# {‘insect’: [‘bee’, ‘moth’] , ‘bird’ : [‘parrot’, ‘sparrow’]}
l2.append({'insect': ['bee', 'moth'] , 'bird' : ['parrot', 'sparrow']})
print(l2)

# 7.From print l2 extract insect information.
l2 = [1, 3, 5, ['a', 'b', 'work hard'], 100, 200, 'Success', {'insect': ['bee', 'moth'], 'bird': ['parrot', 'sparrow']}]
print(l2[7]['insect'])

# 8.Create a dictionary d1 = {‘a’:10, ‘b’:20, ‘c’ : 30} and add the d1 at 2nd position of print l2
d1 = {'a':10, 'b':20, 'c' : 30}
l2 = [1, 3, 5, ['a', 'b', 'work hard'], 100, 200, 'Success', {'insect': ['bee', 'moth'], 'bird': ['parrot', 'sparrow']}]
l2.insert(1, d1)
print(l2)

# 9.Based on new print l2 created here extract the value 10 from print l2 dictionary.
l2 = [1, {'a': 10, 'b': 20, 'c': 30}, 3, 5, ['a', 'b', 'work hard'], 100, 200, 'Success', {'insect': ['bee', 'moth'], 'bird': ['parrot', 'sparrow']}]
print(l2[1]['a'])

# 10.If print l2 =[1,2,3,5, (90,40,50,10), ‘Python’, 400 ,[‘a’, ‘b’, ‘work hard’],100 , 200, “Success”, (200,300, “Hundreds”)] 
# then what is the output of following

l2 =[1,2,3,5, (90,40,50,10), 'Python', 400 ,['a', 'b', 'work hard'],100 , 200, "Success", (200,300, "Hundreds")]

print(l2[4][2]) #50
print(l2[5][:]) #Python
# print(l2[2] [:]) #error
print(l2[1:5]) #[2, 3, 5, (90, 40, 50, 10)]
print(l2[5]) #  Python 
print(l2[5][3:-1])  #ho
print(l2[-1]) #(200, 300, 'Hundreds')
# print(l2[-4, -3]) #TypeError: list indices must be integers or slices, not tuple
print(l2[-4: -10])
print(l2[7][2]) #[]
print(l2[-7][2:]) #thon
print(l2[ :- 3])  #[1, 2, 3, 5, (90, 40, 50, 10), 'Python', 400, ['a', 'b', 'work hard'], 100]
print(l2[-3:]) #[200, 'Success', (200, 300, 'Hundreds')]

# ============================================
# IF-ELIF-ELSE:
# ============================================


# 11. Ask user to enter marks and define the class
# Distinction > 80
# First Class > 60
# Second Class > 50
# Pass > 35
# Fail < 35

# Solution WITHOUT function 
marks = int(input("Enter marks: "))

if marks > 80:
    print("Distinction")
elif marks > 60:
    print("First Class")
elif marks > 50:
    print("Second Class")
elif marks >= 35:
    print("Pass")
else:
    print("Fail")


# Solution WITH function
def classify_marks(marks):
    if marks > 80:
        return "Distinction"
    elif marks > 60:
        return "First Class"
    elif marks > 50:
        return "Second Class"
    elif marks >= 35:
        return "Pass"
    else:
        return "Fail"

m = int(input("Enter marks: "))
print(classify_marks(m))


#  Ask user to enter a number and check if it is
# Positive, Negative or Zero

# Solution WITHOUT function 
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# Solution WITH function 
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

n = int(input("Enter a number: "))
print(check_number(n))


# 8. Ask user to enter age and check voting eligibility

# Solution WITHOUT function 
age = int(input("Enter age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")


# Solution WITH function
def check_vote(age):
    if age >= 18:
        return "Eligible to vote"
    else:
        return "Not eligible"

a = int(input("Enter age: "))
print(check_vote(a))


# 12. Ask user to enter salary per year and rating (A/B/C/D)
# Calculate increment based on conditions

# WithOut function
salary = float(input("Enter salary (in LPA): "))
rating = input("Enter rating (A/B/C/D): ").upper()
increment = 0

if salary <= 5:
    if rating == 'A':
        increment = 0.16
    elif rating == 'B':
        increment = 0.12
    elif rating == 'C':
        increment = 0.10
    elif rating == 'D':
        increment = 0.06

elif salary <= 10:
    if rating == 'A':
        increment = 0.14
    elif rating == 'B':
        increment = 0.10
    elif rating == 'C':
        increment = 0.08
    elif rating == 'D':
        increment = 0.06

elif salary <= 15:
    if rating == 'A':
        increment = 0.08
    elif rating == 'B':
        increment = 0.06
    elif rating == 'C':
        increment = 0.04
    elif rating == 'D':
        increment = 0

elif salary <= 23:
    if rating == 'A':
        increment = 0.07
    elif rating == 'B':
        increment = 0.05
    elif rating == 'C':
        increment = 0.04
    elif rating == 'D':
        increment = 0

new_salary = salary + (salary * increment)
print("New Salary:", new_salary, "LPA")


# With function
def calculate_increment(salary, rating):
    inc = 0

    if salary <= 5:
        inc = {'A':0.16,'B':0.12,'C':0.10,'D':0.06}.get(rating,0)
    elif salary <= 10:
        inc = {'A':0.14,'B':0.10,'C':0.08,'D':0.06}.get(rating,0)
    elif salary <= 15:
        inc = {'A':0.08,'B':0.06,'C':0.04,'D':0}.get(rating,0)
    elif salary <= 23:
        inc = {'A':0.07,'B':0.05,'C':0.04,'D':0}.get(rating,0)

    return salary + (salary * inc)

s = float(input("Enter salary (in LPA): "))
r = input("Enter rating (A/B/C/D): ").upper()
print("New Salary:", calculate_increment(s, r), "LPA")







# # 
# 13.Ask user to opt for courses for master degree based on the following
# L1 = [“HR”, “Finance”, “Marketing”, “DS”]
# Based on above subject there are two different streams. For example- HR is having HR core and HR analytics and Marketing is having core and Marketing analytics. Analytics is the optional subject and having added extra fees. DS is not having analytics.
# If fees for L1 is 2 lakhs for each course core subject having the same fees but analytics subject having 10% extra on 2 lakhs.
# If student opts for hostel then 2 lakhs per year is added. For food monthly 2000 .
# Transportation charges 13000 per semester. Calculate the total annual cost based on selected service.  
# User will enter values as subject, analytics(Y/N), Hostel (Y/N), food(How many months?), Transportation(semester/annual)


L1 = ["HR", "Finance", "Marketing", "DS"]

CORE_FEE = 200000                 
ANALYTICS_EXTRA_PCT = 0.10        
HOSTEL_PER_YEAR = 200000         
FOOD_PER_MONTH = 2000
TRANSPORT_PER_SEM = 13000         

subject = input("Enter subject (HR/Finance/Marketing/DS): ").strip().title()

if subject not in [s.title() for s in L1]:
    print("Invalid subject! Choose from HR, Finance, Marketing, DS.")
    raise SystemExit

if subject == "Ds":
    subject = "DS"
elif subject == "Hr":
    subject = "HR"

analytics = input("Analytics? (Y/N): ").strip().upper()
hostel = input("Hostel? (Y/N): ").strip().upper()

food_months = input("Food months (0-12): ").strip()
if not food_months.isdigit():
    print("Food months must be a number (0 to 12).")
    raise SystemExit
food_months = int(food_months)
if food_months < 0 or food_months > 12:
    print("Food months must be between 0 and 12.")
    raise SystemExit

transport_choice = input("Transportation (semester/annual): ").strip().lower()
if transport_choice not in ["semester", "annual"]:
    print("Transportation must be 'semester' or 'annual'.")
    raise SystemExit


analytics_available = subject in ["HR", "Marketing"]

course_fee = CORE_FEE

if analytics == "Y":
    if analytics_available:
        course_fee += CORE_FEE * ANALYTICS_EXTRA_PCT
    else:
        print(f"Analytics is not available for {subject}. Ignoring analytics choice.")


hostel_fee = HOSTEL_PER_YEAR if hostel == "Y" else 0
food_fee = food_months * FOOD_PER_MONTH

if transport_choice == "semester":
    transport_fee = 2 * TRANSPORT_PER_SEM   
else:
    transport_fee = 2 * TRANSPORT_PER_SEM   


total_annual_cost = course_fee + hostel_fee + food_fee + transport_fee


print("\n------ COST BREAKDOWN (ANNUAL) ------")
print("Subject:", subject)
print("Course fee:", int(course_fee))
print("Hostel fee:", hostel_fee)
print("Food fee:", food_fee, f"({food_months} months)")
print("Transport fee:", transport_fee, f"({transport_choice})")
print("------------------------------------")
print("Total Annual Cost:", int(total_annual_cost))

# 

# 16.
string = """In most organized forms of writing, such as essays, 
paragraphs contain a topic sentence.This topic sentence of the 
paragraph tells the reader what the paragraph will be about. 
Essays usually have multiple paragraphs that make claims to 
support a thesis statement, which is the central idea of the essay. """

print(string)


# Type Casting 
# 17.Create a=100 

a = 100
print(a)
print(type(a))

# Convert a to string 
a = 100
a_str = str(a)
print(a_str, type(a_str))

# Convert a to list    
a = 100
s_list = [100]
print(s_list)
print(type(s_list))

a = 100
a_list = list(str(a))
print(a_list)

# Convert a to tuple  
a = 100
a_tuple = tuple(str(a))
print(a_tuple)

# Convert a to dict 
a = 100
a_dict = {'value': a}
print(a_dict)

a = 100
a_dict = {i: int(d) for i, d in enumerate(str(a), start=1)}
print(a_dict)

# Convert a to set 
a = 100
a_set = {}

# Convert to float 
# Observe the errors and note it down for all conversions. 

a = 100
a = float(a)
print(a)
print(type(a))

# 8.Create city = “Pune” 
# Convert to int     
# Convert float 
# Convert list  
# Convert tuple 
# Convert dict 
# Convert set 
# Observe errors and note it down for all conversions 

# Convert to int 
city = "Pune"
s = int(city)
print(s)
print(type(s)) #ERROR ==> int() works only with digit strings

# Convert float 
float(city)  # ==> float also require digits

# Convert list 
city = "Pune"
print(list(city))

# Convert tuple 
city = "Pune"
print(tuple(city))

# Convert dict 
city = "Pune"
print(dict(city)) #ERROR ==> dict() expects key-value pairs

# Convert set 
city = "Pune"
print(set(city)) #order may change



# 9.Create marks = [20,18,15,17,18]
# Convert to int
# Convert float
# Convert list
# Convert tuple
# Convert dict
# Convert set
# Observe errors and note it down for all conversions

# Convert to int
marks = [20,18,15,17,18]
s = int(marks)
print(s)
print(type(s))  # ERROR ==> int() works only on single numeric value, not list


# Convert to float
marks = [20,18,15,17,18]
float(marks)   # ERROR ==> float() requires single number, not list


# Convert to list
marks = [20,18,15,17,18]
print(list(marks))   


# Convert to tuple
marks = [20,18,15,17,18]
print(tuple(marks))   


# Convert to dict
marks = [20,18,15,17,18]
print(dict(marks))   # ERROR ==> dict() expects key-value pairs (like (key,value))


# Convert to set
marks = [20,18,15,17,18]
print(set(marks))   



# 10. List operations
# Create empty list snames
# Add 20 using append
# Add 30 using extend
# Add values using append
# Add "WORK" using extend
# Create combo = [1,'a','b',2,3]
# Add snames to combo using +
# Add combo to snames using append
# Add combo to snames using extend

snames = []
print(snames)

snames.append(20)
print(snames)

snames.extend([30])
print(snames)

snames.append(40)
snames.append(50)
print(snames)

snames.extend("WORK")  
print(snames)

combo = [1, 'a', 'b', 2, 3]
print(combo)

new_combo = combo + snames
print(new_combo)

snames.append(combo)
print(snames)

snames.extend(combo)
print(snames)


# 11. Create l1 having 2 elements and l3 having 7 elements. Now at 4th position add l1

l1 = [99, 100]
l3 = [1, 2, 3, 4, 5, 6, 7]
print(l3)
l3.insert(3, l1)  
print(l3)



# 

# 12. Collection list operations
# collection = [1,2,3,['a','b','c'],100,'Nisha',20.50,90.10]
# if int or float multiply with 5
# delete "Nisha"
# find location of 20.50

collection = [1, 2, 3, ['a', 'b', 'c'], 100, 'Nisha', 20.50, 90.10]
print("\nOriginal collection:", collection)

for i in range(len(collection)):
    if type(collection[i]) in (int, float):
        collection[i] = collection[i] * 5

print("After multiplying int/float by 5:", collection)

if "Nisha" in collection:
    collection.remove("Nisha")
print("After removing 'Nisha':", collection)

if 20.50 in collection:
    print("Index of 20.50:", collection.index(20.50))
else:
    print("20.50 not found")


# 13. Comprehensive list for square upto 10

squares = [i*i for i in range(1, 11)]
print(squares)


# 14. Comprehensive list to find numbers divisible by 13 till 200

div13 = [i for i in range(1, 201) if i % 13 == 0]
print(div13)


# 15. Create list divisible by 4 from 300 to 400

div4 = [i for i in range(300, 401) if i % 4 == 0]
print(div4)


# 16. Comprehensive list for all combinations of x and y
# x_list = [0..x-1], y_list = [0..y-1], output pairs [i,j]

x = int(input("Enter x: "))
y = int(input("Enter y: "))

x_list = [i for i in range(x)]
y_list = [j for j in range(y)]

pairs = [[i, j] for i in x_list for j in y_list]

print("x_list:", x_list)
print("y_list:", y_list)
print("Pairs:", pairs)




# 21.How to create empty set? 
s = {}
print(type(s))


# 22. Create set s1 and s2 and perform set operations

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print(s1)
print(s2)
print(s1 | s2) #Union
print(s1 & s2) #Intersection
print(s1 - s2) #Difference s1-s2
print(s2 - s1) #Difference s2-s1
print(s1 ^ s2) #Symmetric Difference

# 23. Create l2 as a list and perform set operation on s1 with l2

l2 = [3, 4, 4, 7, 8]
print(l2)
print(s1 | set(l2))
print(s1 & set(l2))


# 24. Password: first 4 chars of name + @ddmm (DOB as DD-MM-YYYY)

name = input("Enter name: ")
dob = input("Enter DOB (DD-MM-YYYY): ")

password = name[:4] + dob[-4:]
print("Generated Password:", password)


# 
# 25. Create a function to accept mobile number.
# Mobile number should contain 10 digits.
# No alphabets, spaces or special characters.

mobile = input("Enter mobile number: ")

if mobile.isdigit() and len(mobile) == 10:
    print("Valid mobile number")
else:
    print("Invalid mobile number")




# 
# 26. Pattern
# *
# * *
# * * *
# * * * *


for i in range(1, 5):
    print("* " * i)


# 27. Pattern
# ****
# ***
# **
# *


for i in range(4, 0, -1):
    print("*" * i)




# 28. Str_val = "ABCD"
# A
# A B
# A B C
# A B C D


str_val = "ABCD"
for i in range(1, len(str_val) + 1):
    print(" ".join(str_val[:i]))




# 29. Pattern
# A
# BB
# CCC
# DDDD

val = "ABCD"
for i in range(len(val)):
    print(val[i] * (i + 1))


# 30. Pattern
# 1
# 22
# 333
# 4444



for i in range(1, 5):
    print(str(i) * i)


# 31. Val = "ABCD"
# D
# DC
# DCB
# DCBA

Val = "ABCD"
rev = Val[::-1]
for i in range(1, len(rev) + 1):
    print(rev[:i])


# 32. Ask user string. If UPGRAD then
# D
# DA
# DAR
# DARG
# DARGP
# DARGPU



user_str = input("Enter a string: ").strip()
rev_user = user_str[::-1]
for i in range(1, len(rev_user) + 1):
    print(rev_user[:i])


# 33. Odd numbers 1 to 10
# 1) for loop
# 2) list comprehension

# Using for loop:
odd_list_loop = []
for i in range(1, 11):
    if i % 2 != 0:
        odd_list_loop.append(i)
print(odd_list_loop)


# Using list comprehension:

odd_list_comp = [i for i in range(1, 11) if i % 2 != 0]
print(odd_list_comp)


# 34. Even number list using for loop from 200 to 250

even_list = []
for i in range(200, 251):
    if i % 2 == 0:
        even_list.append(i)
print(even_list)


