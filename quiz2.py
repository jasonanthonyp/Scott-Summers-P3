import pygame
import sys

pygame.init()

SCREEN = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Lets Get Quizzical")

BG_COLOR = "#0a092d"
FLASHCARD_COLOR = "#2e3856"
FLIPPED_COLOR = "#595e6d"
FONT = pygame.font.SysFont("Arial", 30)

SCREEN.fill(BG_COLOR) 

quiz_data = {
    "Best Actor for \"The Revenant\"": "Leonardo DiCaprio",
    "Best Actress for \"Everything Everywhere All At Once\"": "Michelle Yeoh",
    "2012 Best Picture starring Ben Affleck ": "Argo",
    "Best Actor for \"Lincoln\"": "Daniel Day-Lewis",
    "Best Actress for \"The Iron Lady\"": "Meryl Streep",
    "Best Actress for \"La Vie En Rose\"": "Marion Cotillard",
    "Best Actress winner Charlize Theron for this movie": "Monster",
    "Moonlight wins best picture over this Emma Stone film": "LaLa Land",
    "The second actor to win the oscar for playing The Joker": "Joaquin Phoenix",
    "2019 South Korean black comedy wins best picture": "Parasite"
}

current_question = ""
current_answer = ""

card_turned = False

index = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                card_turned = not card_turned
            elif pygame.key.get_pressed()[pygame.K_RIGHT] and index < len(quiz_data) - 1:
                index += 1
                card_turned = False
            elif pygame.key.get_pressed()[pygame.K_LEFT] and index > 0:
                index -= 1
                card_turned = False
    
    current_question = list(quiz_data)[index]
    current_answer = list(quiz_data.values())[index]
    current_question_object = FONT.render(current_question, True, "white")
    current_question_rect = current_question_object.get_rect(center=(400, 400))
    current_answer_object = FONT.render(current_answer, True, "white")
    current_answer_rect = current_answer_object.get_rect(center=(400, 400))
    current_index_object = FONT.render(f"{index+1}/{len(quiz_data)}", True, "white")
    current_index_rect = current_index_object.get_rect(center=(400, 600))
    
    if not card_turned:
        SCREEN.fill(BG_COLOR)
        pygame.draw.rect(SCREEN, FLASHCARD_COLOR, (150, 250, 500, 300))
        SCREEN.blit(current_question_object, current_question_rect)
    else:
        SCREEN.fill(BG_COLOR)
        pygame.draw.rect(SCREEN, FLIPPED_COLOR, (150, 250, 500, 300))
        SCREEN.blit(current_answer_object, current_answer_rect)
    
    SCREEN.blit(current_index_object, current_index_rect)
    
    pygame.display.update()
