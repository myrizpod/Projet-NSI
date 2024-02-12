# Projet-NSI
  _____ __  __ _____   ____  _____ _______       _   _ _______  
 |_   _|  \/  |  __ \ / __ \|  __ \__   __|/\   | \ | |__   __| 
   | | | \  / | |__) | |  | | |__) | | |  /  \  |  \| |  | |    
   | | | |\/| |  ___/| |  | |  _  /  | | / /\ \ | . ` |  | |    
  _| |_| |  | | |    | |__| | | \ \  | |/ ____ \| |\  |  | |    
 |_____|_|  |_|_|     \____/|_|  \_\ |_/_/    \_\_| \_|  |_|    
                                                                
IL FAUT DESORMAIS LE FICHIER MAIN ET GAME DANS LE MEME REPERTOIR ET LANCER LE MAIN.

Est-ce que toutes les paramètres (ligne19 à 39) ne pourraient pas être définis comme des attributs de l'objet de la classe Game lors de son initialisation ? Ça éviterait d'utiliser des variables globales. Il faudrait de même supprimer les autres variables globales. En programmation orientée objet, ce n'est ni nécessaire, ni souhaitable.
Les variables e et g pourraient être mieux nommées et g ne devrait-il pas plutôt être un booléen ? Je n'ai pas trouvé à quoi servait e ...
La méthode update mériterait quelques commentaires supplémentaires. Dans cette méthode, je vois aussi beaucoup de valeurs numériques qui servent sans doute à régler des problèmes d'affichage. Ces valeurs devraient être dans des variables de paramétrisation afin de pouvoir les changer facilement par la suite.
Dans les méthodes detect_collisions_obstacles() et detect_collisions_coins(), un while serait plus propre qu'un for avec un break.
Ligne 172, "return i" est plus clair et prendrait moins de ressources.
Toutes les méthodes devraient avoir au moins un commentaire (docstring).
