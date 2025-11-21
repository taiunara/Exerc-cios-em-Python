from ListaDeExercicios.ArrayTypes.ArrayDeque import ArrayDeque

deque = ArrayDeque()

while True:

    comando = input("O que deseja fazer? 1. Add no Inicio | 2. Add no fim | 3. Remover do Inicio | 4. Remover do fim: ")

    if comando == '1':
        palavra = input("Digite uma palavra: ")
        deque.add_first(palavra)
        print(deque)
    elif comando == '2':
        palavra = input("Digite uma palavra: ")
        deque.add_last(palavra)
        print(deque)
    elif comando == '3':
        deque.remove_first()
        print(deque)
    elif comando == '4':
        deque.remove_last()
        print(deque)
    else:
        print("Comando não encontrado, verifique e tente novamente!")
        break