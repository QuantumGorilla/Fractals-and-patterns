import turtle as potte

def spiral(size, i):
    potte.begin_fill()
    
    potte.left(size/i)
    potte.forward(40)
    
    potte.left(size/i)
    potte.forward(40)
    
    potte.left(size/i)
    potte.forward(40)
    
    potte.left(size/i)
    potte.forward(40)
    
    potte.left(size/i)
    potte.forward(40)
    
    potte.end_fill()
    
def fractal():
    potte.tracer(4)
    potte.color('gray')
    n = int(input('Digite n: '))
    for i in range(1,360):
        spiral(90, i/n)
    potte.exitonclick()