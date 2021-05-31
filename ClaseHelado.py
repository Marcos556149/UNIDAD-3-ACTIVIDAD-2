from ClaseSabor import Sabor
class Helado:
    __Sabores1= []
    __gramos= 0
    def __init__(self):
        self.__gramos= 0
        self.__Sabores1= []
    def agregarSabores(self,listaSaboresAUX, cantGramos):
        self.__gramos = cantGramos
        for Sabor in listaSaboresAUX:
            self.__Sabores1.append(Sabor)
    def cantSabores(self,listaSaboresTOP):
        for Sabor in self.__Sabores1:
            numm= Sabor.getNumero1()
            listaSaboresTOP[numm - 1] += 1
    def buscarSaborenHelado(self,nummSabor):
        g= 0
        banderaa= False
        while(banderaa == False)and(g < len(self.__Sabores1)):
            if nummSabor == self.__Sabores1[g].getNumero1():
                banderaa= True
            g += 1
        return banderaa
    def getGramosPorSabor(self):
        return self.__gramos / len(self.__Sabores1)
    def getGramos(self):
        return self.__gramos
    def MostrarSaboresNoRepetidos(self,NoRepetir):
        for Sabor in self.__Sabores1:
            Numero1= Sabor.getNumero1()
            if NoRepetir.count(Numero1) == 0:
                NoRepetir.append(Numero1)
                print(Sabor.getNombre())
