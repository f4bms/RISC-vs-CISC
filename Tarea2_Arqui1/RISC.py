#RISC-V tiene traer individualmente
def Load(mem, n):
    return mem[n][n]

#lo que quiero es ir trayendo de memoria los vectores intercalados
def LoadVec(mem, l1, l2):
    for i in range(10):
        l1.append(mem[2*i][2*i])
        l2.append(mem[2*i+1][2*i+1])


#RISC-V tiene sumar individualmente
def Sum(x, y):
    return x + y

#save siendo una variable, guarde la suma de los vectores
def SumVec(x,y, save):
    for i in range(len(x)):
        save.append( x[i] + y[i])

#el write toma la lista del sumVec y la mete
def WriteVec(mem, result):
    for i in range(len(result)):
        mem[i+20][i+20] = result[i]
