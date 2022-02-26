# Cette partie ajoute le dossier principal dans le path pour qu'il trouve les classes
import sys
import os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'..'))

# On importe nos classes
from classes.elements.operation import Operation as OperationModele
from classes.sql.operation import Operation as OperationSQL

if __name__=="__main__":
    operation_sql = OperationSQL("comptes.db")
    operation = OperationModele(libelle="Ma nouvelle operation")

    # Test de creation de la base de donnees
    try:
        operation_sql.create_table()
    except Exception as e:
        print(f"Erreur dans la creation de la table operation, {e}")
    else:
        print(f"Creation de la table")

    # Test d'insertion dans la table
    try:
        operation.compte = 1
        operation.budget = 1
        operation_sql.save(operation)
    except Exception as e:
        print(f"Erreur insertion operation, {e}")
    else:
        print(f"Insertion reussie")

    #Test de mise à jour dans la table
    try:
        operation.budget = 2
        operation.compte = 3
        operation.libelle = "Operation reussie"
        operation.montant = 5.2
        operation_sql.modify(operation)
    except Exception as e:
        print(f"Erreur dans la modification, {e}")
    else:
        print(f"Modification reussie")

    # Test de recuperation dans la base de donnees
    operations = operation_sql.select_all()

    for o in operations:
        print(f"Retrouvee : {o}")

    # Test de suppression
    try:
        operation_sql.delete(operation)
    except Exception as e:
        print(f"Suppression echouee. Erreur : {e}")
    else:
        print(f"Suppression reussie")