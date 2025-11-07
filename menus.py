""" 
    Module qui gère les menus

"""

def nouveau_menu():
    """ Créer un nouveau menu """
    return []

def ajouter_choix(menu, intitule, fonction, *param_fonction):
    """ Ajouter une ligne au menu et la fonction correspondante """
    menu.append((intitule, fonction, param_fonction))

def _afficher_menu(menu):
    """ Afficher le menu """
    print()
    print("_____________MENU______________")
    for num_choix , (intitule, _, _) in enumerate(menu, 1):
        print(f"{num_choix:2d} - {intitule}")
    print(f"{0:2} - Quitter")
    print()

def selectionner_choix(menu):
    """ Demander le choix utilisateur. Retourne le numero du choix """
    while True :
        try :
            num_choix = int(input("Votre choix ? "))
            if 0 <= num_choix <= len(menu):
                return num_choix
            else :    
                print("Choix non valide.")
        except ValueError :
            print("Vous devez entrer un entier.")

def _traiter_choix(menu, num_choix) :
    """ Traiter le choix utilisateur """
    if num_choix != 0 :
        _, fonction, param = menu[num_choix-1]
        fonction(*param)

def gerer_menu(menu):
    """ Gerer un menu utilisateur """
    fini = False
    while not fini :
        _afficher_menu(menu)
        choix = selectionner_choix(menu)
        _traiter_choix(menu, choix)
        fini = choix == 0

