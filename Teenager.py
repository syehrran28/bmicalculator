# Checking user's input as "teenager" for age group and determining which class does their BMI index fall into

def function_teenager(compare):
    if compare < 16.5:
        print("\nYou're Underweight") 
    elif 16.5 < compare < 22.9:
        print("\nYou're Normal")
    elif 23.0 < compare < 27.9:
        print("\nYou're Overweight")
    else:
        print("\nYou're Obese")