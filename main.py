from ClaseManejaHelados import ManejaHelados
from ClaseManejaSabores import ManejaSabores
if __name__=='__main__':
    Sabores= ManejaSabores()
    Sabores.leerArchivoSabores()
    Helados= ManejaHelados()
    while True:
        print("_____MENU DE OPCIONES_____")
        print("[1]...Registrar Venta de helado")
        print("[2]...Top 5 sabores mas pedidos")
        print("[3]...Total de gramos vendidos de un sabor")
        print("[4]...Sabores vendidos de un tipo de helado")
        print("[0]...Salir")
        try:
            op= int(input('Seleccione una opcion: '))
            if op in range(5):
                if op == 1:
                    Helados.agregarHelado(Sabores)
                if op == 2:
                    totalListaSabores= Sabores.getLongitudSabores()
                    Helados.Top5Sabores(totalListaSabores,Sabores)
                if op == 3:
                    Sabores.Mostrar1()
                    Helados.totalGramos(Sabores)
                if op == 4:
                    Helados.tipoDeHelado()
                if op == 0:
                    print("MENU FINALIZADO")
                    break
            else:
                print("ERROR, solo puede ingresar numeros del 0 al 4")
        except ValueError:
            print("ERROR, ingrese solamente numeros")
