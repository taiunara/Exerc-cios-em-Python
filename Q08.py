from ListaDeExercicios.ArrayTypes.ArrayQueue import ArrayQueue

fila_origem = ArrayQueue()
fila_destino = ArrayQueue()

def transferir(origem, destino):
    if origem.is_empty():
        print(f"A fila está vazia!")
    else:
        while not origem.is_empty():
            queue = origem.dequeue()
            destino.enqueue(queue)
        print(f'Transferência concluída com sucesso!')

fila_origem.enqueue('1')
fila_origem.enqueue('2')
fila_origem.enqueue('3')

print(f'Fila Origem: {fila_origem}')
print(f'Fila Destino: {fila_destino}')

transferir(fila_origem,fila_destino)

print(f'Após transferencia - Fila Origem: {fila_origem}')
print(f'Após transferencia- Fila Destino: : {fila_destino}')