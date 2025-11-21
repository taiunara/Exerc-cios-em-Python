from ListaDeExercicios.ArrayTypes.ArrayStack import ArrayStack

# ---------------------------------------
# Usando Pilha
# ---------------------------------------
# def eh_palindromo(elem):
#     stack = ArrayStack()
#     palavra_convertida = ''.join(elem.lower().split())
#
#     for letra in palavra_convertida:
#         stack.push(letra)
#
#     invertida = ""
#
#     while not stack.is_empty():
#         invertida += stack.pop()
#
#     if palavra_convertida == invertida :
#         return True
#     else:
#         return False
#
# print(eh_palindromo('a ra'))

from ListaDeExercicios.ArrayTypes.ArrayQueue import ArrayQueue

# ---------------------------------------
# Usando Fila
# ---------------------------------------

def eh_palindromo(palavra):

    palavra_convertida = "".join(palavra.lower().split())

    fila_normal = ArrayQueue()
    fila_invertida = ArrayQueue()

    for letra in palavra_convertida:
        fila_normal.enqueue(letra)

    for letra in reversed(palavra_convertida):
        fila_invertida.enqueue(letra)

    while not fila_normal.is_empty() and not fila_invertida.is_empty():

        letra1 = fila_normal.dequeue()
        letra2  = fila_invertida.dequeue()

        if letra1 != letra2:
            return False

    return True

print(eh_palindromo("asa"))
print(eh_palindromo("hello"))
print(eh_palindromo("a ra"))