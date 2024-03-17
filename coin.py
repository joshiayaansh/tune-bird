import pygame
class Coin: 
    def __init__(self):
        self.sprite = pygame.image.load('data/gfx/coin.webp')
        self.position = pygame.Vector2()
        self.position.xy