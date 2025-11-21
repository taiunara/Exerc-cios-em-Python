from ListaDeExercicios.ArrayTypes.ArrayStack import ArrayStack, EmptyStack

stack = ArrayStack()

def usando_top(pilha):
    try:
        print(pilha.top())
    except EmptyStack as e:
        print("Erro:", e)

def usando_pop(pilha):
    try:
        print(pilha.pop())
    except EmptyStack as e:
        print("Erro!", e)

# stack.push("A")
# stack.push("B")
# stack.push("C")
# stack.push("D")
usando_top(stack)
usando_pop(stack)