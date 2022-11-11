# created on 25th October, 2022

import random
from surnames import surnames 
from females_firstnames import females_firstnames
from males_firstnames import males_firstnames
from months import months

male_name = random.choice(males_firstnames)
female_name = random.choice(females_firstnames)
last_name = random.choice(surnames)
# birth_year = random.randint(1, 2021)
birth_year = random.randint(1970, 2003)
# I made it between 1970 and 2003 so i would get ages with that specific range
current_year = 2022
age = current_year - birth_year
birth_month = random.choice(months)
birth_day = random.randint(1,31)
# I havent factored in leap years and I am assumming all months have 31 days

print("What is your Gender?")
user_gender = input('Are you a Male or Female?: ')
opt1 = ['male', 'Male', 'MALE']
opt2 = ['female', 'Female', 'FEMALE']

# I made opt1 and opt 2 because thats the only one that worked out. 
# if I did if user_gender == Male, it didnt work correctly
# making the list just made things easier and I havent had any issues with it

# Im going to define a function that will get a valid year of birth
# It is not logical to have someone born in the 80's still alive in this year
# I had issues with the function so i took it out
'''
def valid_year():
    if current_year - birth_year > 75:
        birth_year = random.randint(1, 2021)
    elif current_year - birth_year < 20:
        birth_year = random.randint(1, 2021)
    else:
        return birth_year
'''
        
def rnd_id():
    if user_gender in opt1:
        print("This is your random male ID")
        print("Your first name is: {}".format(male_name))
        print("")
        print("Your last name is: {} ".format(last_name))
        print('')
        print("Your age is: {}".format(age))
        print('')
        print('Your year of birth is: {}'.format(birth_year))
        print('')
        print('Your month of birth is: {}'.format(birth_month))
        print('')
        print('Your day of birth is: {}'.format(birth_day))
    elif user_gender in opt2:
        print('This will be your random female ID')
        print("Your first name is: {}".format(female_name))
        print('')
        print("Your last name is: {}".format(last_name))
        print('')
        print("Your age is: {}".format(age))
        print('')
        print('Your year of birth is: {}'.format(birth_year))
        print('')
        print('Your month of birth is: {}'.format(birth_month))
        print('')
        print('Your day of birth is: {}'.format(birth_day))
    else:
        print('Invalid answer. Please try again')
rnd_id()

