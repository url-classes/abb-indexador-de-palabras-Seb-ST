from serch import Indexer


def main():
    indexer = Indexer()

    while True:
        indexer.update()

        opcion = input("1,Buscar palabra"
                       "\n2.Salir"
                       "\nEscoja la opcion que desea(1/2): ")

        if opcion == "1":
            palabra_a_buscar = input("Ingrese la palabra que quiere buscar: ")
            indexer.serch(palabra_a_buscar)

        elif opcion == "2":
            print("Hasta la proxima")
            break
        else:
            pass


main()
