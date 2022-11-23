ladoA = 5
ladoB = 3
ladoC = 7

if ladoA != ladoB and ladoA != ladoC:
    print("Escaleno")
if ladoA == ladoB and ladoA == ladoC: 
    print("Equilátero")  
elif (ladoA == ladoB) or (ladoB==ladoC) or (ladoC==ladoA):
    print("isóceles")    