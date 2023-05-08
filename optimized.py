import time
import pandas as pd


""" 
Fonction utilisant un algorithme optimisé, appelé méthode du 'Sac à dos' 
afin de trouver la meilleure combinaison d'actions possible 
en fonction du profit total et du budget de 500 euros.
"""
def optimized_combination(data: pd.DataFrame):

    budget_portefeuille = 500

    matrice = [[0 for x in range(budget_portefeuille * 100 + 1)] for x in range(len(data) + 1)]

    for i in range(1, len(data) + 1):
        price = data.iloc[i - 1]['price'] * 100
        profit = price * data.iloc[i - 1]['profit'] / 100
        for w in range(1, budget_portefeuille * 100 + 1):
            try:
                if i == 0 or w == 0:
                    matrice[i][w] = 0
                elif price <= w:
                    matrice[i][w] = max(
                        profit + matrice[i - 1][int(w - price)], matrice[i - 1][w]
                    )
                else:
                    matrice[i][w] = matrice[i - 1][w]
            except Exception:
                matrice[i][w] = matrice[i - 1][w]
                continue

    n = len(data)
    liste_actions_combinaisons = []
    cout = 0
    budget = 500 * 100

    while n > 0 and budget > 0:
        action = data.iloc[n - 1]
        price = action['price'] * 100
        profit = price * action['profit'] / 100
        if (
            matrice[n][budget] == matrice[n - 1][int(budget - price)] + profit
            and price > 0
        ):
            cout += action['price']
            liste_actions_combinaisons.append(action['name'])
            budget -= int(price)
        n -= 1

    meilleur_profit = round(matrice[-1][-1] / 100, 2)
    cout = round(cout, 1)
    return cout, meilleur_profit, liste_actions_combinaisons



""" 
    Affiche le temps utilisé lors du lancement du programme 
"""
def affiche_temps(temps):
    if temps < 1:
        print(" ")
        print("Temps pris par le programme : ", round(temps * 1000, 3), "millisecondes")
        
    else:
        print(" ")
        print("Temps pris par le programme : ", round(temps, 3), "secondes")



"""
    Il s'agit tout simplement d'une vue pour afficher la combinaison dans le terminal 
"""
def affiche_combinaison(combinaison, cout_total, profit_total):
    if combinaison:
        print(" ")
        print("Meilleure combinaison d'actions :")
        for action in combinaison:
            print(action)
        print(f"Coût total : {cout_total} euros")
        print(f"Bénéfice total : {profit_total} euros")
    else:
        print(" ")
        print("Aucune combinaison.")


""" 
    Début du lancement du programme de optimisé 
"""
print("Veuillez patienter s'il vous plait...")
# Début de mesure du temps utilisé et d'analyse mémoire du code
start_time = time.time()

#lancement de l'algorithme
# Lire les données du fichier CSV
#data = pd.read_csv("data/dataset1_Python+P7.csv", sep=",")
data = pd.read_csv("data/dataset2_Python+P7.csv", sep=",")
#data = pd.read_csv("data/dataset_20_Python+P7.csv", sep=",")


# Utiliser la fonction optimized_combination avec le DataFrame
total_cost, total_profit, selected_actions = optimized_combination(data)

# Fin de mesure du temps utilisé par le code
end_time = time.time()
temps_ecoule = end_time - start_time
affiche_temps(temps_ecoule)

# Afficher la meilleure combinaison
affiche_combinaison(selected_actions, total_cost, total_profit)