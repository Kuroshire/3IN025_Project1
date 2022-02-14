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

Representation de data : faire une matrice des preferences du demandeur.
    -lorsque la demande est rejeté ou si il y a un meilleur couple de formé on met un -1 dans la matrice a la position 
    (permet de ne pas boucler sur les demandes car on peut juste skip les -1 et savoir ou on en est)


"""

def prefEtu(contenu):
    pass