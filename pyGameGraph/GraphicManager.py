import sys, pygame
from DataGraphic import *


class GraphicManager(object):
    def __init__(self):
        pygame.init()
        size = width, height = 1000, 768
        self.black = 0, 0, 0
        self.screen = pygame.display.set_mode(size)
        self.graphicsList = []
        self.graphicsListG = []
        self.graphicsDict = {}
        self.recordDict = {}
        self.recording = False

    def addGraphic(self, name, x, y, gain, offset):
        graphic = DataGraphic(100, 100, x, y, gain, offset, name)
        self.graphicsList.append(graphic)
        self.graphicsListG.append(graphic)
        self.graphicsDict[name] = graphic
        self.recordDict[name] = [] #Prepere the graphic to be possibili recorded

    def showGraphics(self):
        for graphic in self.graphicsList:
            graphic.showPoints(self.screen)

    def updateGraphic(self, name, value):
        self.graphicsDict[name].update(value)
        if self.recording:
            self.recordDict[name].append(value)
    
    def startRecording(self):
        #clean the recordDict
        for key in self.recordDict:
            self.recordDict[key] = []
        self.recording = True

    def stopRecording(self):
        self.recording = False
        arq = open('signals/teste.txt','w')
        for name in self.recordDict:
            arq.write(name + ';' + str(self.graphicsDict[name].length) + ';' +  str(self.graphicsDict[name].height) + ';' +  str(self.graphicsDict[name].x) +';' +  str(self.graphicsDict[name].y) + ';' +  str(self.graphicsDict[name].gain)+'\n')
            for value in self.recordDict[name]:
                arq.write(str(value)+';')
            arq.write('\n')
        arq.close()

    def show(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    if self.recording:
                        self.stopRecording()
                        print 'stopRecording'
                    else:
                        self.startRecording()
                        print 'startRecording'
                if event.key == pygame.K_g:
                    self.graphicsList = []
                    for graphic in self.graphicsListG:
                        graphic.length = 100
                        graphic.height = 100
                        graphic.x = graphic.xInit
                        graphic.y = graphic.yInit
                        graphic.initialShow = True
                        self.graphicsList.append(graphic)
                mods = pygame.key.get_mods()
                if mods & pygame.KMOD_SHIFT:
                    if event.key == pygame.K_0:
                        self.graphicsList = [self.graphicsListG[0]]
                        self.graphicBig()
                    if event.key == pygame.K_1:
                        self.graphicsList = [self.graphicsListG[1]]
                        self.graphicBig()

                    if event.key == pygame.K_2:
                        self.graphicsList = [self.graphicsListG[2]]
                        self.graphicBig()

                    if event.key == pygame.K_3:
                        self.graphicsList = [self.graphicsListG[3]]
                        self.graphicBig()

                    if event.key == pygame.K_4:
                        self.graphicsList = [self.graphicsListG[4]]
                        self.graphicBig()

                    if event.key == pygame.K_5:
                        self.graphicsList = [self.graphicsListG[5]]
                        self.graphicBig()

                    if event.key == pygame.K_6:
                        self.graphicsList = [self.graphicsListG[6]]
                        self.graphicBig()

                    if event.key == pygame.K_7:
                        self.graphicsList = [self.graphicsListG[7]]
                        self.graphicBig()

                    if event.key == pygame.K_8:
                        self.graphicsList = [self.graphicsListG[8]]
                        self.graphicBig()

                    if event.key == pygame.K_9:
                        self.graphicsList = [self.graphicsListG[9]]
                        self.graphicBig()

                    if event.key == pygame.K_a:
                        self.graphicsList = [self.graphicsListG[10]]
                        self.graphicBig()

                    if event.key == pygame.K_b:
                        self.graphicsList = [self.graphicsListG[11]]
                        self.graphicBig()

                    if event.key == pygame.K_c:
                        self.graphicsList = [self.graphicsListG[12]]
                        self.graphicBig()

                    if event.key == pygame.K_d:
                        self.graphicsList = [self.graphicsListG[13]]
                        self.graphicBig()

                    if event.key == pygame.K_e:
                        self.graphicsList = [self.graphicsListG[14]]
                        self.graphicBig()

                    if event.key == pygame.K_f:
                        self.graphicsList = [self.graphicsListG[15]]
                        self.graphicBig()

                    if event.key == pygame.K_g:
                        self.graphicsList = [self.graphicsListG[16]]
                        self.graphicBig()

                        
        self.screen.fill(self.black)
        self.showGraphics()
        pygame.display.flip()
    def graphicBig(self):
        self.graphicsList[0].length = 500
        self.graphicsList[0].x = 10
        self.graphicsList[0].y = 10
        self.graphicsList[0].height = 500
        self.graphicsList[0].initialShow = True

