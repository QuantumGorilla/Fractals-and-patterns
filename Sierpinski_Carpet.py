#Imports necesarios (Easter Egg)
import turtle as potte

#---Funciones---
def sierpinski_Carpet(iterations, l):
    
    if iterations == 0: #Case base    
        #Dibuja los rectangulos llenos

        potte.color('red', 'darkgray')
        potte.begin_fill()
        for _ in range (4):
            potte.forward(l)
            potte.left(90)
        potte.end_fill()

    else: #Magia

        #Al rededor del centro crea 8 rectangulos pequeñitos
        #Crea dos rectangulos de cada lado
        #Repite 4 veces

        for _ in range(4):
            #Primer rectangulo
            sierpinski_Carpet(iterations-1, l/3)    
            potte.forward(l/3)

            #Seguno rectangulo
            sierpinski_Carpet(iterations-1, l/3)    
            potte.forward(l/3)

            #Para la otra esquina
            potte.forward(l/3)
            potte.left(90)

        #El update de toda la vida
        potte.update()

#---main---  
def fractal():
    #Para que lo haga más rápido (Evoluciona a liebre)
    potte.speed(0) 

    #Empieza
    n = int(input('Digite n: '))
    potte.penup()
    potte.goto((-400)/2, (-400/2))
    potte.pendown()
    sierpinski_Carpet(n, 400)
    area = (((400)/(3*n))**2)* 8**n
    print('El area es: ' + str(area / 400))
    
    #Salida
    potte.exitOnClick()
