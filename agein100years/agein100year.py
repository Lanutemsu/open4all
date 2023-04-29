import datetime

def calculate_year_of_100(name, age):
    current_year = datetime.datetime.now().year
    year_of_100 = current_year + (100 - age)
    return year_of_100

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

year_of_100 = calculate_year_of_100(name, age)
age_at_100 = age + (year_of_100 - datetime.datetime.now().year)

print(f"{name}, you will turn 100 in the year {year_of_100}. You will be {age_at_100} years old.")
