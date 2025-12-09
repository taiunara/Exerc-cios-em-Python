from ListaDeExercicios.ArrayTypes.ArrayStack import ArrayStack

stack = ArrayStack()

html1 = "<html><body><h1>Título</h1></body></html>"
html2 = "<body><p>Texto 1</p><b>Texto 2</b>"
html3 = "<a><b></b></i>"

print(stack.is_matched_html(html1))
print(stack.is_matched_html(html2))
print(stack.is_matched_html(html3))