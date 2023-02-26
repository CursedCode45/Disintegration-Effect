from Scripts.Settings import *


class Particle:
    def __init__(self, size, x, y):
        # This block of code gets the center coordinate of all pixels in the given pixel array
        self.x = x
        self.y = y
        self.size = size
        self.xCenter = (self.x + self.size)/2
        self.yCenter = (self.y + self.size)/2


        self.color = (0, random.randint(100, 255), random.randint(100, 255))
        # Position will be the average position from all pixels
        self.position = np.array([self.xCenter, self.yCenter], dtype="float64")
        self.velocity = np.array([0, 0], dtype="float64")
        self.acceleration = np.array([0, 0], dtype="float64")


        # This will be used to rotate pixels with the center as it's anchor point
        self.angle = 0
        self.radians = 0
        self.sin = 0
        self.cos = 1


        # It can only react once
        self.shouldReact = True



    # This function only returns accurate values with square particles
    def isOutOfScreen(self, WIDTH, HEIGHT):
        if self.position[0] > WIDTH:
            return True
        if self.position[1] > HEIGHT:
            return True
        if self.position[0] + self.size < 0:
            return True
        if self.position[1] + self.size < 0:
            return True
        return False


    def react(self, reactAmount, acceleration):
        if self.shouldReact:
            self.velocity = np.array([random.uniform(-reactAmount, reactAmount), random.uniform(-reactAmount, reactAmount)])
            self.acceleration = np.array([acceleration, 0])
            self.shouldReact = False

    def reactNoRandom(self, acceleration):
        if self.shouldReact:
            self.acceleration = np.array([acceleration, 0])
            self.shouldReact = False


    def moveParticle(self):
        self.position += self.velocity
        self.velocity += self.acceleration


    def drawParticle(self, screen):
        pg.draw.rect(screen, self.color, (self.position[0], self.position[1], self.size, self.size))


