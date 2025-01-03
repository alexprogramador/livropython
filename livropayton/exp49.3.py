def calcula_nota():
    while True:
        try:
            pontuacao = input("Digite a Pontuação: ")
            pontuacao = float(pontuacao)

            if pontuacao < 0.0 or pontuacao > 1.0:
                print("Pontuação Inválida")
            else:
                if pontuacao >= 0.9:
                    print("A")
                elif pontuacao >= 0.8:
                    print("B")
                elif pontuacao >= 0.7:
                    print("C")
                elif pontuacao >= 0.6:
                    print("D")
                else:
                    print("F")
        except ValueError:
            print("Pontuação Inválida")

# Testando o programa com diferentes valores de entrada
calcula_nota()