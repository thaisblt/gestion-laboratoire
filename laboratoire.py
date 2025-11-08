import csv

class LaboException(Exception):
    """ Généralise les exceptions du laboratoire."""
    pass

class PresentException(LaboException) :
    """ """
    pass

class AbsentException(LaboException) : 
    """ """
    pass

'''
Les opérations sur le laboratoire sans interactions avec l'utilisateur.
Pas de input, pas de print.
Backend.
Partie réutilisable entre les différentes IHM.
python labo_cmd.py add Xavier F305
'''

# Définir ce qu'est un laboratoire ? Quel type ?

# Réponse : dictionnaire, clé = personne, valeur = bureau

'''
Evolution possible :
    labo = {
        'bureaux' : {
            'F305': 4,
            'F307': 2,
        },
        'affectations': {
            'Xavier': 'F305',
        }

    }
'''

# Gérer un laboratoire 

def laboratoire():
    """ Créer un nouveau laboratoire """
    return {}

def enregistrer_arrivee(labo, nom, bureau):
    """ Ajouter un nouveau membre au laboratoire """
    if nom in labo:
        raise PresentException
    labo[nom] = bureau

def enregistrer_depart(labo, nom) :
    """ Supprimer un membre du laboratoire """
    if nom not in labo :
        raise AbsentException
    del labo[nom]
    
def modifier_bureau(labo, nom, bureau) :
    """ Modifier le bureau d'un membre du laboratoire """
    if nom not in labo :
        raise AbsentException
    labo[nom] = bureau

def changer_nom(labo, nom, nouveau_nom) :
    """ Modifier le nom d'un membre déjà existant du laboratoire """
    if nom not in labo :
        raise AbsentException
    labo[nouveau_nom] = labo.pop(nom)

def est_present(labo, nom) :
    """ Vérifier qu'une personne fait partie du laboratoire. Retourne True si présent, False sinon"""
    return nom in labo

def bureau(labo, nom) :
    """ Obtenir le bureau d'un membre. Retourne le bureau occupé par ce membre """
    if nom not in labo :
        raise AbsentException
    return labo[nom]

def occupation_bureau(labo) :
    """ Afficher l'occupation des bureaux. Retourne le dictionnaire des bureaux et la liste de leurs occupants """
    # Récupérer les bureaux et la liste de leurs occupants
    dans_bureau = {}
    for nom, bureau in labo.items() :
        if bureau not in dans_bureau :
            dans_bureau[bureau] = []
        dans_bureau[bureau].append(nom)
    return dans_bureau

def occupation_bureau_html(labo) :
    """ Afficher l'occupation des bureaux sous la forme d'une page HTML. Retourne une liste du contenu de la page HTML """
    # Récupérer les bureaux et la liste de leurs occupants 
    dans_bureau = {}
    for nom, bureau in labo.items() :
        if bureau not in dans_bureau :
            dans_bureau[bureau] = []
        dans_bureau[bureau].append(nom)

    # Construire le contenu de la page HTML
    contenu_html = [
        "<!DOCTYPE html>",
        "<html>",
        "<head>",
        "<title>Occupations des bureaux</title>",
        "</head>",
        "<body>",
        "<h1>Occupation des bureaux</h1>"
    ]
    # Ajouter la liste des occupants au contenu et fermer les balises
    for bureau, occupants in sorted(dans_bureau.items()) :
        contenu_html.append(f"<h2>Bureau {bureau} :</h2>")
        contenu_html.append("<ul>")
        for occupant in sorted(occupants) :
            contenu_html.append(f"<li>{occupant}</li>")
        contenu_html.append("</ul>")    
    contenu_html.append("</body></html>")
    return contenu_html

def importer_donnees_csv(labo, nom_fichier_csv):
    """ Importer et convertir des données csv. 
        Retourne un dictionaire des nouvelles données 
        et une liste des conflits entre les 2 sources de données """
    
    # Convertir csv en dictionnaire
    nouvelles_donnees = {}
    with open(nom_fichier_csv ,"r", encoding="utf-8") as fichier:
        lecteur_csv = csv.DictReader(fichier)
        for ligne in lecteur_csv:
            nom = ligne["nom"]
            bureau = ligne["bureau"]
            nouvelles_donnees[nom] = bureau
    
    # lister les doublons
    doublons_conflits = []
    for nom, bureau in nouvelles_donnees.items():
        if nom in labo and labo[nom] != bureau:
            doublons_conflits.append(nom)

    # Supprimer les doublons
    for nom in doublons_conflits:    
        del nouvelles_donnees[nom]            

    return nouvelles_donnees, doublons_conflits


# Les opérations qui permettent de manipuler les données du labo.

def main():
    print('test')

if __name__ == '__main__':
    main()