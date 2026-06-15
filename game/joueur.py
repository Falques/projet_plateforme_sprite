import pygame

from game.constante import *

class Joueur(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load(
            "assets/sprites/joueur/joueur.png"
        )

        self.image = pygame.transform.scale(
            self.image,
            (96, 96)
        )

        self.rect = self.image.get_rect(
            topleft=(x, y)
        )

        self.vitesse = 5
        self.vitesse_y = 0

        self.gravite = 0.8
        self.force_saut = -15

        self.au_sol = False
        self.double_saut = False

        self.vie = 3
        self.vie_max = 3

        self.score = 0

  
    def update(self):

        self.vitesse_y += self.gravite
        self.rect.y += self.vitesse_y

        sol_y = HAUTEUR - MARGE_BAS 

        if self.rect.bottom >= sol_y:
            self.rect.bottom = sol_y
            self.vitesse_y = 0
            self.au_sol = True
            self.double_saut = True


    def gerer_entrees(self, touches): 
        if touches[pygame.K_LEFT] or touches[pygame.K_q]: 
            self.rect.x -= self.vitesse 
        if touches[pygame.K_RIGHT] or touches[pygame.K_d]: 
            self.rect.x += self.vitesse 
        if (touches[pygame.K_SPACE] or touches[pygame.K_UP]) and self.au_sol : 
            self.vitesse_y = self.force_saut 
            self.au_sol = False
        elif (touches[pygame.K_SPACE] or touches[pygame.K_UP]) and  self.double_saut and self.vitesse_y>0: 
            self.vitesse_y = self.force_saut
            self.double_saut = False