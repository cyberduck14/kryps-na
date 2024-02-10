import math

# coleta de dados
h = str(input('digite h para calcular hipoternusa e para calcular o Cateto qualquer letrar: '))

if h =='h':
    c1 = int(input('escreva o valor do cateto 1: '))
    c2 = int(input('escreva o cateto 2: '))

    # calculo
    r = c1**2 + c2**2
    r1 = math.sqrt(r)

    # resposta
    print(f'o resultado do quadrado da hipoternusa e: {r}^2')
    print(f'o resultado da hipoternusa e:{r1}')
    input('')
    
else:
    h1 = int(input('Valor da Hipotenusa: '))
    c1 = int(input('Valor do Cateto: '))

# Calculo
    r1 = h1**2 - c1**2
    r2 = math.sqrt(r1)
    
# Resposta
    print(f'Valor do Cateto ao Quadrado: {r1}')
    print(f'Valor da Reta do Cateto: {r2}')
    input('')