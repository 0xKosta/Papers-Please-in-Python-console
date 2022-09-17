##MADE BY Buxx0-github.com/Buxx0###
###################################
###____####################___#####
##|  _ \                  / _ \ ###
##| |_) |_   ___  ____  _| | | |###
##|  _ <| | | \ \/ /\ \/ / | | |###
##| |_) | |_| |>  <  >  <| |_| |###
##|____/ \__,_/_/\_\/_/\_\\___/####
###################################
###################################

import random
import time
import os


def choose_discrepency(discrepency_present):
    '''This function lets you choose which data to verify.'''
    possible_choices_1 = ["Y", "N"]
    possible_choices_2 = ["NAME", "GENDER", "DOB", "EXP", "EXIT"]
    discrepency_choice = input("Do you want to check for discrepencies? [Y/N]").upper()
    while discrepency_choice not in possible_choices_1:
        discrepency_choice = input("Incorrect input, choose Y (yes) or N (no).").upper()
    if discrepency_choice == "Y":
        print("Type exit to exit the discrepency menu.")
        parameter = input("Which parameter would you like to check? [NAME/GENDER/DOB/EXP].").upper()
        while parameter != "EXIT":
            while parameter not in possible_choices_2:
                parameter = input("Incorrect input, choose NAME, GENDER, DOB or EXP.").upper()
            if parameter == "EXP":
                if discrepency_present == True:
                    print("!!! Discrepency detected! The document provided is expired. !!!")
                else:
                    print("Matching data.")
            elif parameter == "EXIT":
                return None
            else:
                print("Matching data.")
            print("Type exit to exit the discrepency menu.")
            parameter = input("Which parameter would you like to check? [NAME/GENDER/DOB/EXP].").upper()



def check_discrepency(person, date):
    '''This function checks if there are any discrepencies present.'''
    if date[2] > person["expire"][2]:
        print("year bad")
        return True
    if date[2] == person["expire"][2]:
        if date[1] > person["expire"][1]:
            return True
        if date[1] == person["expire"][1]:
            if date[0] > person["expire"][0]:
                return True
    return False


def clear():
    os.system('cls')
    os.system('clear')

def passport_display(data):
    '''This function displays the passport of a person.'''
    dateofbirth = str(data['dob'][0]) + "/" + str(data['dob'][1]) + "/" + str(data['dob'][2])
    expirydate = str(data['expire'][0]) + "/" + str(data['expire'][1]) + "/" + str(data['expire'][2])
    print('''---------------------------------------------------------
        &@@@@@@@@.        |
       @@@@@@@@@@@(       |
       @@@@@@@@@@@@       | NAME: {}
       @@@@@@@@@@@@       | GENDER: {}
        @@@@@@@@@         | DATE OF BIRTH: {}
          @@@@@@          | EXPIRY DATE: {}
          @@@@@@          |
    @@@@@@@@@@@@@@@@@@    |
 @@@@@@@@@@@@@@@@@@@@@@@@ |
 ---------------------------------------------------------'''.format(data["name"], data["gender"], dateofbirth,expirydate))

def expire_date():
    '''Generates a random expiry date.'''
    month_length = {1: 31, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    year = random.randint(1981, 1988)
    month = random.randint(1, 12)
    if year % 4 == 0:
        if year % 100 != 0:
            if month == 2:
                day = random.randint(1, 29)
            else:
                day = random.randint(1, month_length[month])
        elif year % 100 == 0:
            if year % 400 == 0:
                if month == 2:
                    day = random.randint(1, 29)
                else:
                    day = random.randint(1, month_length[month])
    else:
        if month == 2:
            day = random.randint(1, 28)
        else:
            day = random.randint(1, month_length[month])
    return (day, month, year)


def choose_gender():
    '''Generates random gender.'''
    gender = random.randint(0,1)
    if gender == 0:
        return "F"
    elif gender == 1:
        return "M"

def choose_birthdate():
    '''Generates a random birthdate for a person that is from 18 to 62 years old in the games time (1982).'''
    month_length = {1 : 31, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}
    year = random.randint(1920, 1964)
    month = random.randint(1, 12)
    if year % 4 == 0:
        if year % 100 != 0:
            if month == 2:
                day = random.randint(1, 29)
            else:
                day = random.randint(1, month_length[month])
        elif year % 100 == 0:
            if year % 400 == 0:
                if month == 2:
                    day = random.randint(1, 29)
                else:
                    day = random.randint(1, month_length[month])
    else:
        if month == 2:
            day = random.randint(1, 28)
        else:
            day = random.randint(1, month_length[month])
    return (day, month, year)

def choose_name_female():
    '''Chooses a random female name from the list.'''
    file = open(file = "femalefirstnames.txt")
    content = file.readlines()
    name = content[random.randint(0,1430)]
    name =  name[0:len(name) - 1]
    return name.upper()

def choose_name_male():
    '''Chooses a random male name from the list.'''
    file = open(file="malefirstnames.txt")
    content = file.readlines()
    name = content[random.randint(0,4592)]
    name = name[0:len(name) - 1]
    return name.upper()

def choose_last_name():
    '''Chooses a random last name from the list.'''
    file = open(file="surnames.txt")
    content = file.readlines()
    surname = content[random.randint(0, 99386)]
    surname = surname[0:len(surname) - 1]
    return surname.upper()

def choose_full_name_gender():
    '''This function uses three functions (choose_gender, choose_name_female, choose_name_male and choose_last_name)
    and compiles them to form a full name with a specified gender.'''
    gender = choose_gender()
    if gender == "F":
        first_name = choose_name_female()
    elif gender == "M":
        first_name = choose_name_male()
    last_name = choose_last_name()
    full_name = first_name + " " + last_name
    return (full_name, gender)

def generate_person():
    '''Combines every generation function to create a person's passport.'''
    name, gender = choose_full_name_gender()
    dob = choose_birthdate()
    weight = random.randint(57, 93)
    height = random.randint(160, 195)
    expire = expire_date()
    return {"name" : name, "gender" : gender, "dob" : dob, "weight" : weight, "height" : height,"expire" : expire}

def approve_deny(discrepency_present):
    '''This function handles approval and denial of a person's entry.'''
    possible_choices = ["APPROVE", "DENY"]
    approve = input("Do you want to [APPROVE] or [DENY] entry to this person?").upper()
    while approve not in possible_choices:
        approve = input("Incorrect input, please choose APPROVE or DENY.").upper()
    if approve == "APPROVE":
        print("You have approved entry to the person.")
        if discrepency_present:
            print("You have gotten a citation! There was a discrepency present!")
    elif approve == "DENY":
        print("You have denied entry to the person.")
        if not discrepency_present:
            print("You have gotten a citation! No discrepencies were present!")


def play():
    '''Main function.'''
    todaysdate = (10,11,1982)
    count = 0
    while count != -1:
        person = generate_person()
        passport_display(person)
        print("Today's date is: {}/{}/{}".format(todaysdate[0],todaysdate[1],todaysdate[2]))
        discrepency_present = check_discrepency(person, todaysdate)
        choose_discrepency(discrepency_present)
        approve_deny(discrepency_present)
        input("Press enter to call in the next person.")
        clear()
        count += 1


play()
