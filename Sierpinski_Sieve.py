import turtle as potte

def serp_tri(size, iterations):
    if iterations == 1:
        for i in range(3):
            potte.color('blue')
            potte.ht()
            potte.fd(size)
            potte.left(120)
            potte.tracer(3)

    else:
        potte.ht()
        serp_tri(size/2, iterations-1)
        potte.fd(size/2)
        serp_tri(size/2, iterations-1)
        potte.bk(size/2)
        potte.left(60)
        potte.fd(size/2)
        potte.right(60)
        serp_tri(size/2, iterations-1)
        potte.left(60)
        potte.bk(size/2)
        potte.right(60)

def fractal():
    potte.penup()
    potte.goto(-200, -200)
    potte.pendown()
    n = int(input('Digite n: '))
    serp_tri(400, n)
    potte.exitonclick()