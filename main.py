def añoBisiesto():
    print('Introduce un año')
    año=int(input())
    if (año%4==0):
        print('El año es bisiesto')
    else:
        print('el año no es bisiesto')

añoBisiesto()

