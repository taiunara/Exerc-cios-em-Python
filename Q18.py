from ListaDeExercicios.ArrayTypes.ArrayPriorityQueue import ArrayPriorityQueue
from ListaDeExercicios.ArrayTypes.ArrayQueue import ArrayQueue

queue = ArrayQueue()
queue_priority = ArrayPriorityQueue()

def adicionar_tarefa(tipo_tarefa):
    tarefa_convertida = tipo_tarefa.lower()

    if tarefa_convertida == 'tarefa normal':
        queue.enqueue(tarefa_convertida)
    elif tarefa_convertida == 'tarefa urgente':
        queue_priority.add(1, tarefa_convertida)
    else:
        print(f'Reveja as informações e digite novamente')

def processar_tarefa():
    if not queue_priority.is_empty():
        tarefa = queue_priority.remove_min()
        print(f"Processando tarefa URGENTE: {tarefa}")

    elif not queue.is_empty():
        tarefa = queue.dequeue()
        print(f"Processando tarefa normal: {tarefa}")

    else:
        print("Nenhuma tarefa para processar.")


# teste
adicionar_tarefa("tarefa normal")
adicionar_tarefa("tarefa normal")
adicionar_tarefa("tarefa urgente")
adicionar_tarefa("tarefa urgente")

processar_tarefa()
processar_tarefa()
processar_tarefa()
processar_tarefa()
processar_tarefa()