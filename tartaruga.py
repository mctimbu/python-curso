import turtle


def desenhaQuadradoMulticolorido(t, tam):
    """Faca a tartaruga t desenhar um quadrado multicolorido de lado tam."""
    for i in ['black', 'orange', 'yellow', 'blue', 'purple', 'green', 'blue1', 'blue2', 'blue3', 'pink', 'aquamarine', 'magenta']:
        t.color(i)
        t.forward(tam)
        t.left(30)


wn = turtle.Screen()              # Inicializa a janela e seus atributos
wn.bgcolor("lightgreen")

tess = turtle.Turtle()            # cria tess e seus atributos
tess.pensize(3)

tamanho = 3                      # tamanho do menor quadrado
for i in range(60):
    desenhaQuadradoMulticolorido(tess, tamanho)
    tamanho = tamanho + 2       # aumenta o tamanho para a próxima vez
    tess.forward(4)             # move tess um pouco à frente
    tess.right(28)               # e dá uma virada nela

wn.exitonclick()
