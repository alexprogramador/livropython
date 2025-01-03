# Solicitar horas trabalhadas
horas = float(input("Digite as Horas: "))

# Solicitar taxa horária
taxa = float(input("Digite a taxa: "))

# Calcular pagamento
if horas > 40:
    horas_extras = horas - 40
    pagamento = (40 * taxa) + (horas_extras * taxa * 1.5)
else:
    pagamento = horas * taxa

# Exibir pagamento
print("Pagamento:", pagamento)

# usando try e except
def calcula_pagamento():
    try:
        horas = float(input("Digite as Horas: "))
        taxa = float(input("Digite a taxa: "))
        pagamento = horas * taxa
        print("Pagamento:", pagamento)
    except ValueError:
        print("Erro, por favor utilize uma entrada numérica")

calcula_pagamento()