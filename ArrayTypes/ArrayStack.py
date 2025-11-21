class EmptyStack(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self.__stack = []

    def push(self, elem):
        self.__stack.append(elem)

    def pop(self):
        if not self.is_empty():
            return self.__stack.pop()
        raise EmptyStack("A pilha está vazia!")

    def is_empty(self):
        return  len(self.__stack) == 0

    def top(self):
        if self.is_empty():
            raise EmptyStack("A pilha está vazia!")
        return self.__stack[-1]

    def __str__(self):
        return self.__stack.__str__()

    def remove_all(self):
        self.__stack = []

