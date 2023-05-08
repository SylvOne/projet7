# Résolvez des problèmes en utilisant des algorithmes en Python

## Scénario

Dans ce projet, je travaille dans une société d'investissement AlgoInvest&Trade, il s'agit
d'une société financière spécialisée dans l'investissement. La société cherche à optimiser
ses stratégies d'investissement à l'aide d'algorithmes, afin de dégager davantage de bénéfices pour ses clients.
On me demande alors, de réaliser un algorithme dont le but sera de suggérer une liste des actions les plus rentables
pour maximiser le profit d'un client au bout de deux ans.

Pour cela le projet se décompose en 3 parties :

+ 1ère partie : Concevoir un algorithme type brute force.
+ 2ème partie : Optimiser cet algorithme pour qu'il soit plus rapide tout en restant efficace.
+ 3ème partie : Tester cet algorithme optimisé sur un ensemble de données plus important.

### Concevoir un algorithme type brute force

Cet algorithme appelé "brute force" à la particularité de tester toutes les combinaisons possibles. Il a l'avantage de donner à coup sûr la meilleure solution mais il a une complexité temporelle exponentielle : O(2^n). Il sera difficile de le mettre en pratique dans la réalité, notamment avec un ensemble de données important.

### Optimiser cet algorithme pour qu'il soit plus rapide tout en restant efficace

Ici une version optimisé de l'algorithme sera implémentée. Cette version utilisera ma méthode dite du "sac à dos".
Cet algorithme, ne va pas tester toutes les combinaisons possibles, il utilisera une approche de programmation dynamique
pour résoudre le problème de manière efficace. Il sera donc plus rapide à l'execution. Sa complexité temporelle est de l'ordre de O(nW),
cependant dans ce projet W étant constant, cela ramènera la complexité temporelle à O(n) qui est une complexité linéaire.

## Installation

1. Clonez le dépôt avec `git clone https://github.com/SylvOne/projet7.git`.
2. Naviguez jusqu'au dossier du programme avec `cd projet7`.
3. Créez un environnement virtuel avec `python -m venv venv` sur Windows ou `python3 -m venv venv` sur Linux/Mac
4. Activez l'environnement virtuel avec `source venv/bin/activate`
sur Linux/Mac ou `.\venv\scripts\activate` sur Windows.
5. Installez les dépendances avec `pip install -r requirements.txt`.

## Utilisation

(Avant de lancer les commandes assurez-vous d'avoir activé l'environnement virtuel)
- Lancez l'algorithme brute force  avec `python bruteforce.py`.
- Lancez l'algorithme optimisé avec `python optimized.py`.
vous pouvez modifier l'ensemble des données d'entrée en ouvrant le fichier `optimized.py`
et en commentant décommentant la ligne 96 - 97 ou 98.