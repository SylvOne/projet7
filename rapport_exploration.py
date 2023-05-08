import pandas as pd


#Lire les données
data1 = pd.read_csv("data/dataset1_Python+P7.csv")
data2 = pd.read_csv("data/dataset2_Python+P7.csv")
all_data = all_data = pd.concat([data1, data2], ignore_index=True)


# Afficher les statistiques descriptives pour chaque colonne
print(" ")
print("*** Statistiques descriptives ***")
print(data2.describe())

# Compter le nombre de valeurs nulles pour chaque colonne
print(" ")
print("*** Nombre de valeurs nulles pour chaque colonne ***")
print(data2.isnull().sum())

# Afficher la fréquence des valeurs pour une colonne donnée
print(" ")
print("*** Fréquence des valeurs pour une colonne donnée ***")
print(data2['price'].value_counts())
