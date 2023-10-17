import matplotlib.pyplot as plt
import csv
from Bmi_calculation import *
from Child import *
from Teenager import *
from Adult import *
from Average import *

# Array lists of bmi index, name, gender, age group, adult, teenager, and child
bmi_index_list = []
name_list = []
gender_list = []
weight_list = []
height_list = []
age_group_list = []
Adult_list = []
Teenager_list = []
Child_list = []

print("**************************WELCOME TO THE BMI INDEX CALCULATOR**************************")

entries = int(input("Enter Number Of People: "))

# while loop is used to loop the following variables based on the number entries user has input.
count = 0
while count < entries :
    
    name = input(str("Please enter your name: ")).upper()
    gender = input(str("Please enter your gender [MALE/FEMALE]: ")).upper()
    weight = eval(input("Please enter your weight in KG: "))
    height = eval(input("Please enter your height in cm: "))
    
    while True:
        age_group = input("Please enter your age group [Child = 1, Teenager = 2, Adult = 3]: ")
    
        if age_group == "1":
            bmi = calculate_bmi(weight, height)
            function_child(bmi)
            Child_list.append(bmi)
            break
        
        elif age_group == "2":
            bmi = calculate_bmi(weight, height)
            function_teenager(bmi)
            Teenager_list.append(bmi)
            break
        
        elif age_group == "3":
            bmi = calculate_bmi(weight, height)
            function_adult(bmi)
            Adult_list.append(bmi)
            break
        
        else:
            print("Choose the right age group")
            continue
        
# User's input of name, gender , age group and calculated Bmi index is appended into respective array lists.
    bmi_index_list.append(bmi)
    name_list.append(name)
    gender_list.append(gender)
    weight_list.append(weight)
    height_list.append(height)
    age_group_list.append(age_group)
    
    
    print("Your BMI is: ",bmi)
    print()
    
    count = count + 1
# Prints the average BMI index of each age group based on the user's input.
child_average_bmi = average_bmi(Child_list)
teenager_average_bmi = average_bmi(Teenager_list)
adult_average_bmi = average_bmi(Adult_list)
print("Average BMI Index For Child Age Group is: ", average_bmi(Child_list))
print("Average BMI Index For Teenager Age Group is: ", average_bmi(Teenager_list))
print("Average BMI Index For Adult Age Group is: ", average_bmi(Adult_list))

print("\n**************************Thank You For Your Participation**************************")

print("\n**********************************Data Recorded**********************************")

# Write and append data from name list, age group lists and BMI index list into csv file
with open("records.txt", "a" ,newline='') as fp:
    fp.seek(2,0)
    for i in range(len(name_list)):
        fp.write(f"{name_list[i]}, {gender_list[i]}, {weight_list[i]}, {height_list[i]}, {age_group_list[i]}, {bmi_index_list[i]} \n")
# Read the csv file
with open("records.txt", "r") as fp:
    for row in fp:
        print(row)
        
# Plotting a graph of Average BMI by Age Group
x = ["Child","Teenager","Adult"]
y = [child_average_bmi,teenager_average_bmi,adult_average_bmi]
colours = ['red', 'green', 'blue']

for i in range(len(x)):
    plt.bar(x[i], y[i], color = colours[i])
    
plt.title("Average BMI by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Average BMI")
plt.show()
    






