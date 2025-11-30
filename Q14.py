from ListaDeExercicios.ArrayTypes.ArrayDeque import ArrayDeque

#Testando rotate()

deque = ArrayDeque()

deque.add_first("Lua")
deque.add_first("Sol")
deque.add_last("Star")
deque.add_last("Galaxy")

print(deque)
print(deque.first())
deque.rotate()
print(deque)