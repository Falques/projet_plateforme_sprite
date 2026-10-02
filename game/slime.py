import pygame

from game.ennemi import Ennemi


class Slime(Ennemi):

    def __init__(self, x, y):

        image = pygame.image.load(
            "assets/sprites/slime.png"
        ).convert_alpha()

        image = pygame.transform.scale(
            image,
            (64, 64)
        )

        super().__init__(
            x=x,
            y=y,
            image=image,
            vie=20
        )

        self.vitesse = 2

        self.direction = 1

        self.position_depart = x

        self.distance_patrouille = 150

    def patrouille(self):

        self.rect.x += self.vitesse * self.direction

        distance = self.rect.x - self.position_depart

        if distance > self.distance_patrouille:
            self.direction = -1

        elif distance < -self.distance_patrouille:
            self.direction = 1

    def update(self):

        self.patrouille()

        self.appliquer_gravite()

        self.collision_sol(500)