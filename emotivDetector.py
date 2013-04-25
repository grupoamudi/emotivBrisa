class emotivDetector(object):
    def leftBlink(self,packet):
        if packet.F7[0] > 10000 and packet.F8[0] < 10000 and packet.FC5[0] < 10000: 
            return True
        else:
            return False
         
