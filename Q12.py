from ListaDeExercicios.ArrayTypes.DequeQueue import DequeQueue

#Testando DequeQueue

queue = DequeQueue()

queue.enqueue("Olá Mundo")
queue.enqueue("Sistemas e Mídias Digitais")
queue.enqueue("Tainara")
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")

queue.dequeue()

print(queue)