lista = []


for i in range (3) :
   num = int(input(f"Digite um número {i+1}: "))
   lista.append(num)
#print(lista) 

menor = lista[0]  


for n in range (3):
    if lista[1]< menor :
        menor= lista[1]
    elif lista[2]< menor:
        menor = lista[2]    
print("O menor número é: ", menor)  