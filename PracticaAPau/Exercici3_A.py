from random import random


def numeroAlazar (numeroPedido):
    numeroAleatorio = random.randange(0,100)
    while (numeroPedido == numeroAleatorio):
        if (numeroPedido == numeroAleatorio):
            print("Molt bè !! Has adivinado el numero! = {numeroPedido}".format(numeroPedido=numeroPedido))
        elif (numeroPedido < numeroAleatorio):
            print("El numero es mas grande")
        elif (numeroPedido > numeroAleatorio):
            print("El numero es mas pequeño")
