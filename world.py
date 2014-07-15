from cell import * 
from random import *
from os import system
from patterns import *

class World():

    array = []
    size = 0

    def __init__(self, size, pattern="none"):
        self.size = size
        for x in xrange(size):
                self.array.append([])

        if pattern == "none":
            for x in xrange(size):
                for y in xrange(size):
                    self.array[x].append(Cell(randint(0,1)))
        else:
            for x in xrange(size):
                for y in xrange(size):
                    self.array[x].append(Cell(False))
            if pattern == "ggg":
                gosper_glider_gun(self.array)
            elif pattern == "glider":
                glider(self.array)

    def draw(self):        
        system('clear')
        for x in xrange(self.size):
            for y in xrange(self.size):
                print self.array[x][y],
            print

    def calc(self):
        for y in xrange(self.size):
            for x in xrange(self.size):
                current = self.array[x][y]
                if x > 0:
                    if y > 0:
                        if self.array[x-1][y-1].alive:
                            current.neighbors += 1
                    if self.array[x-1][y].alive:
                        current.neighbors += 1
                    if y < self.size - 1:
                        if self.array[x-1][y+1].alive:
                            current.neighbors += 1
                if y > 0:
                    if self.array[x][y-1].alive:
                        current.neighbors += 1
                if y < self.size - 1:    
                    if self.array[x][y+1].alive:
                        current.neighbors += 1
                if x < self.size - 1:
                    if y > 0:
                        if self.array[x+1][y-1].alive:
                            current.neighbors += 1
                    if self.array[x+1][y].alive:
                        current.neighbors += 1
                    if y < self.size - 1:
                        if self.array[x+1][y+1].alive:
                            current.neighbors += 1
                
                if current.neighbors > 3:
                    current.future = False
                if current.neighbors < 2:
                    current.future = False
                if current.neighbors == 2:
                    current.future = current.alive
                if current.neighbors == 3:
                    current.future = True

    def update(self):
        for x in xrange(self.size):
            for y in xrange(self.size):
                self.array[x][y].alive = self.array[x][y].future
                self.array[x][y].neighbors = 0
