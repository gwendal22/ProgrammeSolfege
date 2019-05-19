#! /usr/bin/env python3

#// PROGRAMME ACCORDS REVISION SOLFEGE //
#
#Fonctions:
#    selection de la note de base
#    choix d'un accord (m5 / m6 /M5 /M6 / 7+ / 65- / +4 / 7-)
#    jeu de l'accord avec un module
#
#    Les 4 fonctions a la suite 20
#
#Fin du programme : on affiche les accords dans l'ordre.
import random
import time
#import pygame
#from pygame.locals import *
import music
from music.core import *
#T = music.tables
#H = music.utils.H

#Initialisation
#pygame.init()
#fenetre = pygame.display.set_mode((300,300))
#son = pygame.mixer.Sound("a3.mp3")
# Variables: 1 note = 1 nb entier

do =  1
do_diese = 2
re = 3
re_diese = 4
mi = 5
fa = 6
fa_diese = 7
sol = 8
sol_diese = 9
la = 10
la_diese = 11
si = 12
do2 = 13
do_diese2 = 14
re2 = 15
re_diese2 = 16
mi2 = 17
fa2 = 18
fa_diese2 = 19
sol2 = 20
sol_diese2 = 21
la2 = 22
la_diese2 = 23
si2 = 24
do3 = 25
#Variables: Accords
mineur_cinq = 1
mineur_six = 2
majeur_cinq = 3
majeur_six = 4
septieme_de_dominante = 5
six_cinq_barre = 6
quatre_plus = 7
sept_barre = 8
# Association note / nom de la note
note_nom = {do: "Do", do_diese: "Do #", re: "Re", re_diese: "Re #", mi: "Mi", fa: "Fa", fa_diese: "Fa #",
        sol: "Sol", sol_diese: "Sol #", la: "La", la_diese: "La #", si: "Si", do2: "Do Octavie",
        do_diese2: "Do # Octavie", re2:"Re Octavie", re_diese2:"Re # Octavie", mi2:"Mi Octavie",
        fa2:"Fa Octavie", fa_diese2:"Fa # Octavie", sol2:"Sol Octavie", sol_diese2:"Sol # Octavie",
        la2:"La Octavie", la_diese2:"La # Octavie", si2:"Si Octavie", do3:"Do Re-Octavie"}

note_numero = {do: 1,do_diese: 2, re: 3, re_diese: 4, mi: 5, fa: 6, fa_diese: 7, sol: 8, sol_diese: 9,
        la: 10, la_diese: 11, si: 12, do2: 13, do_diese2: 14, re2: 15, re_diese2: 16, mi2: 17,
        fa2: 18, fa_diese2: 19, sol2: 20, sol_diese2: 21, la2: 22, la_diese2: 23, si2: 24, do3: 25}

#Association accords
accords = {mineur_cinq: "Mineur Cinq", mineur_six: "Mineur Six", majeur_cinq: "Majeur Cinq", majeur_six: "Majeur Six", septieme_de_dominante: " Septieme de dominante", six_cinq_barre: " Six Cinq Barre", quatre_plus: "Plus Quatre", sept_barre: "Sept Barre"}
# Definition de note_basse

def choixNote():
    global note_basse
    note_basse = random.randint(1, 12)
    print("La note de basse est {0}".format(note_nom[note_basse]))
    return note_basse

def choixAccord():
    global accord_choisi
    accord_choisi = random.randint(1, 8)
    print("L'accord est {0}".format(accords[accord_choisi]))
    return accord_choisi

def defAccord(note_basse, accord_choisi):

    if accord_choisi == 1:
        note1 = note_basse + 3
        note2 = note_basse + 7
        print("{0} {1} {2}".format(note_nom[note_basse], note_nom[note1], note_nom[note2]))
    elif accord_choisi == 2:
        note1 = note_basse + 3
        note2 = note_basse + 8
        print("{0} {1} {2}".format(note_nom[note_basse], note_nom[note1], note_nom[note2]))
    elif accord_choisi == 3:
        note1 = note_basse + 4
        note2 = note_basse + 7
        print("{0} {1} {2}".format(note_nom[note_basse], note_nom[note1], note_nom[note2]))
    elif accord_choisi == 4:
        note1 = note_basse + 5
        note2 = note_basse + 8
        print("{0} {1} {2}".format(note_nom[note_basse], note_nom[note1], note_nom[note2]))
    elif accord_choisi == 5:
        note1 = note_basse + 3
        note2 = note_basse + 7
        note3 = note_basse + 10
        print("{0} {1} {2} {3}".format(note_nom[note_basse], note_nom[note1], note_nom[note2], note_nom[note3]))
    elif accord_choisi == 6:
        note1 = note_basse + 3
        note2 = note_basse + 6
        note3 = note_basse + 8
        print("{0} {1} {2} {3}".format(note_nom[note_basse], note_nom[note1], note_nom[note2], note_nom[note3]))
    elif accord_choisi == 7:
        note1 = note_basse + 2
        note2 = note_basse + 6
        note3 = note_basse + 9
        print("{0} {1} {2} {3}".format(note_nom[note_basse], note_nom[note1], note_nom[note2], note_nom[note3]))
    else:
        note1 = note_basse + 3
        note2 = note_basse + 6
        note3 = note_basse + 9
        print("{0} {1} {2} {3}".format(note_nom[note_basse], note_nom[note1], note_nom[note2], note_nom[note3]))
    if note1 > 24 or note2 > 24 or note_basse > 18:
        choixNote()
def jouerNote():
    pass

choixNote()
choixAccord()
defAccord(note_basse, accord_choisi)
