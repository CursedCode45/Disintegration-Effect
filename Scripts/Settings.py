import pygame as pg
import numpy as np
import math
import random


def getDistance(p1, p2):
    dist = np.linalg.norm(p1-p2)
    return dist


def blendColorsWithAlphas(img, pixel):
    alpha_previous_pixel = img[pixel[0][0]][pixel[0][1]][3] / 255
    alpha_new_pixel = pixel[1][3] / 255
    alpha_final_pixel = min(255, (alpha_previous_pixel + alpha_new_pixel - alpha_previous_pixel * alpha_new_pixel) * 255)
    red = alpha_previous_pixel * img[pixel[0][0]][pixel[0][1]][2] + (1 - alpha_previous_pixel) * alpha_new_pixel * pixel[1][2]
    green = alpha_previous_pixel * img[pixel[0][0]][pixel[0][1]][1] + (1 - alpha_previous_pixel) * alpha_new_pixel * pixel[1][1]
    blue = alpha_previous_pixel * img[pixel[0][0]][pixel[0][1]][0] + (1 - alpha_previous_pixel) * alpha_new_pixel * pixel[1][0]
    return blue, green, red, alpha_final_pixel

