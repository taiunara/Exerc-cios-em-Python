from ListaDeExercicios.ArrayTypes.ArrayQueue import ArrayQueue
from ListaDeExercicios.ArrayTypes.ArrayStack import ArrayStack


def inverter_fila(queue):
    stack = ArrayStack()
    if queue.is_empty():
        return

    print(f'Fila antes: {queue}')
    print(f'Pilha antes: {stack}')
    while not queue.is_empty():
        elemento_fila = queue.dequeue()
        stack.push(elemento_fila)
    print(f'Pilha depois: {stack}')

    while not stack.is_empty():
        elemento_pilha = stack.pop()
        queue.enqueue(elemento_pilha)
    print(f'Fila depois: {queue}')

#teste

fila = ArrayQueue()

fila.enqueue(1)
fila.enqueue(2)
fila.enqueue(3)

inverter_fila(fila)