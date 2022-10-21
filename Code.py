'''
Ce programme donne le pourcentage de chance (au centième près) d'avoir un cancer quelconque selon une donnée age et sexe donnée par l'utilisateur.
Les données de pourcentage proviennent de l'institut Cancer Research UK (https://bit.ly/2BOLDsE).
Auteur: Hugo Chanet-Leyne et Martin-Charles Bartosik
License = GPL-3
'''
import pandas as pd
workbook = pd.read_excel(r'/Users/Hugo/Desktop/School/PREMIERE/TECH/OCTOBRE/Vacation Proj/Exel_datasheet.xlsx', usecols = 'A:B')
workbook.head()
sex = input('Please input your sex (H for male, F for female:')
age = int(input('Please enter your age (between 2 and 90):'))
percentage = str(workbook[sex].iloc[age])

print("You have a "+ percentage+"% chance of having some type of cancer")