n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media =(n1+n2+n3+n4)/4
print(media)

if media>= 5:
    print("Aluno aprovado com media: ", media)
else:
    print("aluno reprovado com media: ", media)