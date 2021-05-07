from datetime import datetime

print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)

# Criar uma data

lancamento_app = datetime(2021, 5, 28)
print(lancamento_app)

# Quero receber a data lançamento do meu app
# dia/mes/ano    -    '%d/%m/%Y'

data_de_lancamento = datetime.strptime(input('Quando devemos lanças o aplicativo?'), '%d/%m/%Y')
print(type(data_de_lancamento))


# Calcular o intervalo entre datas

data_atual = datetime.now()
prazo = data_de_lancamento - data_atual
print(prazo.days)