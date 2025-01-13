
# or  :: or
# and :: and

print(" ")
print("Verificación de acceso")

edad_usuario = int( input("Introduce tu edad: ") )

if 0 < edad_usuario < 18 or edad_usuario >100:
    print("No puedes pasar")

    if edad_usuario > 100:
        print("Es imposible que seas tan mayor")

elif edad_usuario < 0:
    print("Edades negativas no suena muy normal")

else:
    print("Puedes pasar")

print(" ")
print("----------------")
print(" ")

if 1<2<3<4==4>1:                         # Se pueden concatenar condiciones
    print("Todo funciona bien")
    print(" ")

