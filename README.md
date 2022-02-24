# Comptes
Petite application de gestion de comptes

## Parametres

Il est possible de gerer les paramètres depuis un fichier au format ini dont on peut fournir le chemin a l'execution avec l'option `--settings`

A noter : La valeur par défaut pour le chemin du fichier de configuration est : ./conf/settings.ini

Les sections disponibles sont les suivantes :

- Translation : Gere la traduction
- Window : Gere l'affichage
- Database : Gere la base de donnees

Les options sont les suivantes :

- Translation
  - folder_path : Le chemin du dossier contenant les fichiers de traduction
  - locale : La locale a utiliser pour les traductions
- Window :
  - width : La largeur de départ de la fenêtre
  - height : La hauteur de départ de la fenêtre
- Database :
  - filename : Le chemin du fichier de base de données SQLite3 de l'application