
import numpy as np
import timeit



def compute_reciprocalsSLOW(values):        
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 / values[i]
    return output


def compute_reciprocalsFAST(values):
    output = 1.0/values
    return output




big_array = np.random.randint(1, 10, size=1000000)
num_ejec = 10;  # número de ejecuciones


print("\n")
print("----------------------------------")

#print(np.shape(big_array))

t_slow = timeit.timeit( lambda: compute_reciprocalsSLOW(big_array), number = num_ejec )
t_slow = t_slow/num_ejec
t_fast = timeit.timeit( lambda: compute_reciprocalsFAST(big_array), number = num_ejec )
t_fast = t_fast/num_ejec


print("Tiempo SLOW: ", t_slow ) 
print("Tiempo FAST: ", t_fast )
print("t_slow/t_fast: ", t_slow/t_fast )

# print("----------------------------------")
# print(compute_reciprocalsSLOW(big_array))
# print("----------------------------------")
# print(compute_reciprocalsFAST(big_array))


print("----------------------------------")
print("\n")



