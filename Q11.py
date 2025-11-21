from ListaDeExercicios.ArrayTypes.ArrayDeque import ArrayDeque

def eh_palindromo(palavra):
    palavra_convertida = ''.join(palavra.lower().split())
    deque = ArrayDeque()

    for letra in palavra_convertida:
        deque.add_first(letra)

    while not deque.is_empty():
        primeiro = deque.remove_first()
        if deque.is_empty():
            return True
        ultimo = deque.remove_last()
        if primeiro != ultimo:
            return False
    return True

print(eh_palindromo("ca sa"))
print(eh_palindromo("A sa"))
print(eh_palindromo("Ara ra"))
