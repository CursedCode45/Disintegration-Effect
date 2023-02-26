from Scripts.Settings import *


class Activator:
    def __init__(self, x):
        self.color = (53, 250, 0)
        self.x = x


    def checkParticlesInField(self, particles, reactAmount, acceleration):
        for particle in particles:
            if particle.xCenter < self.x:
                particle.react(reactAmount, acceleration)


    def moveActivator(self, amount):
        self.x += amount


    def drawActivator(self, screen, HEIGHT):
        pg.draw.line(screen, self.color, (self.x, 0), (self.x, HEIGHT), width=3)

