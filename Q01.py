from ListaDeExercicios.ArrayTypes.ArrayStack import ArrayStack

def digitar_palavra():
    palavra_digitada = input("Digite algo: ")
    palavras = palavra_digitada.split()

    inverter_frase(palavras)

def inverter_frase(palavras):
    stack = ArrayStack()
    resultado = []
    for palavra in palavras:
        for letra in palavra:
            stack.push(letra)

        frase_invertida = ''

        while not stack.is_empty():
            frase_invertida += stack.pop()
        resultado.append(frase_invertida)

    frase_final = ' '.join(resultado)
    print(frase_final)

digitar_palavra()
