from typing import TypeVar
from node import Node

T = TypeVar('T')


class BinaryTree:
    def __init__(self):
        self.__root = None

    def insert(self, data: T):
        new_node = Node(data)

        if self.__root is None:
            self.__root = new_node

        else:
            self.insert_recuersivo(self.__root, new_node)

    def insert_recuersivo(self, node, new_node):

        if new_node.data.palabra > node.data.palabra:
            if node.right is None:
                node.right = new_node
            else:
                self.insert_recuersivo(node.right, new_node)

        elif new_node.data.palabra < node.data.palabra:
            if node.left is None:
                node.left = new_node
            else:
                self.insert_recuersivo(node.left, new_node)

        else:

            diccionario_temporal_nodo = node.data.repeticiones_direcciones.copy()
            diccionario_temporal_new_node = new_node.data.repeticiones_direcciones.copy()

            for key1 in diccionario_temporal_new_node.keys():
                for key2 in diccionario_temporal_nodo.keys():
                    if key1 == key2:
                        node.data.repeticiones_direcciones[key1] += 1
                    elif key1 not in diccionario_temporal_nodo:
                        node.data.repeticiones_direcciones[key1] = 1

    def recorridos(self):
        print("Inorden")
        self.__inorden(self.__root)

        print("Postorden")
        self.__postorden(self.__root)

        print("PreOrden")
        self.__preorden(self.__root)

    def __inorden(self, node):
        if node is not None:
            self.__inorden(node.left)
            print(node.data)
            self.__inorden(node.right)

    def __postorden(self, node):
        if node is not None:
            self.__postorden(node.left)
            self.__postorden(node.right)
            print(node.data)

    def __preorden(self, node):
        if node is not None:
            self.__preorden(node.right)
            print(node.data)
            self.__preorden(node.left)

    def serch(self, data):
        route = []
        return self.__search_recursive(data=data, route=route, node=self.__root)

    def __search_recursive(self, data, node: Node[T], route):
        if node is None:
            print("El valor no se encuentra en el arbol")
            return

        if node.data.palabra == data:
            route.append(f"Subarbol {node.data}")
            return node.data

        if node.data.palabra < data:
            route.append(f"Subarbol {node.data}")
            self.__search_recursive(data, node.right, route)

        if node.data.palabra > data:
            route.append(f"Subarbol {node.data}")
            self.__search_recursive(data, node.left, route)

    def max(self):
        print("Maximo")
        return self.__max_recursive(self.__root)

    def __max_recursive(self, node):
        if node is not None:
            if node.right is None:
                return node.data
            else:
                return self.__max_recursive(node.right)

    def min(self):
        print("Minimo")
        return self.__min_recursive(self.__root)

    def __min_recursive(self, node):
        if node is not None:
            if node.left is None:
                return node.data
            else:
                return self.__min_recursive(node.left)

    def is_none(self):
        return self.__root is None
