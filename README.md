# TP2: Gestion de base de données d'un hôpital

## Directives

⏰ Date de remise : 

📬 À remettre sur Moodle

## Objectifs

L'objectif de ce travail pratique est d'apprendre à manipuler une base de données en utilisant Python. Ce TP vous permettra de découvrir et de maîtriser :  

- Les structures de contrôle, telles que les structures conditionnelles ('if', 'else', etc.) et les structures de répétition ('for', 'while', etc.)  
- Les différentes structures de données, comme les listes, les dictionnaires, et les tuples.
- Le module python `csv` permettant d'ouvrir et d'enregister des fichiers csv.

Ces notions seront explorées à travers différentes parties présentant chacunes différentes utilisations pratiques.

## Introduction

Vous avez récemment été engagé par un hôpital pour gérer plusieurs bases de données dont la liste des patients ayant donné leur consentement pour participer à une recherche en IRM. Cette base de données, accessible dans le fichier `subjects.csv`, contient les informations suivantes:
- `participant_id`: identifiant unique associé au patient
- `age`: âge du patient
- `sex`: sexe bilogique du patient
- `height`: taille du patient (cm)
- `weight`: masse du patient (kg)
- `date_of_scan`: date de scan (YYYY-MM-DD)
- `pathology`: pathologie
  - HC: Healthy Control (patient sain)
  - DCM: Degenerative Cervical Myelopathy (myelopathie cervicale degenerative)
  - MildCompression: Mild Spinal Cord Copression (compression moyenne de la moelle épinière)

## Instructions

### Partie 1
