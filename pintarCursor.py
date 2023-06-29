import turtle

# Configuración inicial
turtle.speed(0)
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

# Funciones para controlar el movimiento del cursor
def mover_adelante():
    turtle.forward(100)

def mover_atras():
    turtle.backward(100)

def girar_izquierda():
    turtle.left(90)

def girar_derecha():
    turtle.right(90)

def limpiar():
    turtle.clear()

# Configurar los eventos del teclado
turtle.onkey(mover_adelante, 'Up')
turtle.onkey(mover_atras, 'Down')
turtle.onkey(girar_izquierda, 'Left')
turtle.onkey(girar_derecha, 'Right')
turtle.onkey(limpiar, 'c')

# Activar la escucha de eventos
turtle.listen()
turtle.mainloop()