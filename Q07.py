from ListaDeExercicios.ArrayTypes.ArrayQueue import ArrayQueue

fila = ArrayQueue()

def adicionar_docs(documento):
    fila.enqueue(documento)

def imprimir_doc():
    if fila.is_empty():
        print(f'A fila para impressão está vazia')
    else:
        print(f'Imprimindo: {fila.first()}')
        fila.dequeue()


adicionar_docs("trabalho ed.pdf")
adicionar_docs("foto.png")
adicionar_docs("Lilas.mp3")
print(fila)
imprimir_doc()
print(fila)
