import pygame 
import button

pygame.init()

SCREEN = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Lets Get Quizzical")

#game variables

game_paused = False

#define fonts
font = pygame.font.SysFont("arialblack", 40)

TEXT_COL = (255, 255, 255)

#load images
# 
menu_img = pygame.image.load("images/menu2.png").convert_alpha()

#create button instances
menu_button = button.Button(304, 125, menu_img, 1)

def draw_text(text, font, text_col, x, y):
    img  = font.render(text, True, text_col)
    SCREEN.blit(img, (x, y))

run = True
while run:

    SCREEN.fill((52, 78, 91))
    if game_paused == True:
        menu_button.draw(SCREEN)
        game_paused = False

    else:
        draw_text("Press Space to pause", font, TEXT_COL, 160, 250 )

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()
