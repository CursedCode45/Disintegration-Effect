import os
import cv2
from Scripts.Settings import *
from Scripts.Particle import Particle
from Activator import Activator


path = 'C:/Users/Farmpy/Desktop/Learning/pics'



img = cv2.imread('../Loafy.png', cv2.IMREAD_UNCHANGED)
img2 = cv2.imread('../Loafy.png', cv2.IMREAD_UNCHANGED)

WIDTH = img.shape[1]
HEIGHT = img.shape[0]
particleSize = 2
particleNumberForX = int(WIDTH/particleSize)
particleNumberForY = int(HEIGHT/particleSize)

particles = []
# img[y][x]

activator = Activator(550)

# Divides the image into equal squares and each square is considered a particle
for y in range(0, particleNumberForY):
    for x in range(0, particleNumberForX):
        pixelArray = []
        for i in range(particleSize):
            for j in range(particleSize):
                pixelArray.append([[y*particleSize + i, x*particleSize + j], img[y*particleSize + i][x*particleSize + j]])
        particles.append(Particle(pixelArray))


def drawEachParticle():
    for particle in particles:
        for pixel in particle.allPixels:
            if 0 < pixel[0][0] < HEIGHT and 0 < pixel[0][1] < WIDTH:
                # Blending 2 pixels together with alpha values
                img2[pixel[0][0]][pixel[0][1]] = blendColorsWithAlphas(img2, pixel)


def removeOutOfScreenParticles():
    for particle in particles:
        if particle.isOutOfScreen(WIDTH, HEIGHT):
            particles.remove(particle)


def updateAllParticles():
    for particle in particles:
        particle.xCenter = 0
        particle.yCenter = 0
        particle.position[0] += particle.velocity[0]
        particle.position[1] += particle.velocity[1]
        # [y, x]
        for pixel in particle.allPixels:
            if 0 < pixel[0][0] < HEIGHT and 0 < pixel[0][1] < WIDTH:
                img2[pixel[0][0]][pixel[0][1]] = [255, 255, 255, 0]
            pixel[0][0] += int(particle.velocity[0])
            pixel[0][1] += int(particle.velocity[1])

            particle.xCenter += pixel[0][1]
            particle.yCenter += pixel[0][0]

        particle.xCenter /= len(particle.allPixels)
        particle.yCenter /= len(particle.allPixels)

        particle.velocity += particle.acceleration


for i in range(96, 1500):
    updateAllParticles()
    activator.checkParticlesInField(particles, 8, -0.66)
    removeOutOfScreenParticles()
    activator.moveActivator(2)
    drawEachParticle()
    cv2.imwrite(os.path.join(path, str(i)+'.png'), img2)

