import pygame


class Ennemi(pygame.sprite.Sprite):

    def __init__(self, x, y, image, vie=10):

        super().__init__()

        self.image = image
        self.rect = self.image.get_rect(
            topleft=(x, y)
        )

        # Déplacement
        self.vitesse_x = 0
        self.vitesse_y = 0

        # Physique
        self.gravite = 0.8

        # Statistiques
        self.vie = vie
        self.vivant = True

        # Direction
        self.direction = 1

    def subir_degats(self, degats):

        self.vie -= degats

        if self.vie <= 0:
            self.mourir()

    def mourir(self):

        self.vivant = False
        self.kill()

    def appliquer_gravite(self):

        self.vitesse_y += self.gravite
        self.rect.y += self.vitesse_y

    def collision_sol(self, sol_y):

        if self.rect.bottom >= sol_y:
            self.rect.bottom = sol_y
            self.vitesse_y = 0

    def update(self):

        """
        Méthode générique.
        Sera redéfinie dans les classes filles.
        """
        pass