'''
This currently program indicates the user with it's chances of currently having cancer depending on his age, sex and country.
The age and sex specific data is from the UK Cancer institute (https://bit.ly/2BOLDsE), and the country-specific data is from from the 2018 GLOBOCAN statistics survey (https://bit.ly/3DCvLrI).
Author: The Cancer Team
License = GPL-3
'''
import pandas as pd
while True:

# This first part will indicate the basic chance of aving any type of cancer depending on one's age and sex

    url = "https://github.com/Makimousse/Cancer/raw/main/Datasheet1-sex%26age.xlsx" # Url variable represents the dataset that will be used to fetch the data from a person's age and sex.
    df = pd.read_excel(url, usecols = 'A:B') # First dataframe that looks at the sex columns of the excel book

    sex = input('Please input your sex (H for male, F for female):')
    age = int(input('Please enter your age (between 2 and 90):'))
    
    percentage = df[sex].iloc[age] # Fetches the percentage data from row "sex" and line "age"
    percentage  = '%.4f' % round(percentage, 4) # Rounds the result to 4 digits after decimal point

    print("You have a "+ percentage+"% chance of currently having some type of cancer.")

# This next part will indicate the chances of having prostate/breast cancer related to age and sex if the user is aged 15 or older

    if age >= 15:
        sex2 = sex + "_canc" # The rows for the gender-specific cancer survival data are named H_canc and F_canc, so it is important to rename the sex
        df_sex = pd.read_excel(url, usecols = 'C:D') # Second dataframe for the gender-specific cancer data, or else python has a stroke for no reason
        gen_spes_percent = str(df_sex[sex2].iloc[age]) # Same as "percentage", but for the second dataframe
        if sex2 == "H_canc":
            print("If you do have some kind of cancer, there is a 25.4% chance that it is prostate cancer. Prostate cancer has a "+gen_spes_percent+"% survival chance over 5 years for your age")
        else:
            print("If you have some kind of cancer, there is a 30% chance that it is breast cancer. Breast cancer has a "+gen_spes_percent+"% survival chance over 5 years for your age")


#This next part will ask the user if they would like to know their chances of having any type of cancer in other 1rst world countries

    url2 = "https://github.com/Makimousse/Cancer/raw/main/Datasheet2-country.xlsx" # Second url variable to fetch country-specific cancer percentage rates. I use a different excel sheet to not confuse the two
    df_country = pd.read_excel(url2, usecols = 'A:B')  # Country-specific dataframe

    coef = float(percentage) / float(df[sex].iloc[49]) # Finds the coefficient to determine how chances of having cancer are affected by age, the data from the second excel book is somewhat based on an age of 49 for both men and women, so it is used as the reference point here. This coefficient is necessary since the second excel book doesnt indicate sex and age
    country = input("Would you like to know your chance of having cancer in other countries? If yes, please input the country's name, if no, input 'n':") # Asks the user if they would like to know their chances of having cancer in other countries. This country input will be used throughout the code
    if country != "n":
        row_find = df_country[df_country['Country'] == country].index.to_list() # This locates the row of the country in the excel book and indexes it to a list (the code doesnt work otherwise, not sure why)
        country_rates = [df_country['Rates'].iloc[row_find]] # Fetches the country-specific rates from the excel sheet with the row_find variable found earlier
        country_spes_percent = coef * country_rates[0] # Gets the final country, age and sex specific cancer chances 
        country_spes_percent  = '%.4f' % round(country_spes_percent, 4) # Rounds the percentage to 4 digits after the decimal point 
        print("If you were in "+country+", you'd have a "+country_spes_percent+"% chance of having some type of cancer")

    again = input("Run the program again? (y for yes, n for no):") #prompt to run the program again
    if again == "n":
        break