from cell import * 
from random import *
from os import system

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
                self.gosper_glider_gun()

    def gosper_glider_gun(self):
        pos = self.array
        pos[5][1].alive = True
        pos[6][1].alive = True
        pos[5][2].alive = True
        pos[6][2].alive = True
        
        pos[5][11].alive = True
        pos[6][11].alive = True
        pos[7][11].alive = True
        pos[4][12].alive = True
        pos[8][12].alive = True
        pos[3][13].alive = True
        pos[9][13].alive = True
        pos[3][14].alive = True
        pos[9][14].alive = True
        pos[6][15].alive = True
        pos[4][16].alive = True
        pos[8][16].alive = True
        pos[5][17].alive = True
        pos[6][17].alive = True
        pos[7][17].alive = True
        pos[6][18].alive = True

        pos[3][21].alive = True
        pos[4][21].alive = True
        pos[5][21].alive = True
        pos[3][22].alive = True
        pos[4][22].alive = True
        pos[5][22].alive = True
        pos[2][23].alive = True
        pos[6][23].alive = True

        pos[1][25].alive = True
        pos[2][25].alive = True
        pos[6][25].alive = True
        pos[7][25].alive = True

        pos[3][35].alive = True
        pos[4][35].alive = True
        pos[3][36].alive = True
        pos[4][36].alive = True

    def draw(self):
        system('clear')
        for x in xrange(self.size):
            for y in xrange(self.size):
                print self.array[x][y],
            print

    def calc(self):
        for x in xrange(self.size):
            for y in xrange(self.size):
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
                if current.neighbors == 3:
                    current.future = True

    def update(self):
        for x in xrange(self.size):
            for y in xrange(self.size):
                self.array[x][y].alive = self.array[x][y].future
                self.array[x][y].neighbors = 0
