import pygame
import math 
from game.constante import *


class Fleche(pygame.sprite.Sprite):

    def __init__(self, x_depart, y_depart, x_cible, y_cible, duree = 1 ):
        super().__init__()
        self.x_depart = x_depart
        # La gravité fait descendre 
        self.gravite = 0.1 
        # le frotement ralentie
        self.frotement = 0.99

        self.force = max(min(duree, 3), 0.5)

        self.image = pygame.image.load(
            "assets/sprites/skill/tir-a-larc.png"
        )

        self.image = pygame.transform.scale(
            self.image,
            (30, 30)
        )
        # Fleche pointée vers la droite 
        self.image = pygame.transform.rotate(self.image, -45)
        if x_cible > x_depart : 
            self.image_origine = self.image
        else : 
            self.image_origine = pygame.transform.rotate(self.image, 180)

        self.rect = self.image.get_rect(center=(x_depart, y_depart))


        #Calcul d'un vecteur de direction  
        dx = x_cible - x_depart
        dy = y_cible - y_depart



        # Calcul puissance en fonction de la distance 
        #fraction = 100
        #dx = dx /fraction 
        #dy = dy /fraction 
        # Standadisation distance vitesse 
        distance = math.sqrt(dx**2 + dy**2)

        dx /= distance 
        dy /= distance

    

        self.vx = dx * 10 * self.force
        self.vy = dy * 10 * self.force


  
    def update(self):
        # Modification vecteur de direction
        self.vy += self.gravite
        self.vx *= self.frotement

        self.rect.x += self.vx
        self.rect.y += self.vy

        # Dans un triangle rectangle alpha = arctan(a/b) puis on convertie de radiant a degree
        angle = math.atan(self.vy/ self.vx) 
        angle = angle * 180 / math.pi
        
        angle = -1 * angle
        self.image = pygame.transform.rotate(self.image_origine, angle)


        # Suppression si hors écran
        if (
            self.rect.right < 0
            or self.rect.left > LARGEUR
            or self.rect.bottom < 0
            or self.rect.top > HAUTEUR-MARGE_BAS
        ):
            self.kill()