genero = str(input("Digite o genero, F ou M: "))
print(genero)

if genero == 'f':
    altura = float(input("digite sua altura: "))
    p = (62.1 *altura)-44.7
    print("Seu peso idela é: ", p)
elif genero == 'm':
    altura = float(input("digite sua altura: "))
    p = (72.7*altura)-58
    print("Seu peso idela é: ", p)
else:
    print("Genero inválido")
    
    
    