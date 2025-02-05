print(" ")
print("--------------------------")


def division(n1,n2):
    try:
        return n1/n2
    finally:                                    # En este caso se ejecuta el try y como salta una exepción nos la indica
        print("Ha ocurrido un error:")          # El finally se ejecuta si salta una excepción en el try
        print(" ")
       
    


a = division(8,0)
print(a)

print(" ")

b = division(8,"hola")
print(b)


print("--------------------------")
print(" ")