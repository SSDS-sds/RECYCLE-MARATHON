import pygame, random, time
from pygame.locals import *

pygame.init()
WIDTH = 900
HEIGHT = 700
CENTRE_X = WIDTH/2
CENTRE_Y = HEIGHT/2

pygame.display.set_caption("RECYCLE MARATHON")

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Change background
def change_background(img):
    bg = pygame.image.load(img)
    bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
    SCREEN.blit(bg, (0,0))

# Bin class
class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load("bin.png")
        self.image = pygame.transform.scale(self.img, (40,60))
        self.rect = self.image.get_rect()

# Recycle class
class Recycle(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.img = pygame.image.load(img)
        self.image = pygame.transform.scale(self.img, (30,30))
        self.rect = self.image.get_rect()

# Non-recyclable class
class Non_recyclable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load("plastic.png")
        self.image = pygame.transform.scale(self.img, (40,40))
        self.rect = self.image.get_rect()

images = ["item1.png", "item2.png", "item3.png"]

# Create the sprite groups
items_group = pygame.sprite.Group()
plastic_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

# Item sprites
for i in range(50):
    item = Recycle(random.choice(images))
    item.rect.x = random.randrange(WIDTH)
    item.rect.x = random.randrange(HEIGHT)
    items_group.add(item)
    all_sprites.add(item)

# Create plastic
for i in range(20):
    plastic = Non_recyclable()
    plastic.rect.x = random.randrange(WIDTH)
    plastic.rect.y = random.randrange(HEIGHT)
    plastic_group.add(plastic)
    all_sprites.add(plastic)

# Bin sprite
bin = Bin()
all_sprites.add(bin)

# Game variables 
score = 0
clock = pygame.time.Clock()
start_time = time.time()
font = pygame.font.SysFont("Fantasy", 22)
score_txt = font.render(f"Score: {score}", True, "#3F15A8")

running = True
# Main game loop
while running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()

    time_elapsed = time.time() - start_time
    if time_elapsed >= 60:
        if score >= 50:
            change_background("win_screen.jpg")
        else:
            change_background("losing_screen.jpg")
    else:
        change_background("bg.png")
        count_down = font.render(f"Time left: {60 - time_elapsed}", True, "#96DEC8")
        SCREEN.blit(count_down, (20,10))
