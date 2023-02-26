from Scripts.Settings import *


class Particle:
    def __init__(self, pixelsArray):
        # This block of code gets the center coordinate of all pixels in the given pixel array
        self.xCenter = 0
        self.yCenter = 0
        self.allPixels = pixelsArray
        for pixel in self.allPixels:
            self.xCenter += pixel[0][1]
            self.yCenter += pixel[0][0]
        self.xCenter /= len(self.allPixels)
        self.yCenter /= len(self.allPixels)


        self.color = (255, 255, 255)
        # Position will be the average position from all pixels
        self.position = [self.xCenter, self.yCenter]
        self.velocity = [0, 0]
        self.acceleration = [0, 0]


        # This will be used to rotate pixels with the center as it's anchor point
        self.angle = 0
        self.radians = 0
        self.sin = 0
        self.cos = 1


        # It can only react once
        self.shouldReact = True



    # This function only returns accurate values with square particles
    def isOutOfScreen(self, WIDTH, HEIGHT):
        xMin, yMin, xMax, yMax = self.getBoundingBox()
        if xMin > WIDTH:
            return True
        if yMin > HEIGHT:
            return True
        if xMax < 0:
            return True
        if yMax < 0:
            return True
        return False


    def react(self, reactAmount, acceleration):
        if self.shouldReact:
            self.velocity = np.array([random.uniform(-reactAmount, reactAmount), random.uniform(-reactAmount, reactAmount)])
            self.acceleration = np.array([0, acceleration])
            self.shouldReact = False


    def getBoundingBox(self):
        xList = []
        yList = []
        for pixel in self.allPixels:
            xList.append(pixel[0][1])
            yList.append(pixel[0][0])

        return min(xList), min(yList), max(xList), max(yList)





