from Scripts.Settings import *
from Scripts.Activator import Activator
from GameParticle import Particle
import os


pg.init()

WIDTH = 1920
HEIGHT = 1080
FPS = 60
TITLE = "Particle Simulation"

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 0)
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(TITLE)

clock = pg.time.Clock()

particleSize = 15
particleNumberX = 65
particleNumberY = 50
xStart = 1800
yStart = 650

particles = []

activator = Activator(0)

for y in range(0, particleNumberY):
    for x in range(0, particleNumberX):
        particles.append(Particle(particleSize, x*particleSize+xStart, y*particleSize+yStart))


running = True
while running:
    clock.tick(FPS)
    screen.fill(0)
    mouse = pg.mouse.get_pos()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                running = False

    activator.drawActivator(screen, HEIGHT)
    activator.moveActivator(2)


    for particle in particles:
        if particle.isOutOfScreen(WIDTH, HEIGHT):
            particles.remove(particle)
        if particle.xCenter < activator.x:
            particle.react(5, -0.5)
            #particle.reactNoRandom(-0.5)

        particle.moveParticle()
        particle.drawParticle(screen)

    pg.display.update()
