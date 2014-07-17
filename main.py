from world import *
from time import sleep
import sys

pattern = "none"
size = 40
frequence = 0.12 
interactive = False

if len(sys.argv) > 1:
    for i in xrange(len(sys.argv)):
        if sys.argv[i] == "-p":
            pattern = sys.argv[i+1]
        if sys.argv[i] == "-s":
            size = sys.argv[i+1]
        if sys.argv[i] == "-f":
            frequence = float(sys.argv[i+1])
        if sys.argv[i] == "-i":
            interactive = True


world = World(size,pattern)
world.draw()
raw_input()

while 1:
    world.calc()
    world.update()
    world.draw()
    if interactive:
        raw_input()
    else:
        sleep(frequence)