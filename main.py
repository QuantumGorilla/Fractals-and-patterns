import FractalH
import Sierpinski_Carpet
import Squares
import Circles
import Sierpinski_Sieve
import Spiral

def menu():
    print('1. Fractal H')
    print('2. Sierpinski Carpet')
    print('3. Sierpinski Sieve')
    print('4. Patrón: Squares')
    print('5. Patrón: Circles')
    print('6. Patrón: Spiral')
    print('7. Salir')
    answer = int(input('> '))
    if answer == 7:
        return
    elif answer == 1:
        FractalH.fractal()
    elif answer == 2:
        Sierpinski_Carpet.fractal()
    elif answer == 3:
        Sierpinski_Sieve.fractal()
    elif answer == 4:
        Squares.fractal()
    elif answer == 5:
        Circles.fractal()
    elif answer == 6:
        Spiral.fractal()
    else:
        print('Ingrese un número valido\n')
        menu()
        
    print('Presione enter para continuar')
    input()
    menu()
    
if __name__ == '__main__':
    menu()