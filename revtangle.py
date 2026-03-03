import pygame
pygame.init()

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))

screen.fill("black")

class re():
    def __init__(self, x, y, w, h, t):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.t = t

    def draw(self):
        pygame.draw.rect(screen, "blue", (self.x, self.y, self.w, self.h), self.t)

r1 = re(20, 230, 160, 80, 0)

r1.draw()

r2 = re(400, 50, 80, 160, 100)

r2.draw()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()