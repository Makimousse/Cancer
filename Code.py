"""
The program currently indicates the user with it's chances of having cancer depending on his age, sex and country.
The age and sex specific data is from the UK Cancer institute (https://bit.ly/2BOLDsE), and the country-specific data is from from the 2018 GLOBOCAN statistics survey (https://bit.ly/3DCvLrI).
This program is NOT about accuracy of the data (although we're constantly trying to make it more accurate), it is just a high-school assignement, please don't bully us.
Author: ''' adad '''
License = GPL-3
"""
import pandas as pd
from googletrans import Translator

url = "https://github.com/Makimousse/Cancer/raw/main/Datasheet1-sex%26age.xlsx" # Url variable represents the dataset that will be used to fetch the data from a person's age and sex.
df = pd.read_excel(url, usecols = 'A:B') # First dataframe that looks at the sex columns of the excel book
df_sex = pd.read_excel(url, usecols = 'C:D') # Second dataframe for the gender-specific cancer data, or else python has a stroke for no reason

url2 = "https://github.com/Makimousse/Cancer/raw/main/Datasheet2-country.xlsx" # Second url variable to fetch country-specific cancer percentage rates. I use a different excel sheet to not confuse the two
df_country = pd.read_excel(url2, usecols = 'A:B')  # Country-specific dataframe

# On all of these funcitons, when the "return" statement is used, the code simply associates the function with the values

def input_sex(): # This function will ask the user for his sex and check if the sex is correct with a bool
    sex = input('Please input your sex (M for male, F for female):')
    sex_check_list= sex in ['F','M'] # This list contains the valid sex inputs, the code will check if the input is in the list and return a bool
    return sex, sex_check_list

def input_age(): #This function asks the user for his age, it also manages non-integer inputs with a "try" and "except"
    while True: #The while True is used to repeat the loop
        try: # If this line poses no errors, the loop breaks and everyone is happy, the try and except are used to check if the input is an integer
            age = int(input('Please enter your age (between 2 and 90):'))
            break 
        except: # If there is an error, it will restart the function
            input_age()
    return age
def age_check(age): # This function creates a bool to check if the age is in the correct range
    age_list = [*range(2, 90)]
    age_range_check = age in age_list
    return age_range_check

def input_country(): # This function asks for the user's country
    country = input("Would you like to know your chance of having cancer in other countries? If yes, please input the country's name, if no, input 'n':") # Asks the user if they would like to know their chances of having cancer in other countries. This country input will be used throughout the code
    return country
def country_check(country): # This function creates a bool to check if the country is part of the second excel book's
    country_list_file = open('Country_list.txt', 'r') # Instead of writing in the code a long list of countries, we here fetch this list from an external file
    file_contents = country_list_file.read() # This interprets the contents of the external file
    country_list_check = country in file_contents
    return country_list_check




def base_percentage(sex,age): # Function gives the user his basic chance of having any type of cancer
    percentage = df[sex].iloc[int(age)] # Fetches the percentage data from row "sex" and line "age"
    round_percentage  = '%.4f' % round(percentage, 4) # Rounds the result to 4 digits after decimal point
    return round_percentage, percentage
            
def gen_spes(sex, age): # Finds the user's survival chances for gender-specific cancers (breast/prostate)
    sex2 = sex + "_canc" # The rows for the gender-specific cancer survival data are named H_canc and F_canc, so it is important to rename the sex variable
    
    gen_spes_percent = str(df_sex[sex2].iloc[age]) # Same as "percentage", but for the second dataframe
    return gen_spes_percent, sex2
    
def country_percent(sex,country, percentage): # Finds the user's chances of having cancer in otehr countries
    coef = float(percentage) / float(df[sex].iloc[49]) # Finds the coefficient to determine how chances of having cancer are affected by age, the data from the second excel book is somewhat based on an age of 49 for both men and women, so it is used as the reference point here. This coefficient is necessary since the second excel book doesnt indicate sex and age
    row_find = df_country[df_country['Country'] == country].index.to_list() # This locates the row of the country in the excel book and indexes it to a list (the code doesnt work otherwise, not sure why)

    country_rates = [df_country['Rates'].iloc[row_find]] # Fetches the country-specific rates from the excel sheet with the row_find variable found earlier
    country_spes_percent = coef * country_rates[0] # Gets the final country, age and sex specific cancer chances 
    country_spes_percent  = '%.4f' % round(country_spes_percent, 4) # Rounds the percentage to 4 digits after the decimal point 
    return country_spes_percent

def try_again(): # This function will ask the user if they would like to restart the program
    try_prompt = input("Would you like to run the program again? Input anything if yes, input 'n' if no:")
    if try_prompt != "n":
        main()

def main(): #The main is the 'mother function' and will generate all printed code
    # All lines of code with 'variable' = 'function()' simply gather the returned data for these respective functions

    # This first "Big section" of the main will cover inputs and will manage errors for them:
    # These all function on the same principle: the functions asign a bool with the variable (True if the variable is good, False if not), and these lines of code will force the user to try again if the input is invalid
    sex, sex_check_list = input_sex() 
    while sex_check_list == False:  #This first "paragraph" is dedicated for the sex inputs and filtering invalid inputs
        sex, sex_check_list = input_sex()

    age = input_age()
    age_range_check = age_check(age)
    while age_range_check == False:      # This other one is dedicated for age inputs
        age = input_age()           
        age_range_check = age_check(age)

    country = input_country()     
    country_list_check = country_check(country)
    while country_list_check == False:      # And this one for country inputs
        country = input_country()    
        country_list_check = country_check(country)


    # This second big secion takes care of percentage data and printing them:
    round_percentage, percentage = base_percentage(sex,age) 
    print("You have a "+ str(round_percentage)+"% chance of currently having some type of cancer.")

    if age >= 15: 
        gen_spes_percent, sex2 = gen_spes(sex,age) 
        if sex2 == "M_canc": # Simply chooses what kind of gender-specific cancer survival rate to print out
            print("If you do have some kind of cancer, there is a 25.4% chance that it is prostate cancer. Prostate cancer has a "+gen_spes_percent+"% survival chance over 5 years for your age")
        else:
            print("If you have some kind of cancer, there is a 30% chance that it is breast cancer. Breast cancer has a "+gen_spes_percent+"% survival chance over 5 years for your age")
    
    if country != "n": # Checks if the user wants his country-specific rates
        country_spes_percent = country_percent(sex,country,percentage)
        print("If you were in "+country+", you'd have a "+country_spes_percent+"% chance of having some type of cancer")

    try_again() # This simply runs the try_again function at the end of the main
    
    
main()

'''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than right now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
—Tim Peters'''

'''When I wrote this code, only God and I understood what I did. Now only God knows'''