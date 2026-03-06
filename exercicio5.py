def obter_populacao_inicial():
    while True:
        try:
            populacao = int(input("Digite a população inicial (número inteiro): "))
            if populacao > 0:
                return populacao
            else:
                print("A população inicial deve ser maior que zero.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

def obter_taxa_crescimento():
    while True:
        try:
            taxa = float(input("Digite a taxa de crescimento anual (em %): "))
            if 0 < taxa <= 100:
                return taxa / 100  
            else:
                print("A taxa de crescimento deve ser entre 0 e 100.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def calcular_populacao(populacao_inicial, taxa_crescimento, anos):
    return populacao_inicial * (1 + taxa_crescimento) ** anos

def main():
    while True:
        print("\n--- Modelo de Crescimento Populacional ---")
        populacao_inicial = obter_populacao_inicial()
        taxa_crescimento = obter_taxa_crescimento()
        anos = int(input("Digite o número de anos para projeção: "))
        
        populacao_final = calcular_populacao(populacao_inicial, taxa_crescimento, anos)
        print(f"\nPopulação após {anos} anos: {populacao_final:.0f}")

        repetir = input("\nDeseja realizar outra projeção? (s/n): ").strip().lower()
        if repetir != 's':
            print("Obrigado por utilizar o programa!")
            break

if __name__ == "__main__":
    main()
