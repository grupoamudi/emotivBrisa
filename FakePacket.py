class FakePacket(object):
    def __init__(self,filename):
        arq = open(filename,'r')
        i = 0
        self.signals = {}
        self.time = 0
        self.gyroX = 0
        self.gyroY =0
        self.AF3=[0]
        self.F7=[0]
        self.F3=[0]
        self.FC5=[0]
        self.T7=[0]
        self.P7=[0]
        self.O1=[0]
        self.O2=[0]
        self.P8=[0]
        self.T8=[0]
        self.FC6=[0]
        self.F4=[0]
        self.F8=[0]
        self.AF4=[0]
        self.porcentagem = 0;
        for linha in arq:
            if i == 0:
                name = linha.split(';')[0]
            if i == 1:
                linha = linha.split(';')
                self.signals[name] = []
                for dado in linha:
                    if dado != '\n':
                        self.signals[name].append(int(dado))
                i = -1
            i = i + 1
    def dequeue(self):
        
        if (100*self.time/len(self.signals['gyroX'])) != self.porcentagem:
            print self.time*100/len(self.signals['gyroX']) 
            self.porcentagem = self.time*100/len(self.signals['gyroX'])
        self.gyroX = self.signals['gyroX'][self.time]
        self.gyroY = self.signals['gyroY'][self.time]
        self.AF3[0]= self.signals['AF3'][self.time]
        self.F7[0] = self.signals['F7'][self.time]
        self.F3[0] = self.signals['F3'][self.time]
        self.FC5[0]= self.signals['FC5'][self.time]
        self.T7[0] = self.signals['T7'][self.time]
        self.P7[0] = self.signals['P7'][self.time]
        self.O1[0] = self.signals['O1'][self.time]
        self.O2[0] = self.signals['O2'][self.time]
        self.P8[0] = self.signals['P8'][self.time]
        self.T8[0] = self.signals['T8'][self.time]
        self.FC6[0]= self.signals['FC6'][self.time]
        self.F4[0] = self.signals['F4'][self.time]
        self.F8[0] = self.signals['F8'][self.time]
        self.AF4[0]= self.signals['AF4'][self.time]
        self.time = self.time + 1

       
