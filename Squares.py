import turtle as potte

def draw_square():
    potte.forward(50)
    potte.left(90)
    potte.forward(50)
    potte.left(90)
    potte.forward(50)
    potte.left(90)
    potte.forward(50)
    potte.left(90)
    
def fractal():
    potte.color('gray')
    n = int(input('Digite n: '))
    for i in range(360**n):
        potte.tracer(3)
        draw_square()
        potte.left(i)
    potte.exitonclick()