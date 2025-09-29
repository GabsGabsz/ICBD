import os

# --------------------------------------------------------------------------
# Este script procura automaticamente pelo primeiro arquivo .txt no diretório
# em que ele é executado e extrai cada linha para uma lista (vetor).
# --------------------------------------------------------------------------

# Variável para guardar o nome do arquivo que encontrarmos.
arquivo_txt_encontrado = "variaveisSec.txt"

# os.listdir('.') lista todos os arquivos e pastas no diretório atual.
print("Procurando por um arquivo .txt no diretório atual...")
for nome_do_arquivo in os.listdir('.'):
    # Verificamos se o nome do arquivo termina com '.txt'.
    if nome_do_arquivo.endswith('.txt'):
        arquivo_txt_encontrado = nome_do_arquivo
        # Assim que encontrarmos o primeiro, paramos a busca.
        break

# Agora, verificamos se encontramos algum arquivo.
if arquivo_txt_encontrado:
    print(f"Arquivo encontrado! Analisando: '{arquivo_txt_encontrado}'\n")
    try:
        # Cria a lista (vetor) vazia.
        nomes_vetor = []
        
        # Abre o arquivo encontrado para leitura.
        with open(arquivo_txt_encontrado, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                # Limpa a linha de espaços e quebras de linha.
                nome_limpo = linha.strip()
                # Adiciona à lista apenas se a linha não estiver vazia.
                if nome_limpo:
                    nomes_vetor.append(nome_limpo)

        # Imprime o resultado final.
        print("Conteúdo do arquivo armazenado no vetor:")
        print(nomes_vetor)
        print(f"\nTotal de {len(nomes_vetor)} itens adicionados.")

    except Exception as e:
        print(f"Ocorreu um erro ao tentar ler o arquivo: {e}")
else:
    # Se o loop terminar e a variável 'arquivo_txt_encontrado' continuar vazia.
    print("Erro: Nenhum arquivo com a extensão .txt foi encontrado neste diretório.")