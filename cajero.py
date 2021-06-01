clave = int(input("Ingrese su clave: "))
mont = 200000

def monto(mont):

    print(f'El monto total de la cuenta de su tarjeta es: {mont}')
    return run(clave)

def retirar(mont):
    retirar_dinero = int(input('Ingrese la cantidad a retirar: '))
    if retirar_dinero >= mont:
        print('La cantidad ingresada excede el monto de su cuenta\n Ingresela nuevamente\n')
        return retirar(mont)
    elif retirar_dinero < 0:
        print('No se pueden ingresar numeros negativos\n Ingresela nuevamente\n')
        return retirar(mont)
    else:
        print(f'El monto a retirar es de: {retirar_dinero}')
        mont -= retirar_dinero
        print(f'El saldo de su cuenta es de: {mont}')
        return run(clave)



def run(clave):


    if clave == 1234:
        num = int(input("""
        Bienvenido al sistema de cajero
        
        1-Verificar el monto de su tarjeta
        2-Retirar dinero de la cuenta
        3-Salir
        
        """))
        if num == 1:
            monto(mont)

        elif num == 2:
            retirar(mont)
        else:
            print('Gracias por su visita')


    else:
        print('La clave que ha ingresado es incorrecta\n Vuelva a ingresarla')


run(clave)
print('plata')