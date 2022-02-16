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
contenu[1-n] = matrice des preferences des etudiants

Argument: 
    list<st> : données du fichier lu par lectureFichier (PrefEtu.txt)
return:
    int[][] : preferences etudiants
"""
def prefEtu(contenu):

    etuPrefs = contenu # copy, idk if its useful or not in python

    nbEtu = int(etuPrefs[0])
    etuPrefs.pop(0)
    
    #matrice de int
    prefs = np.zeros([nbEtu, 9], dtype = int) #nbEtu lignes et nbMaster colonne (par l'enoncé on sait qu'il y a 9 masters)



    for line in etuPrefs :
        line = line.split()
        x = int(line[0])
        for y in range(2, len(line)):
            #print(y);
            value = int(line[y])
            
            prefs[x][y-2] = value


    return prefs


"""
Cette fonction sert a lire contenu (liste de chaine de caractere) obtenu par lecture du fichier en donnée representant les préferences des spécialités.
contenu[0] = nombre d'etudiant dans le fichier
contenu[1] = liste des places disponibles pour chaque specialité
contenu[2-n] = matrice des preferences des specialités

Argument: 
    list<st> : données du fichier lu par lectureFichier (PrefSpe.txt)
return:
    int[][], list<int> : preferences des masters, liste de capacite des masters
"""
def prefSpe(contenu):

    spePrefs = contenu # copy, idk if its useful or not in python

    nbEtu = int( (spePrefs[0].split())[1] )
    spePrefs.pop(0)

    capacite = []
    cap = spePrefs[0].split()
    cap.pop(0)
    for i in cap:
        capacite.append(i)
    spePrefs.pop(0)
    
    #matrice de int
    prefs = np.zeros([9, nbEtu], dtype = int) #nbMaster lignes et nbEtu colonne (par l'enoncé on sait qu'il y a 9 masters)

    for line in spePrefs :
        line = line.split()
        x = int(line[0])
        for y in range(2, len(line)):
            value = int(line[y])
            
            prefs[x][y-2] = value

    return prefs, capacite


"""
Cette fonction applique l'algorythme de Gayle-Shapley coté ETUDIANTS pour generer des mariages etudiant-master.

Arguments:
    int[][] : matrice des preferences des etudiants     (obtenu avec la fonction prefEtu)
    int[][] : matrice des preferences des masters       (obtenu avec la fonction prefSpe)
    list<int> : liste des capacites des masters         (obtenu avec la fonction prefSpe)

return:
    list<int, int> : liste des mariages etudiant-master selon Gayle-Shapley

""" 

def gayle_shapley(prefEtu, prefSpe, capacites) :
    
    curr_cap = [0] * len(capacites) #crée une liste de 0 de la taille de capacité (len(curr_cap) == 9 sinon probleme car on a seuelement 9 masters)
    
    etuPref = prefEtu #copy de prefEtu
    
    mariages = [] #resultat : list<int, int>
    
    etu = 0 #etu est l'indice de l'etudiant courant que l'on cherche a placer
    
    mariages[0].index(etu) #mariage[0] = 1 tuple -> .index(etu) return position de etu dans le tuple.
    
    while etu != -1 : #lorsque tous les etudiants sont placés etu = -1
        #if(any(etu in  for )
        #on recup le num du master voulu pour obtenir sa position dans les données
        demande = prefEtu[0]
        if (curr_cap[demande] < capacites[demande]) :
            

    pass


"""
Cette fonction applique l'algorythme de Gayle-Shapley coté MASTERS pour generer des mariages etudiant-master.

Arguments:
    int[][] : matrice des preferences des etudiants     (obtenu avec la fonction prefEtu)
    int[][] : matrice des preferences des masters       (obtenu avec la fonction prefSpe)
    list<int> : liste des capacites des masters         (obtenu avec la fonction prefSpe)

return:
    list<int, int> : liste des mariages etudiant-master selon Gayle-Shapley

""" 

def gayle_shapley2(prefEtu, prefSpe, capacites) :


    pass













    

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