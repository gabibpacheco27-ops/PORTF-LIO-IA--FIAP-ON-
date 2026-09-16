# ==========================================
# FARMTECH SOLUTIONS - SISTEMA DE GESTÃO AGRÍCOLA
# Culturas: Mandioca e Laranja
# ==========================================

# Vetores globais para armazenamento dos dados
vetor_cultura = []
vetor_area = []
vetor_insumo = []
vetor_litros = []


def exibir_menu():
    print("\n==============================")
    print("   FARMTECH SOLUTIONS - MENU  ")
    print("==============================")
    print("1. Entrada de dados")
    print("2. Exibir dados cadastrados")
    print("3. Atualizar dados")
    print("4. Deletar dados")
    print("5. Sair do programa")
    print("==============================")


def entrada_dados():
    print("\n--- CADASTRO DE ÁREA E INSUMOS ---")
    print("Culturas disponíveis: 1. Mandioca | 2. Laranja")

    escolha_cultura = input("Escolha a cultura (Mandioca/Laranja): ").strip().capitalize()

    if escolha_cultura not in ["Mandioca", "Laranja"]:
        print("Erro: Cultura inválida! Escolha entre Mandioca ou Laranja.")
        return

    # Cálculo da área de plantio baseado em figura geométrica
    print(
        "\n Agora, calcularemos a área de plantio baseando- se na figura geométrica quadrado:"
    )
    print(" QuadradO (Base ˆ2 )")

    area = 0.0
    base = float(input("Digite a base da plantação (metros): "))
    altura = float(input("Digite a altura da plantação (metros): "))
    area = base **2
    
    # Manejo de insumos
    insumo = input(
        "Digite o nome do insumo (ex: Adubo NPK, Fosfato, Defensivo): "
    ).strip()
    taxa_aplicacao = float(
        input("Digite a quantidade de insumo por metro (ex: em litros ou kg): ")
    )
    ruas = int(input("Digite o número de ruas/fileiras da lavoura: "))

    # Cálculo total de litros/insumo necessário considerando as ruas
    total_insumo = taxa_aplicacao * area * ruas

    # Adicionando aos vetores
    vetor_cultura.append(escolha_cultura)
    vetor_area.append(round(area, 2))
    vetor_insumo.append(insumo)
    vetor_litros.append(round(total_insumo, 2))

    print("\nDados cadastrados com sucesso!")


def saida_dados():
    print("\n--- RELATÓRIO DE DADOS CADASTRADOS ---")
    if len(vetor_cultura) == 0:
        print("Nenhum registro encontrado no sistema.")
        return

    for i in range(len(vetor_cultura)):
        print(f"Registro [{i}]")
        print(f"  - Cultura: {vetor_cultura[i]}")
        print(f"  - Área Calculada: {vetor_area[i]} m²")
        print(f"  - Insumo Utilizado: {vetor_insumo[i]}")
        print(f"  - Total de Insumo Necessário: {vetor_litros[i]} unidades/litros")
        print("-" * 40)


def atualizar_dados():
    saida_dados()
    if len(vetor_cultura) == 0:
        return

    indice = int(
        input("Digite o índice do registro que deseja atualizar: ")
    )
    if 0 <= indice < len(vetor_cultura):
        print(
            f"Atualizando registro {indice}. Insira os novos dados:"
        )
        nova_cultura = (
            input("Nova cultura (Mandioca/Laranja): ").strip().capitalize()
        )
        if nova_cultura in ["Mandioca", "Laranja"]:
            vetor_cultura[indice] = nova_cultura

        vetor_area[indice] = float(input("Nova área (m²): "))
        vetor_insumo[indice] = input("Novo insumo: ").strip()
        vetor_litros[indice] = float(
            input("Novo cálculo total de insumo/litros: ")
        )
        print("Registro atualizado com sucesso!")
    else:
        print("Índice inválido!")


def deletar_dados():
    saida_dados()
    if len(vetor_cultura) == 0:
        return

    indice = int(input("Digite o índice do registro que deseja deletar: "))
    if 0 <= indice < len(vetor_cultura):
        vetor_cultura.pop(indice)
        vetor_area.pop(indice)
        vetor_insumo.pop(indice)
        vetor_litros.pop(indice)
        print("Registro removido com sucesso!")
    else:
        print("Índice inválido!")


# Loop principal do programa
def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            entrada_dados()
        elif opcao == "2":
            saida_dados()
        elif opcao == "3":
            atualizar_dados()
        elif opcao == "4":
            deletar_dados()
        elif opcao == "5":
            print("Saindo do programa da FarmTech Solutions. Até logo!")
            break
        else:
            print("Opção inválida! Escolha uma opção entre 1 e 5.")


if __name__ == "__main__":
    main()