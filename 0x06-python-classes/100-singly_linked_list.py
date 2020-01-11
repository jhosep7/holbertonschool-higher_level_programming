#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return (self.__data)
    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return (self.__next_node)
    @next_node.setter
    def next_node(self, value):
        if value == None:
            self.__next_node = value
        elif isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")

class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if self.__head == None or value < self.__head.data:
            self.__head = Node(value, self.__head)
            return
        Temp = self.__head
        while Temp.next_node != None and Temp.next_node.data < value:
            Temp = Temp.next_node
        Temp.next_node = Node(value, Temp.next_node)

    def __repr__(self):
        if self.__head == None:
            return (" ")
        MyArr = ""
        Temp = self.__head
        while (Temp):
            MyArr += repr(Temp.data)
            Temp = Temp.next_node
            if Temp != None:
                MyArr += "\n"
        return (MyArr)
