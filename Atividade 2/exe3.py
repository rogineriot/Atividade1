lista = []


for i in range (3) :
   num = int(input(f"Digite um número {i+1}: "))
   lista.append(num)
#print(lista) 

maior = lista[0]  
print(maior)

for n in range (3):
    if lista[1]> maior :
        maior= lista[1]
    elif lista[2]> maior:
        maior = lista[2]    
print("O maior número é: ", maior)        