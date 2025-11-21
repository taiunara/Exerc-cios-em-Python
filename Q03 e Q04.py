from ListaDeExercicios.ArrayTypes.ArrayStack import ArrayStack

stack = ArrayStack()
stackRedo = ArrayStack()

comandos_de_edicao = {
    "escrever",
    "selecionar texto",
    "marcar texto",
    "modificar estilo"
}

while True:
    comando = input("Digite um comando: ").lower()

    if comando == "sair":
        print(stack)
        break

    elif comando in comandos_de_edicao:
        stack.push(comando)
        stackRedo.remove_all()

    elif comando == "undo":
        if stack.is_empty():
            print("A lista está vazia!")
        else:
            item = stack.pop()
            stackRedo.push(item)
            print(f"O texto {item} foi removido")

    elif comando == "redo":
        if stackRedo.is_empty():
            print("Nada para desfazer!")
        else:
            item = stackRedo.pop()
            stack.push(item)

    elif comando == "salvar":
        print("Arquivo salvo")

    else:
        print("Comando inválido!")
