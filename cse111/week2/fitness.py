# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime
import math

def main():
    # Get the user's gender, birthdate, height, and weight.

    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.

    # Print the results for the user to see.
    print("Please enter your gender (M or F):",end=" ")
    gender = str(input(""))
    
    print("Enter your birthdate (YYYY-MM-DD):", end=" ")
    birth_date = input("")
    
    print("Enter your weight in U.S. pounds:",end=" ")
    weight = float(input(""))
    
    print("Enter your height in U.S. inches:",end=" ")
    height = float(input(""))
    
    if gender.lower() == "m":
        age_result = compute_age(birth_str=birth_date)
        weight_result = kg_from_lb(pounds=weight)
        height_result = cm_from_in(inches=height)
        bmi_result = body_mass_index(weight=weight_result, height=height_result)
        bmr_result = basal_metabolic_rate(gender="m", weight=weight_result, height=height_result, age=age_result)
        
        print("Age (Years): {}".format(age_result))
        print("Weight (kg): {:.2f}".format(weight_result))
        print("Height (cm): {:.1f}".format(height_result))
        print("Body mass index: {}".format(round(bmi_result, 1)))
        print("Basal metabolic rate (kcal/day): {:.0f}".format(bmr_result))
        
    else:
        if gender.lower() == "f":
            age_result = compute_age(birth_str=birth_date)
            weight_result = kg_from_lb(pounds=weight)
            height_result = cm_from_in(inches=height)
            bmi_result = body_mass_index(weight=weight_result, height=height_result)
            bmr_result = basal_metabolic_rate(gender="f", weight=weight_result, height=height_result, age=age_result)
            
            print("Age (Years): {}".format(age_result))
            print("Weight (kg): {:.2f}".format(weight_result))
            print("Height (cm): {:.1f}".format(height_result))
            print("Body mass index: {:.1f}".format(bmi_result))
            print("Basal metabolic rate (kcal/day): {:.0f}".format(bmr_result))
            
    pass


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    conversion = pounds * 0.45359237
    return conversion


def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    conversion = inches * 2.54 
    return conversion


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    result = weight * 10000
    bmi = result / height ** 2
    
    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    if gender.lower() == "m":
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    else:
        if gender.lower() == "f":
            bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    return bmr


# Call the main function so that
# this program will start executing.

main()