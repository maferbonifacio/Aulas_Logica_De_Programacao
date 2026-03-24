dias = int(input("Escreva a quantidade de dias: "))
horas = int(input("Escreva a quantidade de horas: "))
minutos = int(input("Escreva a quantidade de minutos: "))
segundos = int(input("Escreva a quantidade de segundos: "))

dias = dias * 24 * 60 * 60
horas = horas * 60 * 60
minutos = minutos * 60

total = dias + horas + minutos + segundos

print("O total em segundos é:",segundos)
