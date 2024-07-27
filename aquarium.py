import pygame
import random

pygame.init()

# Розміри вікна
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("aquarium")

# Кольори
AQUA = (0, 0, 255)
LIME = (0, 255, 0)
CRIMSON = (255, 0, 0)
GOLD = (255, 215, 0)
CYAN = (0, 255, 255)

screen.fill(AQUA)

class Fish:
    def __init__(self, x, y, kind, color):
        self.x = x
        self.y = y
        self.kind = kind
        self.color = color
        self.velocity = random.uniform(1, 3)
        self.direction = random.choice([-1, 1])

    def update_position(self):
        self.x += self.velocity * self.direction
        if self.x > WINDOW_WIDTH or self.x < 0:
            self.direction *= -1

    def render(self, surface):
        pygame.draw.ellipse(surface, self.color, [self.x, self.y, 50, 20])

class Plant:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def render(self, surface):
        pygame.draw.rect(surface, LIME, [self.x, self.y, 20, 100])

def feed_all_fish(fish_list):
    for fish in fish_list:
        fish.velocity += 0.2

fish_varieties = [
    ("goldfish", GOLD),
    ("bluefish", CYAN),
    ("reffish", CRIMSON)
]

aquarium_fish = []
number_of_fish = random.randint(4, 8)
for _ in range(number_of_fish):
    kind, color = random.choice(fish_varieties)
    aquarium_fish.append(Fish(random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT), kind, color))

aquarium_plants = [
    Plant(100, WINDOW_HEIGHT - 100),
    Plant(300, WINDOW_HEIGHT - 100),
    Plant(500, WINDOW_HEIGHT - 100)
]

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                feed_all_fish(aquarium_fish)

    screen.fill(AQUA)

    for plant in aquarium_plants:
        plant.render(screen)

    for fish in aquarium_fish:
        fish.update_position()
        fish.render(screen)

    pygame.display.flip()
    pygame.time.delay(25)

pygame.quit()
