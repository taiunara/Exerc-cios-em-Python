from ListaDeExercicios.ArrayTypes.ArrayPriorityQueue import ArrayPriorityQueue

def adicionar_pacientes():
    priority_queue = ArrayPriorityQueue()

    priority_queue.add(3, 'Lucca - Queda')
    priority_queue.add(1, 'Liana - Fratura')
    priority_queue.add(6, 'Fer  - Gripe')

    while not priority_queue.is_empty():
        paciente = priority_queue.remove_min()
        print(f"O caso {paciente} foi atendido")


print(adicionar_pacientes())

