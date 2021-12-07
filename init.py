import pygame

x = pygame.init()
print(x)

# Creating window

gameWindow = pygame.display.set_mode((1200,500))
gamename = pygame.display.set_caption("First Game")

# Game specific variables

exit_game = False
game_over = False

# Creating a gaame loop

while not exit_game:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("RIGHT KEY")

pygame.quit()
quit()
