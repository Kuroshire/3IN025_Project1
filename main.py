#import exemple # Pour pouvoir utiliser les methodes de exemple.py
import GaleShapley

print("bonjour")
maListe = GaleShapley.lectureFichier("PrefEtu.txt") # Execution de la methode lectureFichier du fichier exemple.
prefEtu = GaleShapley.prefEtu(maListe)
print("preferences des etudiants: \n", prefEtu)
#print(len(maListe)) #Longueur de la liste.


maListe2=GaleShapley.lectureFichier("PrefSpe.txt") # Execution de la methode lectureFichier du fichier exemple.
prefSpe, capacites = GaleShapley.prefSpe(maListe2)
print("preferences des masters: \n", prefSpe)
print("capacites des masters: \n", capacites)

"""
print("Affectation des étudiants aux masters: ", GaleShapley.gayle_shapley(prefEtu, prefSpe, capacites))

print("Affectation des étudiants aux masters V2: ", GaleShapley.gayle_shapley2(prefSpe, prefEtu, capacites))

#exemple.createFichierLP(maListe[0][0],int(maListe[1][0])) #Methode int(): transforme la chaine de caracteres en entier
"""