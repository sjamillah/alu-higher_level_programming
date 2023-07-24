#!/usr/bin/python3
""" Defines a new class called Node """


class Node:
    """ Node serves as a single linked list """

    def __init__(self, data, next_node=None):
        """ Initialization of new data """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Returns the value of data """
        return self.__data

    @data.setter
    def data(self, value):
        """ Sets the value of data """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Returns the value of the next node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Sets the value of the next node """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ class to manage singly linked list operations """

    def __str__(self):
        """ prints the members of the singly linked list on a separate line """
        rtn = ""
        ptr = self.__head

        while ptr is not None:
            rtn += str(ptr.data)
            if ptr.next_node is not None:
                rtn += "\n"
            ptr = ptr.next_node

        return rtn

    def __init__(self):
        """ initialization of data into the new singly linked list """
        self.__head = None

    def sorted_insert(self, value):
        ptr = self.__head

        while ptr is not None:
            if ptr.data > value:
                break
            ptr_prev = ptr
            ptr = ptr.next_node

        newNode = Node(value, ptr)
        if ptr == self.__head:
            self.__head = newNode
        else:
            ptr_prev.next_node = newNode
