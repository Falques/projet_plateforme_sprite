import pygame
from game.joueur import Joueur
from game.fleche import Fleche
from game.interface import Interface
from game.constante import *

class Game:
    def __init__(self):
        pygame.init()
        self.ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
        pygame.display.set_caption("Jeu de plateforme")
        self.horloge = pygame.time.Clock()
        self.running = True

        # Création du joueur et de l'interface
        self.joueur = Joueur(100, 400)
        self.interface = Interface(self.joueur, self.ecran)
        
        # Création des groupes de sprites
        self.groupe_joueurs = pygame.sprite.Group()
        self.groupe_joueurs.add(self.joueur)
        
        self.groupe_projectile_joueur = pygame.sprite.Group()
        
        # Variables pour la gestion du clic long
        self.temps_debut_clic = None


        # Les cooldowns 
        self.cooldown = {
            'fleche' : 0
        }
    def gerer_evenements(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.temps_debut_clic = pygame.time.get_ticks()
            if self.cooldown['fleche'] == 0 :
                if event.type == pygame.MOUSEBUTTONUP:
                    souris_x, souris_y = pygame.mouse.get_pos()
                    if self.temps_debut_clic is not None:
                        duree = (pygame.time.get_ticks() - self.temps_debut_clic) / 1000
                        self.temps_debut_clic = None
                    else:
                        duree = 1
                    
                    fleche = Fleche(
                        self.joueur.rect.centerx,
                        self.joueur.rect.centery,
                        souris_x,
                        souris_y,
                        duree
                    )
                    self.groupe_projectile_joueur.add(fleche)
                    self.cooldown['fleche'] = 60

    def gerer_entrées_clavier(self):
        touches = pygame.key.get_pressed()
        self.joueur.gerer_entrees(touches)

    def gerer_cooldown(self):
        self.cooldown['fleche'] = max(self.cooldown['fleche']-1 ,0)

    def update(self):
        self.joueur.update()
        self.groupe_projectile_joueur.update()

    def dessiner(self):
        self.ecran.fill((135, 206, 235))
        pygame.draw.rect(self.ecran, (50, 180, 50), (0, HAUTEUR-MARGE_BAS, LARGEUR, 100))
        
        self.groupe_joueurs.draw(self.ecran)
        self.groupe_projectile_joueur.draw(self.ecran)
        
        self.interface.update()


        pygame.display.flip() 



        

    def lancer(self):
        while self.running:
            dt = self.horloge.tick(FPS)
            self.gerer_cooldown()
            self.gerer_evenements()
            self.gerer_entrées_clavier()
            self.update()
            self.dessiner()

        pygame.quit()