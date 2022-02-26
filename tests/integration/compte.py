# Cette partie ajoute le dossier principal dans le path pour qu'il trouve les classes
import sys
import os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'..'))

# On importe nos classes
from classes.elements.compte import Compte as CompteModele
from classes.sql.compte import Compte as CompteSQL

if __name__ == "__main__":
    compte_sql = CompteSQL("comptes.db")

    # Test de creation de la table
    try:
        compte_sql.create_table()
    except Exception as e:
        print(f"Could not create the table. Maybe it already exists {e}")
    else:
        print(f"Table created")

    # Test d'insertion dans la table
    compte = CompteModele(libelle="Nouveau compte",solde=144.25)

    try:
        compte = compte_sql.save(compte)
    except Exception as e:
        print(f"Could not make the insertion {e}")
    else:
        print(f"Insert ok : {compte}")

    # Test de mise a jour dans la table
    compte.solde = 150.00
    compte.operations = list()

    try:
        compte = compte_sql.modify(compte)
    except Exception as e:
        print(f"Could not update in the database {e}")
    else:
        print(f"Update ok : {compte}")

    # Test de recuperation dans la base de donnees
    comptes = compte_sql.select_all()

    for b in comptes:
        print(f"Retrieved : {b}")

    # Test de suppression de la base de donnees
    try:
        compte_sql.delete(compte)
    except Exception:
        print(f"Delete failed")
    else:
        print(f"Delete ok")