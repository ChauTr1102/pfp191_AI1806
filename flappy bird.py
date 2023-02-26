import pygame
import random

# Initialize Pygame
pygame.init()

# Set the width and height of the screen
SCREEN_WIDTH = 288
SCREEN_HEIGHT = 512
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load images
background_image = pygame.image.load("background.png").convert()
base_image = pygame.image.load("base.png").convert()
bird_image = pygame.image.load("bird.png").convert_alpha()
pipe_image = pygame.image.load("pipe.png").convert_alpha()

# Define constants
GRAVITY = 0.25
BIRD_SPEED = -6
PIPE_SPEED = -3
PIPE_GAP = 100
PIPE_FREQUENCY = 100


# Define classes
class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = bird_image
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = SCREEN_HEIGHT / 2
        self.velocity = 0

    def update(self):
        self.velocity += GRAVITY
        self.rect.y += self.velocity

    def jump(self):
        self.velocity = BIRD_SPEED


class Pipe(pygame.sprite.Sprite):
    def __init__(self, height):
        super().__init__()
        self.image = pipe_image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = height

    def update(self):
        self.rect.x += PIPE_SPEED


# Create game objects
bird = Bird()
pipes = pygame.sprite.Group()
score = 0

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()

    # Update game objects
    bird.update()

    # Spawn new pipes
    if score % PIPE_FREQUENCY == 0:
        top_height = random.randint(50, 250)
        bottom_height = top_height + PIPE_GAP
        top_pipe = Pipe(top_height - pipe_image.get_height())
        bottom_pipe = Pipe(bottom_height)
        pipes.add(top_pipe)
        pipes.add(bottom_pipe)
    score += 1

    # Update pipes
    for pipe in pipes:
        pipe.update()
        if pipe.rect.right < 0:
            pipes.remove(pipe)
        elif bird.rect.colliderect(pipe.rect):
            running = False

    # Draw game objects
    screen.blit(background_image, (0, 0))
    pipes.draw(screen)
    screen.blit(base_image, (0, SCREEN_HEIGHT - base_image.get_height()))
    screen.blit(bird.image, bird.rect)
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
