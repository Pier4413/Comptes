# Cette partie ajoute le dossier principal dans le path pour qu'il trouve les classes
import sys
import os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'..'))

# On importe nos classes
from classes.elements.operation import Operation as OperationModele
from classes.sql.operation import Operation as OperationSQL

if __name__=="__main__":
    operationSQL = OperationSQL()
    operation = OperationModele(libelle="Ma nouvelle operation")

    # Test de creation de la base de donnees
    try:
        operationSQL.createTable()
    except Exception as e:
        print("Erreur dans la creation de la table operation, "+str(e))
    else:
        print("Creation de la table")

    # Test d'insertion dans la table
    try:
        operation.compte = 1
        operation.budget = 1
        operationSQL.save(operation)
    except Exception as e:
        print("Erreur insertion operation, "+str(e))
    else:
        print("Insertion reussie")

    #Test de mise à jour dans la table
    try:
        operation.budget = 2
        operation.compte = 3
        operation.libelle = "Operation reussie"
        operation.montant = 5.2
        operationSQL.modify(operation)
    except Exception as e:
        print("Erreur dans la modification, "+str(e))
    else:
        print("Modification reussie")

    # Test de recuperation dans la base de donnees
    operations = operationSQL.selectAll()

    for o in operations:
        print("Retrouvee : "+str(o))

    # Test de suppression
    try:
        operationSQL.delete(operation)
    except Exception as e:
        print("Suppression echouee, "+str(e))
    else:
        print("Suppression reussie")