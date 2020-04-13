import json
from datetime import date, timedelta
from random import *

# Source code: http://www.planet-libre.org/index.php?post_id=10399 ensuite modifie
# Entree: Date
# Sortie: Date decalee d'un jour
def next_date(date):
    date += timedelta(1)
    return date

# FONCTION QUI VA TIRER AU HASARD LES DONNEES ANORMALES
# RETOURNE UNE LISTE DES INDICES DES DONNEES ANORMALES
# PREND EN COMPTE UNE PROXIMITE DES DONNEES ANORMALES JUSQU'A 4
def choix_indice_valeurs_anormales():
    nb_valeurs_anormales = round(nb_valeurs_a_generer * pourcentage_donnees_anormales)
    liste = []
    liste_indices_val_anormale = []
    print(nb_valeurs_a_generer)
    if(nombre_donnees_anormales_proximite == 1):    # SI LE NOMBRE DE VALEURS ANORMALES CONSECUTIVES EST A 1
        for i in range(nb_valeurs_a_generer):
            liste.append(i)
        liste_indices_val_anormale = sample(liste, int(nb_valeurs_anormales))
    else:                                           # SI LES VALEURS ANORMALES SE SUIVENT
        while(len(liste_indices_val_anormale) < int(nb_valeurs_anormales)):
            indice_aleatoire = randint(1,nb_valeurs_a_generer + 1)

            if(nombre_donnees_anormales_proximite == 2):
                if(indice_aleatoire not in liste_indices_val_anormale and indice_aleatoire + 1 not in liste_indices_val_anormale):
                    liste_indices_val_anormale.append(indice_aleatoire)
                    if(len(liste_indices_val_anormale) < nb_valeurs_anormales): liste_indices_val_anormale.append(indice_aleatoire + 1)
            elif (nombre_donnees_anormales_proximite == 3):
                if(indice_aleatoire not in liste_indices_val_anormale and indice_aleatoire + 1 not in liste_indices_val_anormale and indice_aleatoire + 2 not in liste_indices_val_anormale):
                    liste_indices_val_anormale.append(indice_aleatoire)
                    if(len(liste_indices_val_anormale) < nb_valeurs_anormales): liste_indices_val_anormale.append(indice_aleatoire + 1)
                    if(len(liste_indices_val_anormale) < nb_valeurs_anormales): liste_indices_val_anormale.append(indice_aleatoire + 2)
            elif (nombre_donnees_anormales_proximite == 4):
                if(indice_aleatoire not in liste_indices_val_anormale and indice_aleatoire + 1 not in liste_indices_val_anormale and indice_aleatoire + 2 not in liste_indices_val_anormale):
                    liste_indices_val_anormale.append(indice_aleatoire)
                    if(len(liste_indices_val_anormale) < nb_valeurs_anormales): liste_indices_val_anormale.append(indice_aleatoire + 1)
                    if(len(liste_indices_val_anormale) < nb_valeurs_anormales): liste_indices_val_anormale.append(indice_aleatoire + 2)
                    if(len(liste_indices_val_anormale) < nb_valeurs_anormales): liste_indices_val_anormale.append(indice_aleatoire + 3)
    return liste_indices_val_anormale


# Date de depart
day = 01
month = 04
year = 2020
d = date(year, month, day)


data = {}

# PERSONNE 'NORMALE'
# LUMINOSITE EN %
luminosite_min = 1
luminosite_moy = 65
luminosite_max = 100
luminosite_ecart_normal = 20

# TEMPERATURE EN DEGRES CELCIUS
temperature_min = 1
temperature_moy = 20
temperature_max = 35
temperature_ecart_normal = 3

# MOUVEMENT EN PAS
mouvement_moy = 10000
mouvement_ecart_normal = 2000

# ANXIEUX
luminosite_ecart_anxieux = -30
mouvement_ecart_anxieux = +5000

# DEPRESSIF
luminosite_ecart_depressif = -30
mouvement_ecart_depressif = -4000

# NOMBRE DE DONNEES EN DEHORS DE LA NORMALE
# 0.05 -> 5%
pourcentage_donnees_anormales = 0.06

# PARAMETRE DE PROXIMITE (X DONNEES ANORMALES D'AFFILEE)
nombre_donnees_anormales_proximite = 3

nb_valeurs_a_generer = int(input("Merci d'entrer le nombre de donnees a generer : "))
choix_profil_personne = int(input("Merci de choisir un profil parmi ceux-ci:\n  1 - Normal\n  2 - Anxieux\n  3 - Depressif\n"))
if(choix_profil_personne == 1): # NORMAL
    print("Donnees generees pour une personne normale")
elif(choix_profil_personne == 2): # ANXIEUX
    luminosite_moy += luminosite_ecart_anxieux
    mouvement_moy += mouvement_ecart_anxieux
    print("Donnees generees pour une personne anxieuse")
elif (choix_profil_personne == 3): # DEPRESSIF
    luminosite_moy += luminosite_ecart_depressif
    mouvement_moy += mouvement_ecart_depressif
    print("Donnees generees pour une personne depressive")
else:
    print("MERCI DE CHOISIR 1 2 ou 3")
    quit(0)


calcul_nb_donnees_anormales = round(nb_valeurs_a_generer * pourcentage_donnees_anormales)
print ("Nombre de valeurs anormales: " + str(calcul_nb_donnees_anormales))


liste_indices_val_anormales = choix_indice_valeurs_anormales()
# print(liste_indices_val_anormales)

i = 1
while i <= nb_valeurs_a_generer:
    date = d.strftime('%d-%m-%Y')
    d = next_date(d)
    data[date] = []
    if(i in liste_indices_val_anormales):   # SI LA VALEUR QUI VA ETRE AJOUTEE EST UNE VALEUR ANORMALE
        temperature = randint(temperature_moy + temperature_ecart_normal,temperature_moy + (2 * temperature_ecart_normal))
        luminosite = randint(luminosite_moy + luminosite_ecart_normal, luminosite_moy + (2 * luminosite_ecart_normal))
        mouvement = randint(mouvement_moy + mouvement_ecart_normal, mouvement_moy + (2 * mouvement_ecart_normal))
        #print ("Valeur anormale indice: " + str(i) + "\nTemp:" + str(temperature) + "\nLumi:" + str(luminosite) +"\nMouv:" + str(mouvement) + "\n")

    else:                                   # SI LA VALEUR N'EST PAS ANORMALE
        temperature = randint(temperature_moy - temperature_ecart_normal,temperature_moy + temperature_ecart_normal)
        luminosite = randint(luminosite_moy - luminosite_ecart_normal, luminosite_moy + luminosite_ecart_normal)
        mouvement = randint(mouvement_moy - mouvement_ecart_normal, mouvement_moy + mouvement_ecart_normal)
        #print ("Valeur: indice: " + str(i) + "\nTemp:" + str(temperature) + "\nLumi:" + str(luminosite) +"\nMouv:" + str(mouvement) + "\n")

    data[date].append({
        'temperature': temperature,
        'luminosite': luminosite,
        'mouvement': mouvement
    })
    i = i+1

# ECRIS L'ENSEMBLE DES DONNEES GENEREES DANS LE FICHIER DATA.JSON
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)

