from CISC import *
from Memoria import *
from RISC import *

#variables
A = [1,2,3,4,5,6,7,8,9,10]
B= [1,2,3,4,5,6,7,8,9,10]
list1, list2, resul = [], [], []
cicleRISC = 0
cicleCISC = 0

#quiero meter
mem = Memoria()
#estas escrituras en memoria no se cuentan porque el programa se supone que debe iniciar con estas cargadas
for i in range(len(A)):
    mem.mem[2*i][2*i]     = A[i]
    mem.mem[2*i+1][2*i+1] = B[i]


LoadVec(mem.mem, list1, list2); cicleRISC+=20
SumVec(list1, list2, resul); cicleRISC+=10
WriteVec(mem.mem, resul); cicleRISC+=10

for i in range(len(mem.mem)):
  print(mem.mem[i])
print("Vector 1:", list1)
print("Vector 2:", list2)
print("Suma:", resul)


SUMMEM(mem.mem, 2, 8); cicleCISC +=3

print("Ciclos RISC:", cicleRISC)
print("Ciclos CISC:", cicleCISC)

for i in range(len(mem.mem)):
  print(mem.mem[i])