#Tortuga magica (Easter Egg)(Import necesario)
import turtle as potte

#---Funciones---
#Forward que tanto va a continuar, right(xx) que tanto va a rotar hacia la derecha
#left(xx) que tanto va a rotar hacia la izquierda
#Se necesitan 90 grados para rotar y darle el sentido opuesto a donde termina

def fractalH(iterations, center, length):

    potte.color('blue')
    
    if iterations < 0: #Caso base
        return

    #En caso tal se empiece desde un punto distinto al centro
    if center is not None:
        potte.penup()
        potte.goto(center)
        potte.pendown()

    #Hace las ramas o Hs (aches) de la parte inferior derecha
    potte.forward(length / 2)
    potte.right(90)
    potte.forward(length / 2)
    potte.left(90)

    fractalH(iterations - 1, None, length / 2)

    #Se devuelve
    potte.left(90)
    potte.forward(length)
    potte.right(90)

    fractalH(iterations - 1, None, length / 2)

    #Completa las ramas o Hs (aches) de la parte inferior derecha (->H, este ladito)
    #Y empiezas con las Hs superiores 
    potte.right(90)
    potte.forward(length / 2)
    potte.right(90)
    potte.forward(length)
    potte.left(90)
    potte.forward(length / 2)
    potte.right(90)

    fractalH(iterations - 1, None, length / 2)

    potte.right(90)
    potte.forward(length)
    potte.right(90)

    fractalH(iterations - 1, None, length / 2)

    #Regresa a la tortuga al centro de todo para empezar con el lado izquierdo
    potte.right(90)
    potte.forward(length / 2)
    potte.left(90)
    potte.forward(length / 2)  
    #Una vez terminado con el lado izquierdo deja la tortuga en el centro

#--Main--
def fractal():
    #Empieza
    n = int(input('Digite n: '))
    potte.speed(0)
    fractalH(n, (0, 0), 200) 
    print('Hojas: ' + str(4**(n+1)))
    
    #Salida
    potte.exitonclick()  