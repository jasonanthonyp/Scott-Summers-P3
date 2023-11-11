import pygame 

pygame.init()

SCREEN = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Lets Get Quizzical")

#define fonts
font = pygame.font.SysFont("arialblack", 40)

TEXT_COL = (255, 255, 255)

def draw_text(text, font, text_col, x, y):
    img  = font.render(text, True, text_col)
    SCREEN.blit(img, (x, y))

run = True
while run:
    SCREEN.fill((52, 78, 91))

    draw_text("Press Space to pause", font, TEXT_COL, 160, 250)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()
