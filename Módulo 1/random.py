# Valores aleatórios com random



 # Gera um valor de 0.0 a 1.0
print(random.random())

# Gera um valor decimal de Valor Mínimo ao Valor Máximo
print(random.uniform(4, 10)) 

#Gera um valor inteiro de Valor Mínimo ao Valor Máximo
print(random.randint(4, 10)) 

# Gera valor aleatório de uma lista
core = ['verde', 'vermelho', 'azul']
print(random.choice(cores, k=2)) #com duas opções

# Embaralhar valores
cartas_baralho = ['carta1', 'carta2', 'carta3', 'carta4']
print(random.shuffle(cartas_baralho))
print(cartas_baralho)