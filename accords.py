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
import pygame
from pygame.locals import *
from pydub import AudioSegment
from pydub.playback import play
#your third audio file

# mixed = audio1.overlay(audio2)          #combine , superimpose audio files
# mixed1  = mixed.overlay(audio3)          #Further combine ,
# superimpose audio files
# #If you need to save mixed file
# mixed1.export("mixed.wav", format='wav') #export mixed  audio file
# play(mixed1)
do = 1
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
majeur_six = 2
majeur_cinq = 3
mineur_six = 4
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

note_numero = {do:AudioSegment.from_file("Notes/c3.mp3"),do_diese:AudioSegment.from_file("Notes/c-3.mp3"),
               re:AudioSegment.from_file("Notes/d3.mp3"), re_diese:AudioSegment.from_file("Notes/d-3.mp3"),
               mi:AudioSegment.from_file("Notes/e3.mp3"), fa:AudioSegment.from_file("Notes/f3.mp3"),
               fa_diese:AudioSegment.from_file("Notes/f-3.mp3"), sol:AudioSegment.from_file("Notes/g3.mp3"),
               sol_diese:AudioSegment.from_file("Notes/g-3.mp3"), la:AudioSegment.from_file("Notes/a3.mp3"),
               la_diese:AudioSegment.from_file("Notes/a-3.mp3"), si:AudioSegment.from_file("Notes/b3.mp3"),
               do2:AudioSegment.from_file("Notes/c4.mp3"), do_diese2:AudioSegment.from_file("Notes/c-4.mp3"),
               re2:AudioSegment.from_file("Notes/d4.mp3"), re_diese2:AudioSegment.from_file("Notes/d-4.mp3"),
               mi2:AudioSegment.from_file("Notes/e4.mp3"), fa2:AudioSegment.from_file("Notes/f4.mp3"),
               fa_diese2:AudioSegment.from_file("Notes/f-4.mp3"), sol2:AudioSegment.from_file("Notes/g4.mp3"),
               sol_diese2:AudioSegment.from_file("Notes/g-4.mp3"), la2:AudioSegment.from_file("Notes/a4.mp3"),
               la_diese2:AudioSegment.from_file("Notes/a-4.mp3"), si2:AudioSegment.from_file("Notes/b4.mp3"),
               do3:AudioSegment.from_file("Notes/c5.mp3")}

#Association accords
accords = {mineur_cinq: "Mineur Cinq", mineur_six: "Mineur Six", majeur_cinq: "Majeur Cinq", majeur_six: "Majeur Six", septieme_de_dominante: "Septieme de dominante", six_cinq_barre: "Six Cinq Barre", quatre_plus: "Plus Quatre", sept_barre: "Sept Barre"}
# Definition de note_basse

def choixNote():
    global note_basse
    note_basse = random.randint(1, 12)
    print("La note de basse est {0}".format(note_nom[note_basse]))
    return note_basse

def choixAccord():
    global accord_choisi
    accord_choisi = random.randint(1, 8)
    # print("L'accord est {0}".format(accords[accord_choisi]))
    return accord_choisi

def defAccord(note_basse, accord_choisi):
    duree = 1000
    if accord_choisi == 1:
        note1 = note_basse + 3
        note2 = note_basse + 7
        # print("{0} {1} {2}".format(note_nom[note_basse], note_nom[note1], note_nom[note2]))

        mixed1 = note_numero[note_basse].overlay(note_numero[note1])
        mixed2 = mixed1.overlay(note_numero[note2])
        play(mixed2)
    elif accord_choisi == 2:
        note1 = note_basse + 3
        note2 = note_basse + 8
        # print("{0} {1} {2}".format(note_nom[note_basse], note_nom[note1], note_nom[note2]))

        mixed1 = note_numero[note_basse].overlay(note_numero[note1])
        mixed2 = mixed1.overlay(note_numero[note2])
        mixed2.duration_seconds == duree
        play(mixed2)
    elif accord_choisi == 3:
        note1 = note_basse + 4
        note2 = note_basse + 7
        # print("{0} {1} {2}".format(note_nom[note_basse], note_nom[note1], note_nom[note2]))

        mixed1 = note_numero[note_basse].overlay(note_numero[note1])
        mixed2 = mixed1.overlay(note_numero[note2])
        mixed2.duration_seconds == duree
        play(mixed2)
    elif accord_choisi == 4:
        note1 = note_basse + 5
        note2 = note_basse + 8
        # print("{0} {1} {2}".format(note_nom[note_basse], note_nom[note1], note_nom[note2]))

        mixed1 = note_numero[note_basse].overlay(note_numero[note1])
        mixed2 = mixed1.overlay(note_numero[note2])
        mixed2.duration_seconds == duree
        play(mixed2)
    elif accord_choisi == 5:
        note1 = note_basse + 3
        note2 = note_basse + 7
        note3 = note_basse + 10
        # print("{0} {1} {2} {3}".format(note_nom[note_basse], note_nom[note1], note_nom[note2], note_nom[note3]))

        mixed1 = note_numero[note_basse].overlay(note_numero[note1])
        mixed2 = mixed1.overlay(note_numero[note2])
        mixed3 = mixed2.overlay(note_numero[note3])
        mixed3.duration_seconds == duree
        play(mixed3)
    elif accord_choisi == 6:
        note1 = note_basse + 3
        note2 = note_basse + 6
        note3 = note_basse + 8
        # print("{0} {1} {2} {3}".format(note_nom[note_basse], note_nom[note1], note_nom[note2], note_nom[note3]))

        mixed1 = note_numero[note_basse].overlay(note_numero[note1])
        mixed2 = mixed1.overlay(note_numero[note2])
        mixed3 = mixed2.overlay(note_numero[note3])
        mixed3.duration_seconds == duree
        play(mixed3)
    elif accord_choisi == 7:
        note1 = note_basse + 2
        note2 = note_basse + 6
        note3 = note_basse + 9
        # print("{0} {1} {2} {3}".format(note_nom[note_basse], note_nom[note1], note_nom[note2], note_nom[note3]))

        mixed1 = note_numero[note_basse].overlay(note_numero[note1])
        mixed2 = mixed1.overlay(note_numero[note2])
        mixed3 = mixed2.overlay(note_numero[note3])
        mixed3.duration_seconds == duree
        play(mixed3)
    else:
        note1 = note_basse + 3
        note2 = note_basse + 6
        note3 = note_basse + 9
        #print("{0} {1} {2} {3}".format(note_nom[note_basse], note_nom[note1], note_nom[note2], note_nom[note3]))

        mixed1 = note_numero[note_basse].overlay(note_numero[note1])
        mixed2 = mixed1.overlay(note_numero[note2])
        mixed3 = mixed2.overlay(note_numero[note3])
        mixed3.duration_seconds == duree
        play(mixed3)
    if note1 > 24 or note2 > 24 or note_basse > 18:
        choixNote()
#Initilasitation de PyGame
pygame.init()
#Creation de l'interface graphique
fenetre = pygame.display.set_mode((1200, 960), RESIZABLE)
pygame.display.set_caption('Programme Accords')

#Definition de l'image de fond
fond = pygame.image.load("Images/background.jpg").convert()
fenetre.blit(fond, (0,0))

#Definition du bouton Start
bouton_start = pygame.image.load("Images/Start.png").convert_alpha()
fenetre.blit(bouton_start, (600,90))
bouton_start = pygame.transform.scale(bouton_start, (250, 250))

#Definition des 6 boutons correspondants aux accords

# class Bouton(Size, Xlocation, Ylocation, File):
#     def __init__(self, Size, Xlocation, Ylocation, File):
#         self.apparence = pygame.image.load(File).convert_alpha()
#         fenetre.blit(self, (Xlocation, Ylocation))
#         self.size = pygame.transform.scale(self, (S, S))
#     def on_clicked(self):
#          return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())


S = 150

# Cinq:
bouton_cinq = pygame.image.load("Images/Cinq.png").convert_alpha()
fenetre.blit(bouton_cinq, (100,500))
bouton_cinq = pygame.transform.scale(bouton_cinq, (S, S))

# Six:
bouton_six = pygame.image.load("Images/Six.png").convert_alpha()
fenetre.blit(bouton_six, (300,500))
bouton_six = pygame.transform.scale(bouton_six, (S, S))

# Sept Plus:
bouton_sept_plus = pygame.image.load("Images/SeptPlus.png").convert_alpha()
fenetre.blit(bouton_sept_plus, (500,500))
bouton_sept_plus = pygame.transform.scale(bouton_sept_plus, (S, S))

# Six Cinq Barre:
bouton_six_cinq_barre = pygame.image.load("Images/SixCinqBarre.png").convert_alpha()
fenetre.blit(bouton_six_cinq_barre, (700,500))
bouton_six_cinq_barre = pygame.transform.scale(bouton_six_cinq_barre, (S, S))

# Plus Quatre:
bouton_plus_quatre = pygame.image.load("Images/PlusQuatre.png").convert_alpha()
fenetre.blit(bouton_plus_quatre, (900,500))
bouton_plus_quatre = pygame.transform.scale(bouton_plus_quatre, (S, S))

# Septieme de Dominante:
bouton_sept_barre = pygame.image.load("Images/SeptBarre.png").convert_alpha()
fenetre.blit(bouton_sept_barre, (1100,500))
bouton_sept_barre = pygame.transform.scale(bouton_sept_barre, (S, S))


#Rafraichissement de l'image de fond6
pygame.display.flip()

#Definition des couleurs
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
red = (255, 0, 0)

continuer = 1


# infinite loop
while True :

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get() :
        if event.type == KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("Start")

        # Quitter le programme
        if event.type == pygame.QUIT :

            # deactivates the pygame library
            pygame.quit()

            # quit the program.
            quit()

        # Draws the surface object to the screen.
            pygame.display.update()

    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    fenetre.blit(fond, (0,0))
    fenetre.blit(bouton_start, (500, 90))
    fenetre.blit(bouton_cinq, (100,500))
    fenetre.blit(bouton_six, (275,500))
    fenetre.blit(bouton_sept_plus, (450,500))
    fenetre.blit(bouton_six_cinq_barre, (625,500))
    fenetre.blit(bouton_plus_quatre, (800,500))
    fenetre.blit(bouton_sept_barre, (975,500))

    pygame.display.flip()

            # print("La dictée commence...")
            # i = 0
            # liste_accords = []
            # while i <= 20: # On repete 20 fois
            #     choixNote()
            #     choixAccord()
            #     defAccord(note_basse, accord_choisi)
            #     liste_accords.append(accords[accord_choisi])
            #     time.sleep(2)
            #     i += 1
            # print("La dictée est finie")
            # for accords_liste in liste_accords:
                #     print(accords_liste)
