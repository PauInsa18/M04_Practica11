def mayorMenor (numeroUno,numeroDos):
    if (numeroUno < numeroDos):
        print("Numero menor = {numeroUno} Numero mayor = {numeroDos}".format(numeroUno=numeroUno, numeroDos=numeroDos))
    elif (numeroUno > numeroDos):
        print("Numero mayor = {numeroUno} Numero menor = {numeroDos}".format(numeroUno=numeroUno, numeroDos=numeroDos))
    else:
        print("Los numeros son iguales")
