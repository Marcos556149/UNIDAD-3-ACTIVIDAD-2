from ClaseManejaSabores import ManejaSabores
from ClaseHelado import Helado
class ManejaHelados:
    __listaHelados= []
    def __init__(self):
        self.__listaHelados= []
    def agregarHelado(self, Sabores):
        listaSaboresAUX= []
        tamano=int(input('Ingrese tamaño, TAMAÑOS DISPONIBLES: 100gr, 150gr, 250gr, 500gr, 1000gr: '))
        if (tamano == 100)or(tamano == 150)or(tamano == 250)or(tamano == 500)or(tamano == 1000):
            cantSabores= int(input('Ingrese la cantidad de sabores, el maximo es 4: '))
            if (cantSabores > 0)and(cantSabores < 5):
                print('SABORES DISPONIBLES')
                Sabores.Mostrar1()
                for i in range(cantSabores):
                    numeroSabor= int(input('Ingrese el numero del sabor  que desea agregar al helado: '))
                    while (numeroSabor < 1)or(numeroSabor > Sabores.getLongitudSabores()):
                        numeroSabor= int(input('Numero de sabor incorrecto, ingrese nuevamente el numero del sabor: '))
                    listaSaboresAUX.append(Sabores.getSabor(numeroSabor - 1))
                heladoo= Helado()
                heladoo.agregarSabores(listaSaboresAUX, tamano)
                self.__listaHelados.append(heladoo)
                listaSaboresAUX= []
            else:
                print("Cantidad de sabores incorrecta")
        else:
            print("El tamaño de helado ingresado no corresponde con ningun tamaño disponible")
    def Top5Sabores(self,totalListaSabores,Sabores):
        listaSaboresTOP= [0 for k in range(totalListaSabores)]
        for Helado in self.__listaHelados:
            Helado.cantSabores(listaSaboresTOP)
        for p in range(5):
            maxx= max(listaSaboresTOP)
            indice1= listaSaboresTOP.index(maxx)
            listaSaboresTOP[indice1]= 0
            print("{} = {}".format(p+1,Sabores.obtenerNombre(indice1)))
    def totalGramos(self,Sabores):
        nummSabor= int(input("Ingrese un numero de sabor: "))
        if (nummSabor > 0)and(nummSabor <= Sabores.getLongitudSabores()):
            totaldeGramos= 0
            for Helado in self.__listaHelados:
                if Helado.buscarSaborenHelado(nummSabor):
                    totaldeGramos += Helado.getGramosPorSabor()
            print("Para el sabor numero {} el total de gramos vendidos es: {:.1f}".format(nummSabor,totaldeGramos))
        else:
            print("Numero de sabor incorrecto")
    def tipoDeHelado(self):
        NoRepetir= []
        print("TIPO DE HELADO DISPONIBLE: 100gr, 150gr, 250gr, 500gr, 1000gr")
        tipoHelado= int(input('Ingrese tipo de helado: '))
        if (tipoHelado == 100)or(tipoHelado == 150)or(tipoHelado == 250)or(tipoHelado == 500)or(tipoHelado == 1000):
            for Helado in self.__listaHelados:
                if tipoHelado == Helado.getGramos():
                    Helado.MostrarSaboresNoRepetidos(NoRepetir)
            if len(NoRepetir) == 0:
                print("No se vendio ningun sabor en helados de {} gramos".format(tipoHelado))
        else:
            print("El tipo de helado ingresado no corresponde con ningun tipo de helado disponible")
