def pedirNombre (nombreEscogido):
    lista= ["Manolo", "Pedro", "Matias", "Carlos", "Juan"]
    print(lista)
    if (nombreEscogido == lista[0]):
        print("El nombre escogido tiene una maldicion, La Maldicion de {nombreEscogido}".format(nombreEscogido=nombreEscogido))
    elif (nombreEscogido == lista[1]):
        print("El nombre escogido tendra 50 años de buena suerte gracias a {nombreEscogido}".format(nombreEscogido=nombreEscogido))
    elif (nombreEscogido == lista[2]):
        print("El nombre escogido tendra 100 años de mala suerte todo por el señor {nombreEscogido}".format(nombreEscogido=nombreEscogido))
    elif (nombreEscogido == lista[3]):
        print("El nombre escogido es el ganador de un viaje al caribe gracias a {nombreEscogido}".format(nombreEscogido=nombreEscogido))
    elif (nombreEscogido == lista[4]):
        print("El nombre escogido tendra un collar de diamntes con el nombre {nombreEscogido}".format(nombreEscogido=nombreEscogido))
    else:
        print("El nombre introducido no es de los 5 listados porfabor vuelva intentarlo")