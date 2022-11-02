'''
Ce programme donne le pourcentage de chance (au centième près) d'avoir un cancer quelconque selon une donnée age et sexe donnée par l'utilisateur.
Les données de pourcentage proviennent de l'institut Cancer Research UK (https://bit.ly/2BOLDsE).
Auteur: The Cancer Team
License = GPL-3
'''
import pandas as pd
while True:
    # url variable represents the dataset that will be used with variables such person's sex & age.
    url = "https://github.com/Makimousse/Cancer/raw/main/Exel_datasheet.xlsx" 
    df = pd.read_excel(url, usecols = 'A:B')

    url2 = "https://github.com/Makimousse/Cancer/raw/main/Country%20canc%20data.xlsx" #second url variable to fetch country-specific cancer percentage rates
    df_country = pd.read_excel(url2, usecols = 'A:B')  # Country-specific dataframe

    sex = input('Please input your sex (H for male, F for female):')
    age = int(input('Please enter your age (between 2 and 90):'))
    
    percentage = str(df[sex].iloc[age]) # Fetches the percentage data from row "sex" and line "age"
    
    print("You have a "+ percentage+"% chance of currently having some type of cancer.")


    if age >= 15:
        sex2 = sex + "_canc" # The rows for the gender-specific cancer survival data are named H_canc and F_canc
        df2 = pd.read_excel(url, usecols = 'C:D') # Second dataframe for the gender-specific cancer data, or else python has a stroke for no reason
        gen_spes_percent = str(df2[sex2].iloc[age]) # Same as "percentage"
        if sex2 == "H_canc":
            print("If you do have some kind of cancer, there is a 25.4% chance that it is prostate cancer. Prostate cancer has a "+gen_spes_percent+"% survival chance ")
            print("over 5 years for your age")
        else:
            print("If you have some kind of cancer, there is a 30% chance that it is breast cancer. Breast cancer has a "+gen_spes_percent+"% survival chance ")
            print("over 5 years for your age")


    coef = float(percentage) / float(df[sex].iloc[49])
    country = input("Would you like to know your chance of having cancer in other countries? If yes, please input the country you'd like to know your rates about, if no, input n:")
    if country == "n":
        break
    else:
        sumting = df_country[df_country['Country'] == country]
        print(sumting)

    again = input("Run the program again? (y for yes, n for no):") #prompt to run the program again
    if again == "n":
        break