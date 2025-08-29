#summem trae 2 datos de memoria, pide la posición de memoria que quiere y donde se quiere guardar la misma

def SUMMEM(mem, n, save):
    first_data = mem[n][n] #me da el dato que apunta en la dirección n
    second_data = mem[n+1][n+1]
    add = first_data + second_data
    mem[save][save] = add


