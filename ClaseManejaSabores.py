import csv
from ClaseSabor import Sabor
class ManejaSabores:
    __Sabores2= []
    def __init__(self):
        self.__Sabores2= []
    def Mostrar1(self):
        for Sabor in self.__Sabores2:
            print(Sabor)
    def leerArchivoSabores(self):
        archivo= open('sabores.csv')
        reader= csv.reader(archivo,delimiter=',')
        bandera= True
        for fila in reader:
            if bandera:
                bandera= not bandera
            else:
                nom= fila[0]
                des= fila[1]
                saborNuevo= Sabor(nom,des)
                self.__Sabores2.append(saborNuevo)
        archivo.close()
    def getLongitudSabores(self):
        return len(self.__Sabores2)
    def getSabor(self,indice):
        return self.__Sabores2[indice]
    def obtenerNombre(self,indice2):
        return self.__Sabores2[indice2].getNombre()
