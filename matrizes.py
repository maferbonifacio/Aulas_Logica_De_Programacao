import random

M1 = [[1,2,3],[4,5,6]]
print(M1)
print(M1[1][1])
for i in range(3):
        M1[i] = [0] * 3
        print(M1)
        
M2=[[10,20,30], [40,50,60]]
for i in range(2):
    for j in range(3):
        M2[i][j] = random.randin(0,50)
        print(M2) 
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    print("1-exibir numeros aleatorios")
    print("2-exibir a matriz criada")
    print("3-calcular e exibir a soma dos elementos da diagonal principal da matriz")
    print("4-calcular exibir a soma dos elementos da diagonal da matriz")
    print("5-calcular e exibir o determinante da matriz")