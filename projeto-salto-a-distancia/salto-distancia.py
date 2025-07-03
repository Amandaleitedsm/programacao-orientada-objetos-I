# Programa para cálculo de notas de salto em distância

print('Bem-vindo ao cálculo de notas de salto em distância\n')

# Inicializa variáveis para controle do campeão
mediacamp = 0.0
nomecamp = ''
soma = 0.0

# Pergunta se o usuário deseja iniciar o programa
EscolhaInicial = input('Deseja iniciar o programa? (Digite apenas o número referente à resposta)\n'
                       '1 - Sim / 2 - Não\n')

# Validação da escolha inicial
while not EscolhaInicial.isnumeric():
    EscolhaInicial = input('Entrada inválida. Digite apenas 1 ou 2: ')
EscolhaInicial = int(EscolhaInicial)

if EscolhaInicial == 1:
    opc = 1
    while opc == 1:
        # Solicita o nome do atleta
        nome = input('Digite o nome do atleta: ')
        while not nome.isalpha():
            nome = input('Nome inválido. Digite um nome válido.\n')

        # Recebe os 5 saltos do atleta
        for x in range(1, 6):
            salto = input(f'Insira a distância do salto {x}: ')
            while not salto.isnumeric():
                salto = input('Valor inválido. Digite novamente.')
            salto = float(salto)

            # Define maior e menor salto
            if x == 1:
                maior = menor = salto
            if salto > maior:
                maior = salto
            if salto < menor:
                menor = salto
            soma += salto

        # Calcula a média excluindo o maior e o menor salto
        media = (soma - menor - maior) / 3
        soma = 0.0

        # Atualiza o campeão se a média for a maior
        if media > mediacamp or media == mediacamp:
            mediacamp = media
            nomecamp = nome

        # Mostra resultados do atleta
        print(f"\nMelhor salto: {maior} m")
        print(f"Pior salto: {menor} m")
        print(f"Média dos demais saltos: {media:.1f} m\n")
        print(f"Resultado final:\n{nome.capitalize()}: {media:.1f} m\n")

        # Pergunta se deseja continuar
        opc = input("Deseja continuar? (1 - Sim / 2 - Não): ")
        while not opc.isnumeric() or opc not in ('1', '2'):
            opc = input('Opção inválida.Tente novamente: ')
        opc = int(opc)
        print('-'*80)

    # Exibe o atleta com maior média
    if opc == 2:
        print(f'ATLETA CAMPEÃO: {nomecamp.upper()}')

elif EscolhaInicial == 2:
    print('Você escolheu não iniciar.')
else:
    print('Resposta inválida. Digite apenas 1 ou 2.\n')
