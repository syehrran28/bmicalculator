# Checking user's input as "child" for age group and determining which class does their BMI index fall into

def function_child(compare):
    if compare < 18.5:
        print("\nYou're Underweight") 
    elif 18.5 < compare < 22.9:
        print("\nYou're Normal")
    elif 23.0 < compare < 24.9:
        print("\nYou're Overweight (At Risk")
    elif 25.0 < compare < 29.9:
        print("\nYou're Overweight (Moderately Obese)")
    else:
        print("\nYou're Overweight (Severely Obese)")
