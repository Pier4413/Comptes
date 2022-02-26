# Cette partie ajoute le dossier principal dans le path pour qu'il trouve les classes
import sys
import os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'..'))

# On importe nos classes
from classes.elements.budget import Budget as BudgetModele
from classes.sql.budget import Budget as BudgetSQL

if __name__ == "__main__":
    budget_sql = BudgetSQL("comptes.db")
    budget = BudgetModele(libelle="Nouveau budget")

    # Test de creation de la table
    try:
        budget_sql.create_table()
    except Exception:
        print(f"Could not create the table. Maybe it already exists")
    else:
        print(f"Table created")

    # Test d'insertion dans la table
    try:
        budget = budget_sql.save(budget)
    except Exception as e:
        print(f"Could not make the insertion {e}")
    else:
        print(f"Insert ok : {budget}")

    # Test de mise a jour dans la table
    budget.init = 10
    budget.courant = 3
    budget.libelle = "Libelle"

    try:
        budget = budget_sql.modify(budget)
    except Exception as e:
        print(f"Could not update in the database {e}")
    else:
        print(f"Update ok : {budget}")

    # Test de recuperation dans la base de donnees
    budgets = budget_sql.select_all()

    for b in budgets:
        print(f"Retrieved : {b}")

    # Test de suppression de la base de donnees
    try:
        budget_sql.delete(budget)
    except Exception:
        print(f"Delete failed")
    else:
        print(f"Delete ok")