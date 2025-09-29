def getVars():
    vet = []
    NOME_ARQUIVO_TXT = "variaveisSec.txt"
    try:
        with open(NOME_ARQUIVO_TXT, 'r', encoding='utf-8') as f:
            vet = [line.strip() for line in f if line.strip()]
        if vet:
            print(f"--> {len(vet)} nomes de colunas carregados para o vetor.\n")
        else:
            print(f"--> ERRO: O arquivo '{NOME_ARQUIVO_TXT}' está vazio. O script não pode continuar.")
            exit()
    except FileNotFoundError:
        print(f"--> ERRO: O arquivo '{NOME_ARQUIVO_TXT}' não foi encontrado neste diretório.")
        print("Por favor, certifique-se de que o arquivo está na mesma pasta que o script.")
        exit()

    return vet

