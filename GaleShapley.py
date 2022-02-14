""" On considere l'algo de Gale Shapley sur le cas personnes/service:
        personnes = Etudiants
        service = masters (avec un nombre de place maximum)
        On possede:
            -liste des places disponibles dans chaque master
            -les préferences de master de chaque etudiant
            -les preferences des masters sur les etudiants

        Etapes de Gale Shapley coté etudiant:
            -on parcours les etudiants : current student = etu
                -on demande aux maqsters une place dans l'ordre de preference de etu
                2 CAS POSSIBLES:
                    -master est vide / possede encore de la place: ajout auto de etu au master.
                    -master est plein: on regarde la liste des preferences du master
                        2 CAS:
                        -master prefere etu a l'un de ceux dans sa liste: 
                            l'etudiant moins interessant degage et etu le remplace.
                            etu = etudiant remplacé
                            on reprend la boucle pour le nouveau etu
                        -master ne prefere pas etu a ceux dans sa liste:
                            etu passe au master suivant de sa liste.



Representation de data : faire une matrice des preferences du demandeur.
    -lorsque la demande est rejeté ou si il y a un meilleur couple de formé on met un -1 dans la matrice a la position 
    (permet de ne pas boucler sur les demandes car on peut juste skip les -1 et savoir ou on en est)


1/ on recup la matrice des preference
2/ on parcours ligne par ligne


"""

#region imports

import numpy as np

#endregion



"""
Cette fonction sert a lire contenu (liste de chaine de caractere) obtenu par lecture du fichier en donnée representant les préferences des etudiants.
contenu[0] = nombre d'etudiant dans le fichier
contenu[0-n] = matrice des preferences des etudiants

Argument: list<str>, list<str>
return:
    int,int[][] : nombre etudiants, preferences etudiants
"""
def prefEtu(etuPrefs):
    nbEtu = int(etuPrefs[0])
    
    #matrice de int
    prefs = np.zeros()


    return nbEtu

        
    

#region lecture fichier ---------------------------------------------------------------------------------------------------------------------

def lectureFichier(s): # Definition d'une fonction, avec un parametre (s). Ne pas oublier les ":"
    monFichier = open(s, "r") # Ouverture en lecture. Indentation par rapport a la ligne d'avant (<-> bloc).
    contenu = monFichier.readlines() # Contenu contient une liste de chainces de caracteres, chaque chaine correspond a une ligne       
    monFichier.close() #Fermeture du fichier
    	#print(contenu[i])
    	#print("blblb")
    	#contenu[i].pop(0)
    	#contenu[i].pop(1)
    return contenu
    # Commandes utiles:
    # n=int(s) transforme la chaine s en entier.
    # s=str(n) l'inverse
    # Quelques methodes sur les listes:
    # l.append(t) ajoute t a la fin de la liste l
    # l.index(t) renvoie la position de t dans l (s'assurer que t est dans l)
    # for s in l: s vaut successivement chacun des elements de l (pas les indices, les elements)
			

def createFichierLP(nomFichier,nombreVariables):
    monFichier=open(nomFichier,"w") #Ouverture en ecriture. Le fichier est ecrase s'il existe, cree s'il n'existe pas
    monFichier.write("Maximize\n")
    for i in range(0,nombreVariables): #Boucle i variant de 0 a NombreVariables-1
        monFichier.write("x"+str(i)+" ") #write pour ecrire. Indentation
        if (i<nombreVariables-1): # Syntaxe d'un test. 'and' et 'or' dans les expressions logique
            monFichier.write("+ ")
        else:
            monFichier.write("\n")
    monFichier.write("st\n") # Fin de l'indentation -> fin de la boucle
    monFichier.write("Binary\n")
    for i in range(0,nombreVariables):
        monFichier.write("x"+str(i)+" ")
    monFichier.write("\n")
    monFichier.write("end")
    monFichier.close()


#endregion -----------------------------------------------------------------------------------------------------------------------------------