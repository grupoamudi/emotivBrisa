import emotivPython.emotiv as emotiv
from pyGameGraph.GraphicManager import *
from emotivDetector import *
import gevent
import time

headset = emotiv.Emotiv() #emotiv
gevent.spawn(headset.setup) #emotiv
gevent.sleep(1) #emotiv
teste = GraphicManager()
teste.addGraphic('gyroX',50,0,1,0)
teste.addGraphic('gyroY',160,0,1,0)
teste.addGraphic('AF3',50,110,54,-150)
teste.addGraphic('F7',160,110,54,-150)
teste.addGraphic('F3',270,110,54,-150)
teste.addGraphic('FC5',380,110,54,-150)
teste.addGraphic('T7',50,220,54,-150)
teste.addGraphic('P7',160,220,54,-150)
teste.addGraphic('O1',270,220,54,-150)
teste.addGraphic('O2',380,220,54,-150)
teste.addGraphic('P8',50,330,54,-150)
teste.addGraphic('T8',160,330,54,-150)
teste.addGraphic('FC6',270,330,54,-150)
teste.addGraphic('F4',380,330,54,-150)
teste.addGraphic('F8',50,440,54,-150)
teste.addGraphic('AF4',160,440,54,-150)
start = time.clock()
ed = emotivDetector()
try:
  while True:
    packet = headset.dequeue() #para pegar do emotiv
    if (time.clock() - start) >= 0.0001:
        start = time.clock()
        #if ed.leftBlink(packet):
        #    print packet.F7[0]
        #    print 'LBLINK'
        teste.updateGraphic('gyroX',packet.gyroX)
        teste.updateGraphic('gyroY',packet.gyroY)
        teste.updateGraphic('AF3',packet.AF3[0])
        teste.updateGraphic('F7',packet.F7[0])
        teste.updateGraphic('F3',packet.F3[0])
        teste.updateGraphic('FC5',packet.FC5[0])
        teste.updateGraphic('T7',packet.T7[0])
        teste.updateGraphic('P7',packet.P7[0])
        teste.updateGraphic('O1',packet.O1[0])
        teste.updateGraphic('O2',packet.O2[0])
        teste.updateGraphic('P8',packet.P8[0])
        teste.updateGraphic('T8',packet.T8[0])
        teste.updateGraphic('FC6',packet.FC6[0])
        teste.updateGraphic('F4',packet.F4[0])
        teste.updateGraphic('F8',packet.F8[0])
        teste.updateGraphic('AF4',packet.AF4[0])
        teste.show()
except KeyboardInterrupt:
  headset.close()
finally:
  headset.close()
