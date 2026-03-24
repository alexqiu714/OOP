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

class cir():
    def __init__(self, c, x, y, r, t):
        self.c = c
        self.x = x
        self.y = y
        self.r = r
        self.t = t
    def draw(self):
        pygame.draw.circle(screen, self.c, (self.x, self.y), self.r, self.t)
    def big(self):
        self.r += 1
        pygame.draw.circle(screen, self.c, (self.x, self.y), self.r, self.t)
    def up(self):
        self.y -= 5
        pygame.draw.circle(screen, self.c, (self.x, self.y), self.r, self.t)
    def down(self):
        self.y += 5
        pygame.draw.circle(screen, self.c, (self.x, self.y), self.r, self.t)
    def left(self):
        self.x -= 5
        pygame.draw.circle(screen, self.c, (self.x, self.y), self.r, self.t)
    def right(self):
        self.x += 5
        pygame.draw.circle(screen, self.c, (self.x, self.y), self.r, self.t)

r1 = re(20, 230, 160, 80, 0)

c1 = cir("Yellow", 250, 250, 30, 1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                r1.draw()
            if event.key == pygame.K_RIGHT:
                c1.draw()
    pygame.display.update()