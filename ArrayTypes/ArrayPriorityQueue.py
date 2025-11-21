class ArrayPriorityQueue:
    def __init__(self):
        self.__priority_queue = []

    def add(self, priority, elem):
        self.__priority_queue.append((priority, elem))
        self.__priority_queue.sort()

    def remove_min(self):
        return self.__priority_queue.pop(0)

    def min(self):
        if not self.is_empty():
            return self.__priority_queue[0]
        return print(f'Está vazia!')

    def is_empty(self):
        return len(self.__priority_queue) == 0

    def __str__(self):
        return self.__priority_queue.__str__()