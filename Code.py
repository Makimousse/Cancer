'''
Ce programme donne le pourcentage de chance (au centième près) d'avoir un cancer quelconque selon une donnée age et sexe donnée par l'utilisateur.
Les données de pourcentage proviennent de l'institut Cancer Research UK (https://bit.ly/2BOLDsE).
Auteur: The Cancer Team
License = GPL-3
'''
import pandas as pd
url = "https://github.com/Makimousse/Cancer/raw/main/Exel_datasheet.xlsx" 
df = pd.read_excel(url, usecols = 'A:B:H:I')
df.head()
sex = input('Please input your sex (H for male, F for female:')
age = int(input('Please enter your age (between 2 and 90):'))
percentage = str(df[sex].iloc[age])



print("You have a "+ percentage+"% chance of having some type of cancer.")

if sex == "H" and age >= 16:
    print("If you do have some kind of cancer, there is a 25.4% chance that it is prostate cancer. Prostate cancer has a x% mortality rate at your age")