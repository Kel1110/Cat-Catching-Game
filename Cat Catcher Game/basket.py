import pygame




# basket class
class Basket(pygame.sprite.Sprite):
   def __init__(self):
       super().__init__()
       self.image = pygame.image.load('basket.png')
       self.rect = self.image.get_rect()
       self.rect.x = 800 // 2
       self.rect.y = 600 - self.rect.height
      
# move the sprite left and right within the screen
   def update(self):
       keys = pygame.key.get_pressed()
       if keys[pygame.K_LEFT] and self.rect.x > 0:
           self.rect.x -= 5
       if keys[pygame.K_RIGHT] and self.rect.x < 800 - self.rect.width:
           self.rect.x += 5
