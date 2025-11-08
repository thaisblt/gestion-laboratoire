import laboratoire
import menus
import json

'''
Interface sur la labo avec menu textuel.
'''

def gerer_arrivee(labo):
    """
    Demander à l'utilisateur le nom du membre à ajouter et son bureau. 
    Ajouter le membre au laboratoire.
    param labo : dictionnaire contenant les membres et leurs bureaux.
    """
    try:
        nom = input("Nom ? ")
        bureau = input("Bureau ? ")
        laboratoire.enregistrer_arrivee(labo, nom, bureau)
        print(f"{nom} a été ajouté")
    except laboratoire.PresentException :
        print(f"Impossible: {nom} est déjà présent.")

def gerer_depart(labo) :
    """
    Demander à l'utilisateur le nom à supprimer. 
    Puis supprimer le membre du laboratoire.
    param labo : dictionnaire contenant les membres et leurs bureaux.
    """
    try :
        nom = input("Nom ? ")
        laboratoire.enregistrer_depart(labo, nom)
        print(f"{nom} a été supprimé.")      
    except laboratoire.AbsentException : 
            print(f"Impossible : {nom} n'est pas présent.")

def gerer_modifier_bureau(labo) :
    """
    Demander un nom à l'utilisateur puis le nouveau bureau à attribuer. 
    Attribuer le nouveau bureau  au membre.
    param labo : dictionnaire contenant les membres et leurs bureaux.
    """
    try : 
        nom = input("Nom ? ")
        bureau = input("Nouveau bureau ? ")
        laboratoire.modifier_bureau(labo, nom, bureau)
        print(f"{nom} est maintenant dans le bureau {bureau}.")
    except laboratoire.AbsentException : 
            print(f"Impossible : {nom} n'est pas présent.")

def gerer_changer_nom(labo) :
    """
    Demander un nom à l'utilisateur puis le nouveau nom à donner. 
    Modifier l'ancien nom par le nouveau.
    param labo : dictionnaire contenant les membres et leurs bureaux.
    """
    try :
        nom = input("Nom à modifier ? ")
        nouveau_nom = input("Nouveau nom ? ")
        laboratoire.changer_nom(labo, nom, nouveau_nom)
        print(f"{nouveau_nom} a été modifié.")
    except laboratoire.AbsentException : 
        print(f"Impossible : {nom} n'est pas présent.")

def gerer_est_present(labo) : 
    """
    Demander un nom à l'utilisateur et indiquer si ce membre est présent
    dans le laboratoire ou non.
    param labo : dictionnaire contenant les membres et leurs bureaux.
    """
    nom = input("Nom ? ")
    if laboratoire.est_present(labo, nom) :
        print(f"{nom} est membre de ce laboratoire")
    else :
        print(f"{nom} n'est pas membre de ce laboratoire")

def gerer_bureau(labo) :
    """
    Demander un nom à l'utilisateur et indiquer dans quel bureau se trouve ce membre
    param labo : dictionnaire contenant les membres et leurs bureaux.
    """
    try :
        nom = input("Nom ? ")
        bureau = laboratoire.bureau(labo, nom)
        print(f"{nom} est dans le bureau {bureau}")
    except laboratoire.AbsentException : 
        print(f"Impossible : {nom} n'est pas présent.") 

def liste_du_personnel(labo) :  
    """
    Afficher la liste de tous les membres du laboratoire et leurs bureaux
    param labo : dictionnaire contenant les membres et leurs bureaux.
    """
    for nom, bureau in labo.items() : 
       print(f"{nom : <8} : {bureau}")  

def gerer_occupation_bureau(labo) : 
    """
    Afficher les bureaux et la liste de leurs occupants
    param labo : dictionnaire contenant les membres et leurs bureaux.
    """
    dans_bureau = laboratoire.occupation_bureau(labo)
    for bureau, occupants in sorted(dans_bureau.items()) :
        print(f"{bureau} :")
        print("\n".join(occupants))
    
def gerer_occupation_bureau_html(labo):
    """
    Créer le fichier html et écrire le contenu HTML dedans.
    param labo : dictionnaire contenant les membres et leurs bureaux.
    """
    nom_fichier = 'occupations_bureaux.html'
    contenu_html = laboratoire.occupation_bureau_html(labo)
    with open(nom_fichier, 'w', encoding="utf-8") as fichier:
        fichier.write('\n'.join(contenu_html))
    print("Le fichier occupation_bureaux.html à été créé.")

def charger_donnees():
    """
    Charger les données du laboratoire depuis le fichier JSON.
    Retourne un dictionnaire contenant les membres et leurs bureaux.
    Si le fichier est vide ou inexistant, retourne un dictionnaire vide.
    """
    nom_fichier = 'donnees_labo.json'
    try:
        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            return json.load(fichier)
    except json.JSONDecodeError:
        return {}

def sauvegarder_donnees(labo):
    """
    Sauvegarder les données du laboratoire dans le fichier JSON.
    param labo : le dictionnaire contenant les membres et leurs bureaux à enregistrer.
    """
    with open("donnees_labo.json", "w", encoding="utf-8") as fichier:
        json.dump(labo, fichier)

def gerer_importer_donnees_csv(labo):
    """
    Demander à l'utilisateur un nom de fichier CSV puis l'importer
    Signaler les conflits éventuels, puis fusionner les nouvelles données
    avec celles déjà présentes dans le laboratoire.
    param labo : dictionnaire à mettre à jour.
    """
    nom_fichier_csv = input("Nom du fichier csv à importer ? ")

    try:
        nouvelles_donnees, doublons_conflits = laboratoire.importer_donnees_csv(labo, nom_fichier_csv)
    except FileNotFoundError :
        print("Fichier introuvable")
        return
    
    # Afficher les doublons avec des bureaux différents
    for nom in doublons_conflits:
        print(f"- {nom} déjà enregistré dans un bureau différent")
    print()

    # Fusionner les données csv avec celle du laboratoire
    labo.update(nouvelles_donnees)
    print("Les données ont bien été mises à jour")
    print()


def main():

    labo = charger_donnees()
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
    menus.ajouter_choix(menu, "Importer de nouvelles données (format csv)", gerer_importer_donnees_csv, labo)
    menus.gerer_menu(menu)
    sauvegarder_donnees(labo)


if __name__ == '__main__':
    main()