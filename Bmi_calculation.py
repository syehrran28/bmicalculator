# Calculating the BMI index which is rounded to two decimal places based on the user's weight and height
def calculate_bmi(weight, height):
    bmi = eval('weight / ((height/100) ** 2)')
    rounded_bmi = round(bmi,2)
    return rounded_bmi
