#Escribir un programa que pida al usuario un texto y un entero. 
#Mandar a imprimir en pantalla el texto repitido las veces indicadas por el numero.
#Hacer el programa usando una función

def  repetir ( texto , rep ):
    texto  + =  ' \ n '
    print ( texto * rep )

t  =  input ( "Ingrese texto a imprimir:" )
r  =  int ( input ( "Ingrese el número de veces que se va a imprimir el texto:" ))
repetir ( t , r )