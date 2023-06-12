import asyncio
import pygame
import random

pygame.init()

async def main():
    screen_width = 500
    screen_height = 750

    # Set screen size
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    # Background image
    background_image = pygame.image.load('background.jpg')

    # Bird properties
    BIRD_IMAGE = pygame.image.load('bird.png')
    bird_width = 50
    bird_height = 300
    bird_position = 0

    # Obstacle properties
    obstacle_width = 70
    obstacle_height = random.randint(150, 450)
    obstacle_color = (211, 253, 117)
    obstacle_movement = -4
    obstacle_position = 500


    # Display bird on the screen
    def display_bird(x, y):
        screen.blit(BIRD_IMAGE, (x, y))

    # Display obstacles on the screen
    def display_obstacle(height):
        pygame.draw.rect(screen, obstacle_color, (obstacle_position, 0, obstacle_width, height))
        obstacle_bottom_height = 635 - height - 150
        pygame.draw.rect(screen, obstacle_color, (obstacle_position, 635, obstacle_width, -obstacle_bottom_height))

    # Detect collision between bird and obstacle
    def detect_collision(obstacle_position, obstacle_height, bird_height, obstacle_bottom_height):
        if obstacle_position >= 50 and obstacle_position <= (50 + 64):
            if bird_height <= obstacle_height or bird_height >= (obstacle_bottom_height - 64):
                return True
        return False

    game_running = True
    collision = False
    menu = True
    font = pygame.font.Font('freesansbold.ttf', 32)

    while game_running:
        screen.fill((0, 0, 0))
        clock.tick(60)
        screen.blit(background_image, (0, 0))

        while menu:
            if collision == False:
                start_message = font.render("Press space to start!", True, (200, 35, 35))
                screen.blit(start_message, (90, 300))
                pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        menu = False

                if event.type == pygame.QUIT:
                    menu = False
                    game_running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_position = -6
                    menu = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    bird_position = 3

        bird_height += bird_position
        if bird_height <= 0:
            bird_height = 0
        if bird_height >= 571:
            bird_height = 571

        obstacle_position += obstacle_movement
        collision = detect_collision(obstacle_position, obstacle_height, bird_height, obstacle_height + 150)

        if collision:
            game_running = False

        if obstacle_position <= -10:
            obstacle_position = 500
            obstacle_height = random.randint(200, 400)
        display_obstacle(obstacle_height)

        display_bird(bird_width, bird_height)
        pygame.display.update()
        await asyncio.sleep(0)
        
asyncio.run(main())
# pygame.quit()