import itertools
import time
import pandas as pd


""" 
fonction bruteforce pour rechercher la meilleure combinaison d'actions
en fonction du profit et d'un budget de 500 euros, en testant toutes les possibilités
"""
def brute_force(data):
    # On tri les données pour ne pas tenir compte des prix et profit inférieur ou égale à 0
    data_sorted = data[(data['price'] > 0)]

    combinaisons = []
    for i in range(1, len(data_sorted) + 1):
        for combinaison in itertools.combinations(data_sorted.iterrows(), i):
            combinaisons.append(combinaison)

    meilleure_combinaison = None
    meilleur_profit = 0

    for combinaison in combinaisons:
        total_cost = sum(action[1]['price'] for action in combinaison)
        total_profit = sum(action[1]['price'] * (action[1]['profit'] / 100) for action in combinaison)
        if total_cost <= 50000 and total_profit > meilleur_profit:
            meilleure_combinaison = combinaison
            meilleur_profit = total_profit
    
    return total_cost, total_profit, [action[1]['name'] for action in meilleure_combinaison] if meilleure_combinaison else None



""" 
affiche une combinaison d'actions donnée
"""
def affiche_combinaison(cout_total, profit_total, combinaison):
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
affiche le temps utilisé lors du lancement du programme
"""
def affiche_temps(temps):
    if temps < 1:
        print(" ")
        print("Temps pris par le programme : ", round(temps * 1000, 3), "millisecondes")
        
    else:
        print(" ")
        print("Temps pris par le programme : ", round(temps, 3), "secondes")



""" 
Début du lancement du programme de bruteforce 
"""
# Début de mesure du temps utilisé
print("Veuillez patienter s'il vous plait...")
start_time = time.time()

#lancement de l'algorithme
# Lire les données du fichier CSV
data = pd.read_csv("data/dataset_20_Python+P7.csv", sep=",")

# Utiliser la fonction optimized_combination avec le DataFrame
total_cost, total_profit, combinaison = brute_force(data)

# Fin de mesure du temps utilisé par le code
end_time = time.time()
temps_ecoule = end_time - start_time

affiche_temps(temps_ecoule)
affiche_combinaison(total_cost, total_profit, combinaison)