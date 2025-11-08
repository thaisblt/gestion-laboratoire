import laboratoire
import ihm

def main():
    labo = laboratoire.laboratoire()

    # Enregistrer une arrivée
    laboratoire.enregistrer_arrivee(labo, 'Xavier', 'F305')
    laboratoire.enregistrer_arrivee(labo, 'Marc', 'F305')
    laboratoire.enregistrer_arrivee(labo, 'Sylvie', 'F307')
    laboratoire.enregistrer_arrivee(labo, 'Loic', 'F310')

    print(labo)
    print()

    # Afficher la liste du personnel
    ihm.liste_du_personnel(labo)
    print()

    # Vérifier si présent
    assert laboratoire.est_present(labo, 'Xavier')
    assert laboratoire.est_present(labo, 'Marc')
    assert not laboratoire.est_present(labo, 'Aurélie')

    # assert bureau(labo, 'Xavier') == 'F305'
    assert laboratoire.bureau(labo, 'Xavier') == 'F305'
    assert laboratoire.bureau(labo, 'Marc') == 'F305'
    assert laboratoire.bureau(labo, 'Sylvie') == 'F307'
    assert laboratoire.bureau(labo, 'Loic') == 'F310'
    print(labo)
    print()

    # Changer de nom
    laboratoire.changer_nom(labo, 'Sylvie', 'Pauline')
    print(labo)
    assert laboratoire.est_present(labo,'Pauline')
    assert not laboratoire.est_present(labo,'Sylvie')
    print()

    # Modifier un bureau
    laboratoire.modifier_bureau(labo, 'Xavier', 'F309')
    laboratoire.modifier_bureau(labo, 'Marc', 'F307')
    print(labo)
    assert laboratoire.bureau(labo, 'Xavier') == 'F309'
    assert laboratoire.bureau(labo, 'Marc') == 'F307'
    print()

    # Enregistrer un départ
    laboratoire.enregistrer_depart(labo, 'Loic')
    laboratoire.enregistrer_depart(labo, 'Pauline')
    print(labo)
    assert not laboratoire.est_present(labo, 'Loic')
    assert not laboratoire.est_present(labo, 'Pauline')
    
    print()

    # Test des exceptions 
    try :
        laboratoire.enregistrer_arrivee(labo, "Xavier", "F320")
        assert False, "Une PresentException aurait du être levée"
    except :
        laboratoire.PresentException
        pass

    try :
        laboratoire.enregistrer_depart(labo, "Martine")
        assert False, "Une AbsentException aurait du être levée"
    except :
        laboratoire.AbsentException
        pass


if __name__ == '__main__':
    main()