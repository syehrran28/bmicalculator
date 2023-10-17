import math 
# Calculating the average BMI index for each age group using the array lists of each age group
# If else is used to avoid error when sum of index is divide by 0 and return the average bmi as 0
def average_bmi(index):
    if len(index) == 0 :
        return 0
    else:
        average = math.fsum(index) / len(index)
        return average