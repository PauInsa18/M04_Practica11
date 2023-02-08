from PracticaAPau import Exercici1_A as ex1a
from PracticaAPau import Exercici2_A as ex2a
from PracticaAPau import Exercici3_A as ex3a
#Mostrar cual es el numero menor o el mayor, y si son iguales tambien decirlo.

numeroUno = int(input("Introduce un numero : "))
numeroDos = int(input("Introduce un segundo numero: "))
print(ex1a.mayorMenor(numeroUno,numeroDos))


#Aqui podremos crear una lista de 5 nombres en el cual el usuario tendra que escoger
#Segun cada nombre le printara una cosa distinta.
nombreEscogido = input("Introduce un nombre : ")
print(ex2a.pedirNombre(nombreEscogido))


#Aqui pedira al usuario que ponga un numero del 1 - 100 si lo adivina le saldra el mensaje
numeroPedido = int(input("Escoja entre un numero del 1 al 100 : "))
print(ex3a.numeroAlazar(numeroPedido))