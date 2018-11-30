import pygame
import random

WIDTH = 800
HEIGHT = 600
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Player(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1, 1))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        self.directionX = random.randint(-10, 10)
        self.directionY = random.randint(-10, 10)

    def update(self):
        # any code here will happen every time the game loop updates
        self.rect.x += self.directionX
        self.rect.y += self.directionY
        if self.rect.left < 0:
            self.directionX = random.randint(0, 10)
        if self.rect.right > WIDTH:
            self.directionX = random.randint(-10, 0)
        if self.rect.top < 0:
            self.directionY = random.randint(0, 10)
        if self.rect.bottom > HEIGHT:
            self.directionY = random.randint(-10, 0)


# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("点和线")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
all_sprites_arr = []

for i in range(10):
    player = Player()
    all_sprites.add(player)
    all_sprites_arr.append(player)

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)

    for player in all_sprites_arr:
        for player2 in all_sprites_arr:
            pygame.draw.aaline(screen, GREEN, (player.rect.x, player.rect.y),
                               (player2.rect.x, player2.rect.y))

    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
