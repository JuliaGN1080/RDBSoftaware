def fazer_escolha():
    # Exibe as opções para o usuário
    print("Escolha uma das opções abaixo:")
    print("1 - Programação")
    print("2 - Manutenção")
    print("3 - Marketing")
    print("4 - Consultoria de TI")

    # Solicita ao usuário que escolha uma opção
    escolha = input("Digite o número correspondente à sua escolha: ")

    # Verifica a escolha e retorna a resposta correspondente
    if escolha == "1":
        return "Você escolheu Programação."
    elif escolha == "2":
        return "Você escolheu Manutenção."
    elif escolha == "3":
        return "Você escolheu Marketing."
    elif escolha == "4":
        return "Você escolheu Consultoria de TI."
    else:
        return "Opção inválida. Por favor, escolha um número de 1 a 4."
