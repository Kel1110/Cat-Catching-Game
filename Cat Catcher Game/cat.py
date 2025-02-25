import pygame
import random




# falling cat class
class FallingCat(pygame.sprite.Sprite):
   def __init__(self):
       super().__init__()
       self.image = pygame.image.load("cat.png")
       self.rect = self.image.get_rect()
       self.rect.x = random.randint(0, 800 - self.rect.width)
       # loads the sprite in a random location on the top of the screen
       self.rect.y = -self.rect.height


   def update(self):
       self.rect.y += 5
       if self.rect.y > 600:
           self.kill() # removes the sprite
