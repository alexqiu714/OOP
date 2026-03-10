import pygame
pygame.init()

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))

screen.fill("black")

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
    
c1 = cir("Blue", 250, 250, 1, 1)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            c1.draw()
        if event.type == pygame.MOUSEBUTTONUP:
            c1.big()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                screen.fill("black")
                c1.up()
            if event.key == pygame.K_DOWN:
                screen.fill("black")
                c1.down()
            if event.key == pygame.K_LEFT:
                screen.fill("black")
                c1.left()
            if event.key == pygame.K_RIGHT:
                screen.fill("black")
                c1.right()
    pygame.display.update()