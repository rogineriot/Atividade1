opcao = str(input(print("Digite C para Celcius ou F para Fahrenheit: ")))
# transformacao = 0
# temperatura = 0


if (opcao == "f") or (opcao == "F"):
    temperatura = float(input(("Digite a temperatura em Celsius: ")))
    transformacao = (temperatura*9 + 160)/5
elif   (opcao == "c") or (opcao == "C"):
    temperatura = float(input(("Digite a temperatura em Fahrenheit: ")))
    transformacao = (5*temperatura - 160)/9 
print(transformacao)    