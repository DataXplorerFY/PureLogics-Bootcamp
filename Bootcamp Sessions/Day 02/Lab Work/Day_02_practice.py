#Step 01, Variables and Data types

#create a variables to store your name, age, height, and a boolean variable 

name = "Farhan"
age = 25
height = 5.9
is_student = False


#Print the variables to the console
print("Name:", name)
print("Type of name variable is:", type(name))
print("******************************")

print("Age:", age)
print("Type of age variable is", type(age))
print("******************************")

print("Height:", height)
print("Type of height bariable is", type(height))
print("******************************") 

print("is_student:", is_student)
print("Type of is_student variable is", type(is_student))
print("******************************") 


#Step 2: Conditional Statements
#Write a simple program to evaluate a student's grade.

# TODO: Ask user to enter a score (0-100) and print the grade
# Hint: Use if-elif-else ladder

user_score = int(input("Enter your Score (0-100):"))

if user_score >= 90 and user_score <=100:
    print("Your grade is A+")

elif user_score >= 80 and user_score < 90:
    print("Your grade is A")

elif user_score >= 70 and user_score <80:
    print("your grade is B")

elif user_score >= 60 and user_score <70:
    print("your garde is C")

elif user_score >= 50 and user_score <60:
    print("your grade is D")

elif user_score >= 40 and user_score <50:
    print("your grade is E")                        

else:
    print("your grade is F")
    print("You have failed the exam")
