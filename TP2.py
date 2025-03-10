"""
TP2 : Gestion d'une base de données d'un hôpital

Groupe de laboratoire : 02
Numéro d'équipe :  10
Noms et matricules : Charlorin kateleen (2437457), Alice Delisle (2436614)
"""

import csv


########################################################################################################## 
# PARTIE 1 : Initialisation des données (2 points)
##########################################################################################################

def load_csv(csv_path):
    """
    Fonction python dont l'objectif est de venir créer un dictionnaire "patients_dict" à partir d'un fichier csv

    Paramètres
    ----------
    csv_path : chaîne de caractères (str)
        Chemin vers le fichier csv (exemple: "/home/data/fichier.csv")
    
    Résultats
    ---------
    patients_dict : dictionnaire python (dict)
        Dictionnaire composé des informations contenues dans le fichier csv
    """
    patients_dict = {}
    # TODO : Écrire votre code ici
    with open(csv_path, newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader : 
            patient_id = row['participant_id']
            patients_dict[patient_id] = {
                'sex': row['sex'],
                'age': row['age'],
                'height': row['height'],
                'weight': row['weight'],
                'date_of_scan': row['date_of_scan'], 
                'pathology': row['pathology']
            }

    # Fin du code

    return patients_dict
   

########################################################################################################## 
# PARTIE 2 : Fusion des données (3 points)
########################################################################################################## 

def load_multiple_csv(csv_path1, csv_path2):
    """
    Fonction python dont l'objectif est de venir créer un unique dictionnaire "patients" à partir de deux fichier csv

    Paramètres
    ----------
    csv_path1 : chaîne de caractères (str)
        Chemin vers le premier fichier csv (exemple: "/home/data/fichier1.csv")
    
    csv_path2 : chaîne de caractères (str)
        Chemin vers le second fichier csv (exemple: "/home/data/fichier2.csv")
    
    Résultats
    ---------
    patients_dict : dictionnaire python (dict)
        Dictionnaire composé des informations contenues dans les deux fichier csv SANS DUPLICATIONS
    """
    patients_dict = {}

    # TODO : Écrire votre code ici
    csv_paths = [csv_path1, csv_path2]
    for csv_path in csv_paths:
        with open(csv_path, newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                patient_id = row['participant_id']
                if patient_id not in patients_dict:
                    patients_dict[patient_id] = {
                        'sex': row['sex'],
                        'age': row['age'],
                        'height': row['height'],
                        'weight': row['weight'],
                        'date_of_scan': row['date_of_scan'],
                        'pathology': row['pathology']
                    }

    # Fin du code

    return patients_dict

########################################################################################################## 
# PARTIE 3 : Changements de convention (4 points)
########################################################################################################## 

def update_convention(old_convention_dict):
    """
    Fonction python dont l'objectif est de mettre à jour la convention d'un dictionnaire. Pour ce faire, un nouveau dictionnaire
    est généré à partir d'un dictionnaire d'entré.

    Paramètres
    ----------
    old_convention_dict : dictionnaire python (dict)
        Dictionnaire contenant les informations des "patients" suivant l'ancienne convention
    
    Résultats
    ---------
    new_convention_dict : dictionnaire python (dict)
        Dictionnaire contenant les informations des "patients" suivant la nouvelle convention
    """
    new_convention_dict = {}

    # TODO : Écrire votre code ici
    new_convention_dict = old_convention_dict
    for id in new_convention_dict:
        new_convention_dict[id]['date_of_scan'] = new_convention_dict[id]['date_of_scan'].replace('-', '/')
        if new_convention_dict[id]['date_of_scan'] == "n/a":
            new_convention_dict[id]['date_of_scan'] = None

    # Fin du code

    return new_convention_dict

########################################################################################################## 
# PARTIE 4 : Recherche de candidats pour une étude (5 points)
########################################################################################################## 

def fetch_candidates(patients_dict):
    """
    Fonction python dont l'objectif est de venir sélectionner des candidats à partir d'un dictionnaire patients et 3 critères:
    - sexe = femme
    - 25 <= âge <= 32
    - taille > 170

    Paramètres
    ----------
    patients_dict : dictionnaire python (dict)
        Dictionnaire contenant les informations des "patients"
    
    Résultats
    ---------
    candidates_list : liste python (list)
        Liste composée des `participant_id` de l'ensemble des candidats suivant les critères
    """
    candidates_list = []

    # TODO : Écrire votre code ici
    for participant_id in patients_dict:
        if patients_dict[participant_id]['sex']=='F' and\
            patients_dict[participant_id]['age'] >= '25' and \
            patients_dict[participant_id]['age'] <= '32' and \
            patients_dict[participant_id]['height'] != 'n/a' and \
            patients_dict[participant_id]['height'] > '170':
            candidates_list.append(participant_id)

    # Fin du code

    return candidates_list

########################################################################################################## 
# PARTIE 5 : Statistiques (6 points)
########################################################################################################## 

def fetch_statistics(patients_dict):
    """
    Fonction python dont l'objectif est de venir calculer et ranger dans un nouveau dictionnaire "metrics" la moyenne et 
    l'écart type de l'âge, de la taille et de la masse pour chacun des sexes présents dans le dictionnaire "patients_dict".

    Paramètres
    ----------
    patients_dict : dictionnaire python (dict)
        Dictionnaire contenant les informations des "patients"
    
    Résultats
    ---------
    metrics : dictionnaire python (dict)
        Dictionnaire à 3 niveaux contenant:
            - au premier niveau: le sexe --> metrics.keys() == ['M', 'F']
            - au deuxième niveau: les métriques --> metrics['M'].keys() == ['age', 'height', 'weight'] et metrics['F'].keys() == ['age', 'height', 'weight']
            - au troisième niveau: la moyenne et l'écart type --> metrics['M']['age'].keys() == ['mean', 'std'] ...
    
    """
    metrics = {'M':{}, 'F':{}}

    # TODO : Écrire votre code ici

    males_age =[]
    males_height =[]
    males_weight = []
    females_age = []
    females_height = []
    females_weight = []
    
    for dic_participant_id in patients_dict.values(): 
        patient = dic_participant_id
        if patient['sex'] == 'M':
            males_age.append(int(dic_participant_id['age']))
            if patient['height'] != 'n/a':
                males_height.append(round(float(dic_participant_id['height']), 2))
                if patient['weight'] != 'n/a':
                    males_weight.append(round(float(dic_participant_id['weight']), 2))
        else: 
            females_age.append(int(dic_participant_id['age']))
            if patient['height'] != 'n/a':
                females_height.append(round(float(dic_participant_id['height']), 2))
                if patient['weight'] != 'n/a':
                    females_weight.append(round(float(dic_participant_id['weight']), 2))
    # Moyennes et écart-types pour les hommes
    metrics['M']['age'] = {'mean': round(sum(males_age)/len(males_age), 2),
                            'std': round((sum([(x - sum(males_age)/len(males_age))**2 for x in males_age])/len(males_age))**0.5, 2)} 
    
    metrics['M']['height'] = {'mean': round(sum(males_height)/len(males_height), 2),
                            'std': round((sum([(x - sum(males_height)/len(males_height))**2 for x in males_height])/len(males_height))**0.5, 2)} 
    
    metrics['M']['weight'] = {'mean': round(sum(males_weight)/len(males_weight), 2),
                            'std': round((sum([(x - sum(males_weight)/len(males_weight))**2 for x in males_weight])/len(males_weight))**0.5, 2)} 
    
    # Moyennes et écart-types pour les femmes
    metrics['F']['age'] = {'mean': round(sum(females_age)/len(females_age), 2),
                            'std': round((sum([(x - sum(females_age)/len(females_age))**2 for x in females_age])/len(females_age))**0.5, 2)} 
    
    metrics['F']['height'] = {'mean': round(sum(females_height)/len(females_height), 2),
                            'std': round((sum([(x - sum(females_height)/len(females_height))**2 for x in females_height])/len(females_height))**0.5, 2)} 
    
    metrics['F']['weight'] = {'mean': round(sum(females_weight)/len(females_weight), 2),
                            'std': round((sum([(x - sum(females_weight)/len(females_weight))**2 for x in females_weight])/len(females_weight))**0.5, 2)}        
    
    # Fin du code

    return metrics

########################################################################################################## 
# PARTIE 6 : Bonus (+2 points)
########################################################################################################## 

def create_csv(metrics):
    """
    Fonction python dont l'objectif est d'enregister le dictionnaire "metrics" au sein de deux fichier csv appelés
    "F_metrics.csv" et "M_metrics.csv" respectivement pour les deux sexes.

    Paramètres
    ----------
    metrics : dictionnaire python (dict)
        Dictionnaire à 3 niveaux généré lors de la partie 5
    
    Résultats
    ---------
    paths_list : liste python (list)
        Liste contenant les chemins des deux fichiers "F_metrics.csv" et "M_metrics.csv"
    """
    paths_list = []

    f_metrics_path = "F_metrics.csv"
    m_metrics_path = "M_metrics.csv"

    # Hommes
    with open(m_metrics_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['stats', 'age', 'height', 'weight'])
        writer.writerow(['mean', round(metrics['M']['age']['mean'], 2), round(metrics['M']['height']['mean'], 2), round(metrics['M']['weight']['mean'], 2)])
        writer.writerow(['std', round(metrics['M']['age']['std'], 2), round(metrics['M']['height']['std'], 2), round(metrics['M']['weight']['std'], 2)])

    # Femmes
    with open(f_metrics_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['stats', 'age', 'height', 'weight'])
        writer.writerow(['mean', round(metrics['F']['age']['mean'], 2), round(metrics['F']['height']['mean'], 2), round(metrics['F']['weight']['mean'], 2)])
        writer.writerow(['std', round(metrics['F']['age']['std'], 2), round(metrics['F']['height']['std'], 2), round(metrics['F']['weight']['std'], 2)])
    
    paths_list.append(f_metrics_path)
    paths_list.append(m_metrics_path)

    # Fin du code

    return paths_list

########################################################################################################## 
# TESTS : Le code qui suit permet de tester les différentes parties 
########################################################################################################## 

if __name__ == '__main__':
    ######################
    # Tester la partie 1 #
    ######################

    # Initialisation de l'argument
    csv_path = "subjects.csv"

    # Utilisation de la fonction
    patients_dict = load_csv(csv_path)

    # Affichage du résultat
    print("Partie 1: \n\n",patients_dict['sub-tokyoIngenia04'], "\n")

    ######################
    # Tester la partie 2 #
    ######################

    # Initialisation des arguments
    csv_path1 = "subjects.csv"
    csv_path2 = "extra_subjects.csv"

    # Utilisation de la fonction
    patients_dict_multi = load_multiple_csv(csv_path1=csv_path1, csv_path2=csv_path2)

    # Affichage du résultat
    print("Partie 2: \n\n", patients_dict, "\n")

    ######################
    # Tester la partie 3 #
    ######################

    # Utilisation de la fonction
    new_patients_dict = update_convention(patients_dict)

    # Affichage du résultat
    print("Partie 3: \n\n", new_patients_dict, "\n")

    ######################
    # Tester la partie 4 #
    ######################

    # Utilisation de la fonction
    candicates_list = fetch_candidates(patients_dict)

    # Affichage du résultat
    print("Partie 4: \n\n", candicates_list, "\n")

    ######################
    # Tester la partie 5 #
    ######################

    # Utilisation de la fonction
    metrics = fetch_statistics(patients_dict)

    # Affichage du résultat
    print("Partie 5: \n\n", metrics, "\n")

    ######################
    # Tester la partie 6 #
    ######################

    # Initialisation des arguments
    dummy_metrics = {'M':{'age':{'mean':0,'std':0}, 'height':{'mean':0,'std':0}, 'weight':{'mean':0,'std':0}}, 
                     'F':{'age':{'mean':0,'std':0}, 'height':{'mean':0,'std':0}, 'weight':{'mean':0,'std':0}}}
    
    # Utilisation de la fonction
    paths_list = create_csv(metrics)

    # Affichage du résultat
    print("Partie 6: \n\n", paths_list, "\n")

