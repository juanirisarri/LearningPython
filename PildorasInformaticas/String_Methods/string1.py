
# String methods:
#   upper()       :: convierte a mayus
#   lower()       :: convierte a minus
#   capitalize()  :: Primera a mayus. Resto en minus

#   count(str)    :: Cuenta cuantas veces aparece una cierta cadena un otra
#   isdigit()     :: Devuelve 'True' si es digito
#   isalnum()     :: Devuelve 'True' si es alfanumerico
#   isalpha()     :: Devuelve 'True' si hay solo letras

#   split()       :: Separa utilizando los espacios que haya (devuelve una lista)
#   strip()       :: Borra los espacios sobrantes al ppio y final

#   find(str)     :: Devuelve el primer índice de cierta cadena dentro de otra
#   rfind(str)    :: Como find() pero empieza por el final

#   replace(str_old, str_new)   :: Cambia una cadena por otra


print("\n")
print("---------------------------------")


A = "jUAn"
B = A.upper()
C = A.lower()
D = A.capitalize()
print(B)
print(C)
print(D)
print(A.isdigit())
print(A.isalnum())
print(A.isalpha())
print("---------------------------------")

Frase = " Hola mundo cruel"
#Frase = " lol"
Palabras = Frase.split()
print(Palabras)
print(Frase.strip())

Frase2 = Frase.replace("cruel","feliz")
print(Frase2)
print("---------------------------------")

conteo = Frase.count("o")
print(conteo)
ind1 = Frase.find("l")
ind2 = Frase.rfind("l")
print(ind1)
print(ind2)


print("---------------------------------")
print("\n")





