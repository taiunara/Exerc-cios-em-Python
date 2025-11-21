from ListaDeExercicios.ArrayTypes.ArrayQueue import ArrayQueue, EmptyQueue

queue = ArrayQueue()

def usando_first(fila):
    try:
        print(fila.first())
    except EmptyQueue as e:
        print("Erro!", e)

def usando_dequeue(fila):
    try:
        print(fila.dequeue())
    except EmptyQueue as e:
        print("Erro!", e)

usando_first(queue)
usando_dequeue(queue)