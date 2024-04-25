import os
from serch_binary_tree import BinaryTree


def serch_txt():
    # Ruta de la carpeta a recorrer
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    lista_directorios = []

    # Recorre la carpeta y lista los archivos con extensión .txt
    for archivo in os.listdir(directorio_actual):
        if archivo.endswith('.txt'):
            lista_directorios.append(archivo)

    return lista_directorios


class Word:
    def __init__(self, palabra, repeticiones, direccion):
        self.palabra = palabra

        self.repeticiones_direcciones = {direccion: repeticiones}

    def update(self, repeticiones, direccion):
        self.repeticiones_direcciones[direccion] += repeticiones


class Indexer:
    def __init__(self):
        self.tree = BinaryTree()

    def serch(self, palabra):
        locacion_palabra = self.tree.serch(palabra)

        if locacion_palabra is not None:
            print("En estas locaciones se encuentra la palabra qu busca")
            print(locacion_palabra.repeticiones_direcciones)
        else:
            print("La palabra no esta en el arbol")

    def update(self):
        # Conseguimos la lista de ficheros
        lista_directorios = serch_txt()

        # Recorremos la lista
        for directorio in lista_directorios:

            # Abrimos cada fichero
            with open(directorio, "r") as fichero:

                # Recorremos las lineas de cada fichero
                for linea in fichero.readlines():

                    # Obtenemos las palabras de cada fichero
                    for palabra in linea.split():
                        palabra_temporal = Word(palabra, 1, directorio)
                        self.tree.insert(palabra_temporal)
