notas = []

print("Digite as 5 notas")
for i in range(5):
   print("Digite a nota",(i+1))
   n = eval(input())
   notas.append(n)
soma = sum(notas)
media = soma/5
print("A soma das notas é: ", soma)
print("A media do aluno é: ", media)    
  
for i in range(5):
    if notas[i]> media:
        maior = notas[i]
        print(maior)