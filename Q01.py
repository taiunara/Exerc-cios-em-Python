from ListaDeExercicios.ArrayTypes.ArrayStack import ArrayStack

def inverter_frase(frase):
    palavras = frase.split()
    resultado = []

    for palavra in palavras:
        stack = ArrayStack()
        for letra in palavra:
            stack.push(letra)
        invertida = ''

        while not stack.is_empty():
           invertida += stack.pop()
        resultado.append(invertida)

    frase_final = " ".join(resultado)
    print(frase_final)

inverter_frase("Sistemas e Midias")
inverter_frase("Olá Mundo")













