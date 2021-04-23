#! /usr/bin/python3
#
import random
from numpy import *
from set import w, h, debug
from color import color
from screen import screen_array
from randomColor import RandomColor

screen_array = screen_array()

randomColor = RandomColor(screen_array)


if debug == True:
    print(type(w))
    print(type(h))
    print(random.randint(0, 3), random.randint(0, 3), random.randint(0, 3))
    input()


def draw():
    for x in range(w):
#        print("x:{}".format(x))
        for y in  range(h):
#            print("y:{}".format(y))
            print(screen_array[y][x], end='')
#        print('\n1')

randomColor.randomOneColorFill(16, 8, 24, 16, types='one_ang')

draw()

if debug == True:
    r = int(input())
    g = int(input())
    b = int(input())
    print(color(r, g, b))
