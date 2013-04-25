import sys, pygame

class DataGraphic(object):
    def setValues(self, values):
        i = 0
        for point in self.points:
            point[1][1] = self.y + self.height - values[i]*point[1][3]
            i = i + 1

    def showPoints(self, screen):
        i = 0 
        for point in self.points:
            point[1][0] = self.x + i*point[1][2] 
            screen.blit(point[0], point[1])
            i = i + 1
        if self.initialShow:
            self.points = []
            values = []
            for i in range(self.length):
                values.append(0)
                point = pygame.image.load("/home/berncs/Dropbox/Amudi/emotiv/script/pyGameGraph/green.png")
                self.points.append((point, point.get_rect()))
            self.setValues(values)
            self.grids = []
            for i in range(self.length+1):
                grid = pygame.image.load("/home/berncs/Dropbox/Amudi/emotiv/script/pyGameGraph/red.png")
                gridRect = grid.get_rect()
                gridRect[0] = self.x + i
                gridRect[1] = self.y + self.height + 1
                self.grids.append((grid,gridRect))
            for i in range(self.height+1):
                grid = pygame.image.load("/home/berncs/Dropbox/Amudi/emotiv/script/pyGameGraph/red.png")
                gridRect = grid.get_rect()
                gridRect[0] = self.x - 1
                gridRect[1] = self.y + i
                self.grids.append((grid,gridRect))
            self.initialShow = False
        for grid in self.grids:
            screen.blit(grid[0],grid[1])
        screen.blit(self.text, self.textRect)
         
    def update(self, value):
        self.points.append(self.points.pop(0)) #grab the first point and put it in the and
        self.points[-1][1][1] = self.y + self.height - (self.offset + value*self.points[-1][1][3]/self.gain) #set the last point (the one that was the first) to the new value
         
    def __init__(self, length, height, x, y, gain, offset, name): 
        self.length = length
        self.height = height
        self.gain = gain
        self.offset = offset
        self.x = x
        self.y = y
        self.xInit = x
        self.yInit = y
        self.points = []
        self.grids = []
        values = []
        self.initialShow = True
        for i in range(length):
            values.append(0)
            point = pygame.image.load("/home/berncs/Dropbox/Amudi/emotiv/script/pyGameGraph/green.png")
            self.points.append((point, point.get_rect()))
        self.setValues(values)
        font = pygame.font.Font(None, 16)
        self.text = font.render(name, 1, (255, 0, 0))
        self.textRect = self.text.get_rect()
        self.textRect[1] = self.y + (self.height/2) - self.textRect[3]/2
        self.textRect[0] = self.x - self.textRect[2] - 10
