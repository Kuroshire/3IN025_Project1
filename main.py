import exemple # Pour pouvoir utiliser les methodes de exemple.py

print("bonjour")
maListe=exemple.lectureFichier("PrefEtu.txt") # Execution de la methode lectureFichier du fichier exemple.
prefEtu = exemple.prefEtu(maListe)
print("preferences des etudiants: ", prefEtu)
#print(len(maListe)) #Longueur de la liste.

maListe2=exemple.lectureFichier("PrefSpe.txt") # Execution de la methode lectureFichier du fichier exemple.
prefSpe, capacites = exemple.prefSpe(maListe2)
print("preferences des masters: ", prefSpe)
print("capacites des masters: ", capacites)

print("Affectation des étudiants aux masters: ", exemple.gayle_shapley(prefEtu, prefSpe, capacites))

print("Affectation des étudiants aux masters V2: ", exemple.gayle_shapley2(prefSpe, prefEtu, capacites))

#exemple.createFichierLP(maListe[0][0],int(maListe[1][0])) #Methode int(): transforme la chaine de caracteres en entier
