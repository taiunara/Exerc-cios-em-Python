from ListaDeExercicios.ArrayTypes.DequeStack import DequeStack

#Testando DequeStack

stack = DequeStack()

stack.push("Olá Mundo")
stack.push("Sistemas e Mídias Digitais")
stack.push("Tainara")
stack.push("A")
stack.push("B")
stack.push("C")

stack.pop()

print(stack)