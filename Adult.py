# Checking user's input as "adult" for age group and determining which class does their BMI index fall into

def function_adult(compare):
    if compare < 18.5:
        print("\nYou're Underweight") 
    elif 18.5 < compare < 24.9:
        print("\nYou're Normal")
    elif 25.0 < compare < 29.9:
        print("\nYou're Overweight")
    elif 30.0 < compare < 34.9:
        print("\nYou're Obese (Class I)")
    elif 35.0 < compare < 39.9:
        print("\nYou're Obese (Class II)")
    else:
        print("\nYou're Obese (Class III)")