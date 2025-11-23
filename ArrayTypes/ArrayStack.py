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

    def remove_bar(self, tag):
        tag_formatada = ""
        for i in tag:
            if i != '/':
                tag_formatada += i
        return tag_formatada

    def is_matched_html(self, html):
        itr = 0

        while itr < len(html):
            if html[itr] == '<':
                comeco = itr
                while itr < len(html) and html[itr] != '>':
                    itr += 1
                tag = html[comeco:itr + 1]

                if tag[1] != '/':
                    self.push(tag)
                else:
                    if self.is_empty():
                        raise ValueError("Inválido - Tag de fechamento sem abertura.")

                    if self.pop()[1:1] != self.remove_bar(tag)[1:1]:
                        raise ValueError("Inválido - Aninhamento  ")

            itr += 1

            if not self.is_empty():
                raise ValueError(f"Inválido - As tags {self.__stack} não foram fechadas.")

            print("Válido")