import turtle as potte

def circle():
    potte.right(45)
    potte.forward(45)
    potte.right(45)
    potte.forward(85)
    potte.right(85)
    potte.forward(85)
    potte.right(45)
    potte.forward(85)
    potte.right(45)
    potte.forward(85)
    
    

def fractal():
    potte.left(90)
    potte.backward(30)
    potte.penup()
    potte.goto(-50,100)
    potte.pendown()
    potte.tracer(3)
    n = int(input('Digite n: '))
    for i in range(270**n):
        circle()
    potte.exitonclick()