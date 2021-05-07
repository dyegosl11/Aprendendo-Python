# Calcule quantos dias faltam até o seu aniversário

from datetime import datetime
aniversário = datetime(2021, 9, 11)
dias_para_aniversario = aniversário - datetime.now()
print(dias_para_aniversario)