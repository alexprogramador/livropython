Largura = 17
Altura = 12.0

expressoes = [
    Largura // 2,
    Largura / 2.0,
    Altura / 3,
    1 + 2 * 5
]

for i, expressao in enumerate(expressoes, 1):
    print(f"Expressão {i}: Valor = {expressao}, Tipo = {type(expressao)}")