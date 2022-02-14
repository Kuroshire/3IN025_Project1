"""ouvre un fichier et retourne une liste de lignes
"""
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

"""prend une liste de lignes et retourne une liste de liste des préférences par étudiant
"""		
def prefEtu(contenu):
	contenu[0]=contenu[0].split()     # ligne.split() renvoie une liste de toutes les chaines contenues dans la chaine ligne (separateur=espace) 
	for i in range(1, int(contenu[0][0])+1):
		contenu[i]=contenu[i].split()
		contenu[i].pop(0)
		contenu[i].pop(0)
	contenu.pop(0)
	for i in range(len(contenu)):
		for j in range(len(contenu[i])):
			contenu[i][j] = int(contenu[i][j])
	return contenu
	
"""prend une liste de lignes et retourne un tuple composé d'une liste de listes des préférences par master et une liste des capacités de chaque master
"""
def prefSpe(contenu):
	contenu.pop(0)
	capacites = contenu[0].split()
	capacites.pop(0)
	for i in range(len(capacites)):
		capacites[i] = int(capacites[i])
	contenu.pop(0)
	for i in range(9):
		contenu[i]=contenu[i].split()
		contenu[i].pop(0)
		contenu[i].pop(0)
	for i in range(len(contenu)):
		for j in range(len(contenu[i])):
			contenu[i][j] = int(contenu[i][j])
	return contenu, capacites
	
"""retourne un etudiant qui est libre et qui n'a pas candidaté dans tous les masters s'il existe
ou -1 sinon
"""
def existe_etu_libre_nonrejete_partout(affectations, candidatures):
    for etu in affectations.keys():
        if (affectations[etu] == -1): #libre
            if (len(candidatures[etu]) < len(candidatures)): #n'a pas proposé à tout le monde
                return etu
    return -1

"""retourne le master temporaire affecté à un étudiant
"""
def master(spe, affectations):
    for etu in affectations.keys():
        if (affectations[etu] == spe):
            return etu
"""retourne l'etu le moins prefere par une spe parmi ceux qui lui ont été affecté
"""        
def etu_affecte_le_moins_pref(spe, pref_spe, affectations):
    for etu in pref_spe[::-1]:
        if (affectations[etu] == spe):
            return etu

"""retourne une affectation stable des etudiants aux masters
"""
def gayle_shapley(etudiants, masters, capacites):
    affectations = dict()
    candidatures = dict()
    nb_affectations_par_spe = list()
    
    for etu in range(len(etudiants)):
        affectations[etu] = -1
        candidatures[etu] = []
        
    for spe in range(len(masters)):
        nb_affectations_par_spe.append(0)

    etu = existe_etu_libre_nonrejete_partout(affectations, candidatures)  
    while ( etu != -1):
        for spe in etudiants[etu]:
            if (spe not in candidatures[etu]):
                candidatures[etu].append(spe)
                
                #si spe n'a pas atteint sa capacite max
                if (nb_affectations_par_spe[spe] < capacites[spe]):
                    affectations[etu] = spe
                    nb_affectations_par_spe[spe] = nb_affectations_par_spe[spe] + 1
                    break
                    
                #si spe pas libre mais prefere etu à l'etu qu'il accueille
                elif (masters[spe].index(etu) < masters[spe].index(etu_affecte_le_moins_pref(spe, masters[spe], affectations))):
                    affectations[etu_affecte_le_moins_pref(spe, masters[spe], affectations)] = -1
                    affectations[etu] = spe
                    break
        etu = existe_etu_libre_nonrejete_partout(affectations, candidatures)

    return affectations

#masters : liste des masters
def gayle_shapley2(masters, etudiants, capacites):
    affectations = dict()   #dico : cle: indice du master, valeur: liste des etudiants(int)
    demandes = dict()       #dico : cle: indice de master, valeur: liste etu

    for i in range(len(masters)):
        affectations[i] = []
        demandes[i] = []

    print(affectations)

    #master avec une place dispo
    num = place_dispo(affectations, capacites)
    while( num != -1):
        print(affectations)
        #print("num = " + str(num))
        
        for etu in masters[num] :   #master[num] = list[int]
            print("bique")
    
            if(etu not in demandes[num]):
                print("sa")
                demandes[num].append(etu)

                master = cherche_dans_dico(affectations, etu)
                #si etudiant n'a pas de master
                if master == -1:
                    affectations[num].append(etu)

                #si etudiant possede un master moins interressant
                elif etudiants[etu].index(num) < etudiants[etu].index(master):
                    affectations[master].remove(etu)
                    affectations[num].append(etu)
                    print("maman")
                
        num = place_dispo(affectations, capacites)

    return affectations


#return numero du premier master qui possede une place, sinon -1
def place_dispo(affectations, capacites):
    for i in range(len(affectations)):
        if(len(affectations[i]) < capacites[i]):
            return i

    return -1

#return int
#dico : dictionnaire[int] : list[int],  cherche = int
def cherche_dans_dico(dico, cherche):
    for k in dico:
        if cherche in dico[k]:
            return k
    return -1
