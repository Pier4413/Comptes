# Cette partie ajoute le dossier principal dans le path pour qu'il trouve les classes
import sys
import os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'..'))

# On importe nos classes
from classes.elements.compte import Compte as CompteModele
from classes.sql.compte import Compte as CompteSQL

if __name__ == "__main__":
    compteSql = CompteSQL()

    # Test de creation de la table
    try:
        compteSql.createTable()
    except Exception as e:
        print("Could not create the table. Maybe it already exists"+str(e))
    else:
        print("Table created")

    # Test d'insertion dans la table
    compte = CompteModele(libelle="Nouveau compte",solde=144.25)

    try:
        compte = compteSql.save(compte)
    except Exception as e:
        print("Could not make the insertion"+ str(e))
    else:
        print("Insert ok : "+str(compte))

    # Test de mise a jour dans la table
    compte.Solde = 150.00
    compte.operations = list()

    try:
        compte = compteSql.modify(compte)
    except Exception as e:
        print("Could not update in the database"+str(e))
    else:
        print("Update ok : "+str(compte))

    # Test de recuperation dans la base de donnees
    comptes = compteSql.selectAll()

    for b in comptes:
        print("Retrieved : "+str(b))

    # Test de suppression de la base de donnees
    try:
        compteSql.delete(compte)
    except Exception:
        print("Delete failed")
    else:
        print("Delete ok")