class Cell():
    alive = False
    future = False
    neighbors = 0
    def __init__(self,alive):
        self.alive = alive

    def __str__(self):
        if self.alive:
            return 'x'
        else:
            return ' '