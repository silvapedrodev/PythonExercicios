from datetime import datetime

worker = dict()
current_year = datetime.now().year

worker['nome'] = str(input("Nome: "))
worker['idade'] = current_year - int(input("Ano de Nascimento: "))
worker['ctps'] = int(input("Carteira de trabalho (0 se não tiver): "))
if worker['ctps'] != 0:
    worker['contratação'] = int(input("Ano de Contratação: "))
    worker['salário'] = float(input("Salário: R$"))
    worker['aposentadoria'] = worker['idade'] + ((worker['contratação'] + 35) - current_year)

print("-=" * 25)
for key, value in worker.items():
    print(f'  - {key} tem o valor {value}')
