# Consigne: On souhaite déterminer le nombre de mots de 1 lettre, 2 lettres, 3 lettres… que contient un texte.
# Le texte contient un ensemble de mots, séparés par des espaces, sans aucun signe de ponctuation

# Exemple texte : 
# La cigale ayant chanté
# Tout l'été,
# Se trouva fort dépourvue
# Quand la bise fut venue.

phrase = input() 

liste = []
for mot in phrase.split():
  liste.append(len(mot))

for i in range(max(liste) + 1):
  if liste.count(i) != 0:
    print(i, ':', liste.count(i))
    
    
 # output :
# 2 : 3
# 3 : 1
# 4 : 3
# 5 : 2
# 6 : 5
# 9 : 1
        
