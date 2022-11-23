numeros = [1,2,3,4,5,6,7,8,9]
countPar = 0
countImpar = 0

for i in range(9):
    if numeros[i] % 2 == 0 :
        countPar +=1
    else:
        countImpar += 1    
print("A quantidade de números par é: ", countPar) 
print("A quantidade de números impar é: ", countImpar)         