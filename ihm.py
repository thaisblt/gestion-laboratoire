import laboratoire
import menus
import json

'''
Interface sur la labo avec menu textuel.
'''

def gerer_arrivee(labo):
    try:
        nom = input("Nom ? ")
        bureau = input("Bureau ? ")
        laboratoire.enregistrer_arrivee(labo, nom, bureau)
        print(f"{nom} a été ajouté")
    except laboratoire.PresentException :
        print(f"Impossible: {nom} est déjà présent.")

def gerer_depart(labo) :
    try :
        nom = input("Nom ? ")
        laboratoire.enregistrer_depart(labo, nom)
        print(f"{nom} a été supprimé.")      
    except laboratoire.AbsentException : 
            print(f"Impossible : {nom} n'est pas présent.")

def gerer_modifier_bureau(labo) :
    try : 
        nom = input("Nom ? ")
        bureau = input("Nouveau bureau ? ")
        laboratoire.modifier_bureau(labo, nom, bureau)
        print(f"{nom} est maintenant dans le bureau {bureau}.")
    except laboratoire.AbsentException : 
            print(f"Impossible : {nom} n'est pas présent.")

def gerer_changer_nom(labo) :
    try :
        nom = input("Nom à modifier ? ")
        nouveau_nom = input("Nouveau nom ? ")
        laboratoire.changer_nom(labo, nom, nouveau_nom)
        print(f"{nouveau_nom} a été modifié.")
    except laboratoire.AbsentException : 
        print(f"Impossible : {nom} n'est pas présent.")

def gerer_est_present(labo) : 
    """ """
    nom = input("Nom ? ")
    if laboratoire.est_present(labo, nom) :
        print(f"{nom} est membre de ce laboratoire")
    else :
        print(f"{nom} n'est pas membre de ce laboratoire")

def gerer_bureau(labo) :
    try :
        nom = input("Nom ? ")
        bureau = laboratoire.bureau(labo, nom)
        print(f"{nom} est dans le bureau {bureau}")
    except laboratoire.AbsentException : 
        print(f"Impossible : {nom} n'est pas présent.") 


# Afficher la liste de tous les membres du laboratoire et leurs bureaux
def liste_du_personnel(labo) :  
    for nom, bureau in labo.items() : 
       print(f"{nom : <8} : {bureau}")  

# Afficher les bureaux et la liste de leurs occupants
def gerer_occupation_bureau(labo) : 
    dans_bureau = laboratoire.occupation_bureau(labo)
    for bureau, occupants in sorted(dans_bureau.items()) :
        print(f"{bureau} :")
        print("\n".join(occupants))
    
def gerer_occupation_bureau_html(labo):
    # Ecrire le contenue HTML dans le fichier .html
    nom_fichier = 'occupations_bureaux.html'
    contenu_html = laboratoire.occupation_bureau_html(labo)
    with open(nom_fichier, 'w', encoding="utf-8") as fichier:
        fichier.write('\n'.join(contenu_html))
    print("Le fichier occupation_bureaux.html à été créé.")

def importer_donnees():
    """ Convertir les données. Retourne le dictionnaire laboratoire et ses données"""
    nom_fichier = 'donnees_labo.json'
    try:
        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            return json.load(fichier)
    except json.JSONDecodeError:
        return {}

def enregistrer_donnees(labo):
    with open("donnees_labo.json", "w", encoding="utf-8") as fichier:
        json.dump(labo, fichier)

def main():
    """labo = laboratoire.laboratoire()"""
    labo = importer_donnees()
    menu = menus.nouveau_menu()
    menus.ajouter_choix(menu, "Enregistrer une arrivée", gerer_arrivee, labo)
    menus.ajouter_choix(menu, "Enregistrer un départ", gerer_depart, labo)
    menus.ajouter_choix(menu, "Modifier un bureau", gerer_modifier_bureau, labo)
    menus.ajouter_choix(menu, "Modifier un nom", gerer_changer_nom, labo)
    menus.ajouter_choix(menu, "Vérifier la présence d'un membre", gerer_est_present, labo)
    menus.ajouter_choix(menu, "Obtenir le bureau d'un membre", gerer_bureau, labo)
    menus.ajouter_choix(menu, "Afficher la liste des membres avec le bureau occupé", liste_du_personnel, labo)
    menus.ajouter_choix(menu, "Afficher l'occupation des bureaux", gerer_occupation_bureau, labo)
    menus.ajouter_choix(menu, "Afficher l'occupation des bureaux (exportation au format HTML)", gerer_occupation_bureau_html, labo)
    menus.gerer_menu(menu)
    enregistrer_donnees(labo)


    """
    quitter = False
    labo = laboratoire.laboratoire()
    while not quitter:
        afficher_menu()
        choix = demander_choix()
        traiter_choix(choix, labo)
        print(labo)
        quitter = choix == 0
    """


if __name__ == '__main__':
    main()