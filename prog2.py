#Escribir un programa que pida al usuario 2 numeros entertos y calcular la suma desde 
#desde el numero 1 hasta el numero 2.
#Imprimir el resultado de la suma.

suma  =  0
num1  =  int ( input ( "Dame un numero: \ n " ))
num2  =  int ( input ( "Dame otro numero: \ n " ))
num2  =  num2  +  1

para  num  en  rango ( num1 , num2 ):
    suma  + =  num
    
imprimir ( suma )