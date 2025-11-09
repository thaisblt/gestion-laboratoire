Gestion des membres d'un laboratoire

Ce programme permet de gérer les membres d'un laboratoire ainsi que les bureaux qu'ils occupent.
Les données sont sauvegardées automatiquement en JSON pour assurer la persistance lors de la fermeture du programme.

Fonctionnalités principales :
  - Ajouter un membre et son bureau
  - Supprimer un membre
  - Modifier le nom d'un membre
  - Modifier le bureau d'un membre
  - Vérifier si un membre est présent dans le laboratoire
  - Afficher le bureau d'un membre
  - Voir la liste complète des membres
  - Afficher l'occupation des bureaux
  - Exporter l'occupation des bureaux au format HTML
  - Importer de nouvelles données depuis un fichier CSV
  - Importation depuis un fichier CSV

Pour importer un fichier CSV, celui-ci doit se trouver dans le même dossier que le programme.
Lorsque l'importation est lancée :
  - Les nouveaux membres sont ajoutés automatiquement au laboratoire.
  - Si un membre existe déjà mais avec un bureau différent, le programme signale un conflit.

Sauvegarde des données :
  - Toutes les modifications sont sauvegardées dans le fichier donnees_labo.json
  - Ce fichier est créé automatiquement si nécessaire.

L'interface dans le terminal propose un menu pour accéder aux différentes fonctionnalités.
