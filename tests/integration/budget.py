# Cette partie ajoute le dossier principal dans le path pour qu'il trouve les classes
import sys
import os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'..'))

# On importe nos classes
from classes.elements.budget import Budget as BudgetModele
from classes.sql.budget import Budget as BudgetSQL

if __name__ == "__main__":
    budgetSql = BudgetSQL()

    # Test de creation de la table
    try:
        budgetSql.createTable()
    except Exception:
        print("Could not create the table. Maybe it already exists")
    else:
        print("Table created")

    # Test d'insertion dans la table
    budget = BudgetModele(libelle="Nouveau budget")

    try:
        budget = budgetSql.save(budget)
    except Exception:
        print("Could not make the insertion")
    else:
        print("Insert ok : "+budget)

    # Test de mise a jour dans la table
    budget.init = 10
    budget.courant = 3
    budget.libelle = "Libelle"

    try:
        budget = budgetSql.modify(budget)
    except Exception:
        print("Could not update in the database")
    else:
        print("Update ok : "+budget)

    # Test de recuperation dans la base de donnees
    budgets = budgetSql.selectAll()

    for b in budgets:
        print("Retrieved : "+b)

    # Test de suppression de la base de donnees
    try:
        budgetSql.delete(budget)
    except Exception:
        print("Delete failed")
    else:
        print("Delete ok")