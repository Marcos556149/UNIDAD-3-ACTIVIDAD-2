class Sabor:
    Numero= 0
    __numero= 0
    __nombre= ''
    __descripcion= ''
    @classmethod
    def getNumero(cls):
        cls.Numero += 1
        return cls.Numero
    def __init__(self,nom='',des=''):
        self.__nombre= nom
        self.__descripcion= des
        self.__numero = self.getNumero()
    def __str__(self):
        return 'Sabor: {}, Numero: {}, Descripcion: {}'.format(self.__nombre,self.__numero,self.__descripcion)
    def getNumero1(self):
        return self.__numero
    def getNombre(self):
        return self.__nombre
