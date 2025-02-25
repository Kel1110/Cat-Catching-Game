import pygame
import random
from basket import Basket
from cat import FallingCat






# initialize Pygame
pygame.init()
pygame.font.init()
font = pygame.font.SysFont("Comic Sans", 38)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch The Cat!")






# load images
starter_screen = pygame.image.load('intoscreen.jpeg')
bg_screen = pygame.image.load('background.jpeg')
lose_screen = pygame.image.load('endingscreen.jpeg')






# game variables
basket = Basket()
all_sprites = pygame.sprite.Group()
falling_cats = pygame.sprite.Group()
all_sprites.add(basket)
score = 0
game_over = False








# game loop
running = True
show_intro = True
while running:
 screen.blit(bg_screen, (0,0))






 if show_intro:
     score=0 #starting score is 0
     screen.blit(starter_screen,(0, 0)) # shows intro screen
     pygame.display.flip()
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running = False
         if event.type == pygame.KEYDOWN:
             show_intro = False
 elif game_over:
     screen.blit(lose_screen,(0,0)) # shows lose screen
     display_score = font.render(str(score), True, (0, 0, 0)) # displays score
     screen.blit(display_score,(450, 81))
     pygame.display.flip()
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running = False
         if event.type == pygame.KEYDOWN: # restarts game when a key is pressed
             game_over = False
             score = 0
             all_sprites.empty()
             falling_cats.empty()
             basket = Basket()




             all_sprites.add(basket)
 else:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running = False




     if random.randint(1, 30) == 1:
         falling_cat = FallingCat()
         all_sprites.add(falling_cat)
         falling_cats.add(falling_cat)




   
     all_sprites.update()








     hits = pygame.sprite.spritecollide(basket, falling_cats, True)
     if hits:
         score += 1








     for obj in falling_cats:
         if obj.rect.y > 550: # game is over if cat falls out of the screen
             game_over = True




     all_sprites.draw(screen)
     display_score = font.render(f"score: {score}", True, (0, 0, 0))
     screen.blit(display_score,(10, 100))
     pygame.display.flip()
     pygame.time.Clock().tick(60)








pygame.quit()