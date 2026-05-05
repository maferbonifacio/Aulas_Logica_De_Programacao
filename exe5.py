import random
while True:
    numero1 = random.randint(0,10)
    numero2 = random.randint(0,10)

    print("Você escolheu os números", numero1,"e",numero2)
    
    mult = int(input("Qual é a multiplicação desses dois números?: "))
    resul = numero1 * numero2
    
    if mult == resul:
        print("ACERTOU!")
    else:
        print("ERROU!") 
        
    



