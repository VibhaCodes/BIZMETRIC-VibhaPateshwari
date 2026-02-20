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










# 11. Ask user to enter marks and define the class
# Distinction > 80
# First Class > 60
# Second Class > 50
# Pass > 35
# Fail < 35

# 
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


# WITH function
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






# 14. Digitalize the book allotment process for school. Charges are mentioned here in the given table:

total = 0

std = int(input("Enter Standard (1-10): "))

if 1 <= std <= 4:
    standard = "1-4"
elif 5 <= std <= 8:
    standard = "5-8"
elif 9 <= std <= 10:
    standard = "9-10"
else:
    print("Invalid Standard")
    exit()


books = {
    "1-4": {
        "hindi": 60, "marathi": 60, "english": 80,
        "science": 90, "maths": 100
    },
    "5-8": {
        "hindi": 100, "marathi": 100, "english": 100,
        "science": 120, "maths": 140
    },
    "9-10": {
        "hindi": 150, "marathi": 150, "english": 150,
        "science": 200, "maths": 250
    }
}


choice = input("Do you want books? (yes/no): ").lower()

if choice == "yes":

    print("Subjects: Hindi Marathi English Science Maths")

    subjects = input(
        "Enter subjects separated by space: "
    ).lower().split()

    for sub in subjects:
        if sub in books[standard]:
            total += books[standard][sub]
        else:
            print("Invalid subject skipped:", sub)


notebooks = {
    "1": 40,   # square 100
    "2": 70,   # square 200
    "3": 30,   # 4 lines 100
    "4": 50,   # 4 lines 200
    "5": 30,   # single 100
    "6": 50,   # single 200
    "7": 100,  # A4 100
    "8": 180   # A4 200
}

choice2 = input("Do you want notebooks? (yes/no): ").lower()

if choice2 == "yes":

    print("""
1 Square 100 pages
2 Square 200 pages
3 Four lines 100 pages
4 Four lines 200 pages
5 Single line 100 pages
6 Single line 200 pages
7 A4 100 pages
8 A4 200 pages
""")

    nbs = input(
        "Enter notebook numbers separated by space: "
    ).split()

    for nb in nbs:
        if nb in notebooks:
            total += notebooks[nb]
        else:
            print("Invalid notebook skipped:", nb)

print("\nTotal Amount to Pay =", total)




# -------------------
#  Using functions

def user_input(*s):
    std = input('Enter which standard: ')
    book = input('Enter the subject: ')
    b_quant = input('Quantity: ')
    return dict({
        "Standard" : std,
        "Subject" : book,
        "Quantity" : b_quant
    })

print(user_input())


def get_standard():
    s = int(input("Enter Standard (1-10): "))
    if 1 <= s <= 4:
        return "1-4"
    elif 5 <= s <= 8:
        return "5-8"
    elif 9 <= s <= 10:
        return "9-10"
    else:
        print("Invalid standard")
        return None


def get_books_total(standard, book_dict):
    total = 0
    choice = input("Do you want to buy books? (yes/no): ").lower()

    if choice == "yes":
        print("Available books: Hindi Marathi English Science Maths")
        subjects = input(
            "Enter the books you want (separated by space): "
        ).lower().split()

        for sub in subjects:
            if sub in book_dict[standard]:
                total += book_dict[standard][sub]
            else:
                print(f"Invalid subject skipped: {sub}")

    return total


def get_notebooks_total(notebook_dict):
    total = 0
    choice = input("Do you want to buy notebooks? (yes/no): ").lower()

    if choice == "yes":
        notebooks = input(
            """
Choose notebooks:
1 square 100 pages
2 square 200 pages
3 4lines 100 pages
4 4lines 200 pages
5 single_line 100 pages
6 single_line 200 pages
7 A4 notebook 100 pages
8 A4 notebook 200 pages

Enter notebook numbers (separated by space):
"""
        ).split()

        for nb in notebooks:
            if nb in notebook_dict:
                total += notebook_dict[nb]
            else:
                print(f"Invalid notebook skipped: {nb}")

    return total


def BookAmount():
    book_dict = {
        "1-4": {
            "hindi": 60, "marathi": 60, "english": 80,
            "science": 90, "maths": 100
        },
        "5-8": {
            "hindi": 100, "marathi": 100, "english": 100,
            "science": 120, "maths": 140
        },
        "9-10": {
            "hindi": 150, "marathi": 150, "english": 150,
            "science": 200, "maths": 250
        }
    }

    notebook_dict = {
        "1": 40, "2": 70, "3": 30, "4": 50,
        "5": 30, "6": 50, "7": 100, "8": 180
    }

    standard = get_standard()
    if standard is None:
        return

    total = 0
    total += get_books_total(standard, book_dict)
    total += get_notebooks_total(notebook_dict)

    print(f"\nTotal amount to pay: ₹{total}")


BookAmount()






# Using oops

class BookAllotment:

    def __init__(self):

        self.book_dict = {
        "1-4": {
            "hindi": 60, "marathi": 60, "english": 80,
            "science": 90, "maths": 100
        },
        "5-8": {
            "hindi": 100, "marathi": 100, "english": 100,
            "science": 120, "maths": 140
        },
        "9-10": {
            "hindi": 150, "marathi": 150, "english": 150,
            "science": 200, "maths": 250
        }
    }

        self.notebook_dict = {
        "1": 40, "2": 70, "3": 30, "4": 50, "5": 30, "6": 50, "7": 100, "8": 180
    }


    def get_standard(self):

        s = int(input("Enter Standard (1-10): "))

        if 1 <= s <= 4:
            return "1-4"

        elif 5 <= s <= 8:
            return "5-8"

        elif 9 <= s <= 10:
            return "9-10"

        else:
            print("Invalid standard")
            return None


    def get_books_total(self, standard):

        total = 0

        choice = input("Do you want to buy books? (yes/no): ").lower()

        if choice == "yes":

            print("Available books: Hindi Marathi English Science Maths")

            subjects = input(
                "Enter subjects separated by space: "
            ).lower().split()

            for sub in subjects:

                if sub in self.book_dict[standard]:
                    total += self.book_dict[standard][sub]

                else:
                    print("Invalid subject skipped:", sub)

        return total


    def get_notebooks_total(self):

        total = 0

        choice = input("Do you want to buy notebooks? (yes/no): ").lower()

        if choice == "yes":

            print("""
1  square 100 pages
2  square 200 pages
3  4lines 100 pages
4  4lines 200 pages
5  single_line 100 pages
6  single_line 200 pages
7  A4 notebook 100 pages
8  A4 notebook 200 pages
""")

            notebooks = input(
                "Enter notebook numbers: "
            ).split()

            for nb in notebooks:

                if nb in self.notebook_dict:
                    total += self.notebook_dict[nb]

                else:
                    print("Invalid notebook skipped:", nb)

        return total


    def generate_bill(self):

        standard = self.get_standard()

        if standard is None:
            return

        total = 0

        total += self.get_books_total(standard)
        total += self.get_notebooks_total()

        print("\nTotal amount to pay:", total)



b = BookAllotment()
b.generate_bill()

# ---------------







# 15.   Create an interest bucket for Fix Deposit in the bank.
# Ask user to enter start date and end date for the FD and check which bucket list it belongs to 
# and assign the interest rate


from datetime import datetime


class FDAccount:

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self.days = 0
        self.interest_rate = 0

    def calculate_days(self):
        d1 = datetime.strptime(self.start_date, "%d-%m-%Y")
        d2 = datetime.strptime(self.end_date, "%d-%m-%Y")

        diff = d2 - d1
        self.days = diff.days

    def assign_interest(self):

        if 7 <= self.days <= 45:
            self.interest_rate = 5.75

        elif 46 <= self.days <= 179:
            self.interest_rate = 6.25

        elif 180 <= self.days <= 210:
            self.interest_rate = 6.35

        elif 211 <= self.days < 365:
            self.interest_rate = 6.40

        elif 365 <= self.days < 730:
            self.interest_rate = 7.00

        elif 730 <= self.days < 1095:
            self.interest_rate = 6.75

        elif 1095 <= self.days < 1825:
            self.interest_rate = 6.70

        elif 1825 <= self.days <= 3650:
            self.interest_rate = 6.60

        else:
            self.interest_rate = "Invalid tenure"

    def display(self):
        print("FD Tenure (days):", self.days)
        print("Interest Rate:", self.interest_rate, "%")

start = input("Enter FD Start Date (dd-mm-yyyy): ")
end = input("Enter FD End Date (dd-mm-yyyy): ")

fd = FDAccount(start, end)

fd.calculate_days()
fd.assign_interest()
fd.display()





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
print(type(a))
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
print(set(city)) #order can be different evcerytime



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
print(dict(marks))   # ERROR ==> dict() it requires key-value pairs 


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




# 17.What is the difference between add and update methods in set?  - theory
# 18.What is the difference between append and extend methods in list?  - theory
# 19.What is the difference between pop and remove methods? - theory
# 20.What is the difference between discard, pop, remove methods? - theory



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




# \
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



# 35.List2 = [2,70,'work', para, 2.5, [1,2,3], (1,2), {1,2}, {1:'a', 2:'b'}, 3,10,302.5]
# Multiply each and every element by 2 and display the answer
para = "para"

List2 = [2,70,'work', para, 2.5, [1,2,3], (1,2), {1,2}, {1:'a', 2:'b'}, 3,10,302.5]

for i in List2:
    if type(i) == int or type(i) == float or type(i) == str or type(i) == list or type(i) == tuple:
        print(i * 2)
    else:
        print(i)





# 36.List2 = [2,70,'work', para, 2.5, [1,2,3], (1,2), {1,2}, {1:'a', 2:'b'}, 3,10,302.5]
# Multiply each and every element from list2 by 2 and store the answer in list3
para = "para"

List2 = [2,70,'work', para, 2.5, [1,2,3], (1,2), {1,2}, {1:'a', 2:'b'}, 3,10,302.5]

List3 = []

for i in List2:
    
    if type(i) == int or type(i) == float or type(i) == str or type(i) == list or type(i) == tuple:
        List3.append(i * 2)
    else:
        List3.append(i)

print(List3)



# 37. Create a function to accept marks from user utilize exception concept to validate proper marks.
# marks = input("Enter the number: ")


def validate_marks():
    marks = input("Enter the marks: ")
    try:
        if marks.isdigit():
            marks = int(marks)

            if 0<= marks <=100:
                print("Enter the valid marks.")
            else:
                print("Enter the marks betn 0 and 100")
        else:
            raise ValueError
    except ValueError:
        print("Enter valid number")

validate_marks()
    



# 38.Create a function to validate user first name/last name. User first name/last name should contain only characters. 
# No special characters, numbers, space in name 


    
def validate_name():
    try:
        first_name = input("Enter your first name: ").title()
        last_name = input("Enter your last name: ").title()

        if first_name.isalpha() & last_name.isalpha():
            print(first_name+" " +last_name,' Name is correct.')       
        else:
            raise ValueError()
            
    except ValueError:
        print("Enter your valid name(No special characters, numbers, space in name)")

validate_name()

# 39.Create a function to accept mobile number. Mobile number should contain 10 digits. No Special character, alphabets and space. 

def Validate_number(contact_number):
    if contact_number.isdigit():
        if len(contact_number) == 10:
            print("Valid contact number")
        else:
            print("Invalid contact number")
    else:
        print("Enter the number correctly")


contact_number = input("Enter contact number: ")
Validate_number(contact_number)

# 40.Create a function to generate auto-password based on specific person details. Ask user to enter name, DOB. 
# And password must be First name 4 characters and year of birth.

def generate_password(name, dob):
    first_part = name[:4]
    year = dob[-4:]
    password = first_part + year
    return password


name = input("Enter your name: ")
dob = input("Enter your DOB (DD-MM-YYYY): ")

print("Generated Password:", generate_password(name, dob))


# 41.Create a empty dictionary and ask user to enter values as name, DOB, mobile number add all the details in dictionary with 
# customer number as 1 for first time. If user try to enter another value, then number should increase as 2 with new details 
# and previous values should not change.
# For example:
# {}
# {1:{name : "Sachin", "DOB": "21-06-1965" , "mobile": "1234123423"}}

# {1:{name : "Sachine", "DOB": "21-06-1965" , "mobile": "1234123423"},
# 2: {name : "Sumedh", "DOB": "02-02-2002" , "mobile": "1234123433"}}



dict1 = {}

for i in range (1,10):
    name = input("Enter name : ")
    dob = input("Enter DOB : ")
    mobile = input("Enter mobile num: ")

    if name.isalpha() and mobile.isdigit() and len(mobile) == 10:
        dict1[i] = dict({'name': name, 'DOB': dob, 'Mobile': mobile})
        print(dict1)
        if input("Want to enter more? (y/n): ").upper() != 'Y':
            break

        print()
    else:
        print("Enter the correct details.")
        break

print("Final dictionary",dict1)



# 45.Dict1= {“Key”: {“subkey”:20} ,  “k2”:{“sub2” : 5}, “k3” : {“sub4” :16},  “k4” : {“sub4” : 6}}
# Sort elements based on values
# Output must be {,  “k2”:{“sub2” : 5}, “k4” : {“sub4” : 6},  “k3” : {“sub4” : 16}, “Key”:{“subkey”:20}}

def get_marks():
    while True:
        try:
            marks = float(input("Enter marks (0-100): ").strip())
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Enter only numbers (e.g., 75 or 82.5).")

m = get_marks()
print("Saved marks:", m)


# 46.Create a function to calculate age till now.

from datetime import date

year = int(input("Enter birth year: "))
month = int(input("Enter birth month: "))
day = int(input("Enter birth day: "))

dob = date(year, month, day)
today = date.today()

age = today.year - dob.year

if (today.month, today.day) < (dob.month, dob.day):
    age -= 1

print("Age:", age)



# 47.Create a function to check age eligibility for given customer based on DOB. Function will take two input DOB and ELIGIBILITY age.
from datetime import date

def check_eligibility(dob, eligibility_age):
    today = date.today()

    age = today.year - dob.year
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1

    if age >= eligibility_age:
        return "You are eligible"
    else:
        return "You are not eligible"

year = int(input("Enter birth year: "))
month = int(input("Enter birth month: "))
day = int(input("Enter birth day: "))

eligibility = int(input("Enter eligibility age: "))

dob = date(year, month, day)

result = check_eligibility(dob, eligibility)
print(result)






# 48.Create a function to check if string is palindrome or not ? For example, if input is NITIN then reverse of the string 
# is same then it is palindrome. If input is ANIL then reverse is LINA which is not same then it is not palindrome.  
def check_palindrome(str):
    if str.upper() == str[::-1].upper():
        print("Palindrome.")
    else:
        print("Not a palindrome.")

str = input("Enter a str : ")
check_palindrome(str)




# 49.Create a function to generate a Fibonacci Series. 0 1 1 2 3 5 8 13 21 34 …..  upto 100 

def fibonacci_upto_100():
    a = 0
    b = 1

    while a <= 100:
        print(a, end=" ")
        a, b = b, a + b

fibonacci_upto_100()



# 50.Write a code to generate factorial of the number  For example: factorial of 5 = 5! = 5*4*3*2*1
num = int(input("Enter a number: "))
fact = 1

for i in range(1, num+1):
    fact = fact * i

print("Factorial is:", fact)


# 51.Write a program to find largest number in the list.
l = [10, 45, 23, 89, 12]

largest = l[0]

for i in l:
    if i > largest:
        largest = i

print("Largest number is:", largest)




# 52.Write a program to check frequency of each element in the list.
l = [1, 2, 2, 3, 3, 3]

freq = {}

for i in l:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)


# 53.There are two string l1 =[ 1,2,3,4,5] and l2 =[3,2,8,7,9] then write a program to find common elements in the list.
l1 = [1,2,3,4,5]
l2 = [3,2,8,7,9]

common = []

for i in l1:
    if i in l2:
        common.append(i)

print("Common elements:", common)

# Simple print hello
print("hello")







