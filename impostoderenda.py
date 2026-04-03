print("Calcule o seu Imposto de Renda!")
print("Mudanças em vigor desde 1 de Janeiro de 2026 - Receita Federal")
salario=float(input("Digite o seu salário:"))

if salario <= 2428.80:
    print("Você está Isento!")
    
elif 2428.81 <= salario <= 2826.65:
    desconto = (salario * 0.075) - (182.16) 
    descontofinal = desconto - 312.89
    
    if descontofinal < 0:
            descontofinal = 0
            
    print("Após a contagem com a Alíquota e Dedução, o valor ficou",desconto,"reais, porém, com o Desconto, você terá que pagar um valor de",descontofinal,"reais.")
    
    
elif 2826.66 <= salario <= 3751.05:    
    desconto = (salario * 0.15) - (394.16) 
    descontofinal = desconto - 312.89
   
    if descontofinal < 0:
            descontofinal = 0
            
    print("Após a contagem com a Alíquota e Dedução, você terá que pagar um valor de", desconto,"reais, porém, com o Desconto, você terá que pagar um valor de",descontofinal,"reais.")

    
elif 3751.06 <= salario <= 4664.68:    
    desconto = (salario * 0.225) - (675.49)
    descontofinal = desconto - 312.89
 
    
    if descontofinal < 0:
            descontofinal = 0
            
    print("Após a contagem com a Alíquota e Dedução, você terá que pagar um valor de", desconto,"reais, porém, com o Desconto, você terá que pagar um valor de",descontofinal,"reais.")

    
    
elif 4664.69 <= salario <= 5000.00:    
    desconto = (salario * 0.275) - (908.73)
    descontofinal = desconto - 312.89
    
    if descontofinal < 0:
            descontofinal = 0
            
    print("Após a contagem com a Alíquota e Dedução, você terá que pagar um valor de", desconto,"reais, porém, com o Desconto, você terá que pagar um valor de",descontofinal,"reais.")

    
elif 5000.01 <= salario <= 7350.00:    
    desconto = 978.62 - (0.133145 * salario)

    if desconto < 0:
            desconto = 0
            
    print("Você não será isento, porém, terá um desconto que dimunuirá o valor!")
    print("Após cálculos, seu imposto final é de:",desconto,"reais.")
    
elif salario >= 7350.01:
    print("Seu rendimento ultrapassou o valor de R$ 7.350,01, portanto, você NÃO terá descontos extras!")
    imposto = (salario * 0.275) - 908.73
    print("Como seu salário é superior a R$ 7.350,01 você deverá pagar",imposto,"reais.")
    
else:
    print("Opção inválida!")     