import pygame
import math 

from game.constante import *

class Interface():

    def __init__(self, joueur, ecran):
        self.joueur = joueur
        # La gravité fait descendre 
        self.ecran = ecran

        self.image = pygame.image.load(
            "assets/sprites/joueur/joueur.png"
        )

        self.image = pygame.transform.scale(
            self.image,
            (30, 30)
        )
        pygame.font.init() 
        self.my_font = pygame.font.SysFont('calibri', 30)



  
    def update(self):
        for i in range(self.joueur.vie):
            self.ecran.blit(
                self.image,
                (50 + i * 50, 35)
            )
        text_surface = self.my_font.render(str(self.joueur.score), False, (0, 0, 0))
        self.ecran.blit(text_surface, (55,75))