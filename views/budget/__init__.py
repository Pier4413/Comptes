from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QSizePolicy

def LIBELLE_EXPANSION():
    return 3

def INIT_EXPANSION():
    return 2

def DEPENSE_EXPANSION():
    return 2

def COURANT_EXPANSION():
    return 2

def SUPPR_EXPANSION():
    return 1

def EXPANSION_POLICY():
    return QSizePolicy.Policy.MinimumExpanding

def ALIGNEMENT_POLICY():
    return Qt.AlignmentFlag.AlignCenter