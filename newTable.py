import sqlite3
import getVarSelect
import time # Para medir o tempo de execução

# --- 1. CONFIGURAÇÃO ---
NOME_BANCO_DE_DADOS = "BD_ORIGIN.db"
NOME_DA_TABELA = "filtred" # Tabela de onde os registros serão apagados

# --- 2. CARREGAR NOMES DAS COLUNAS ---
# Usando seu módulo para obter a lista de colunas que não podem ser nulas.
print("Passo 1: Lendo o arquivo de colunas...")
try:
    colunas_para_verificar = getVarSelect.getVars()
    print(f"--> {len(colunas_para_verificar)} nomes de colunas carregados.")
except FileNotFoundError:
    print(f"--> ERRO: Arquivo de variáveis não encontrado.")
    exit()

# --- 3. CONSTRUIR E EXECUTAR A CONSULTA SQL ---
try:
    # Conecta ao banco de dados. O timeout ajuda a evitar erros de 'database is locked'
    # em outras situações, embora aqui não seja o problema principal.
    conn = sqlite3.connect(NOME_BANCO_DE_DADOS, timeout=10)
    cursor = conn.cursor()
    print("\nPasso 2: Conexão com o banco de dados bem-sucedida.")

    # Constrói a cláusula WHERE dinamicamente.
    # A lógica é: apague a linha se a 'coluna1' É NULA OU a 'coluna2' É NULA OU...
    clausula_where = " OR ".join(f'"{coluna}" IS NULL' for coluna in colunas_para_verificar)

    # Monta o comando DELETE completo. Este é o único comando que precisamos.
    consulta_sql = f"DELETE FROM {NOME_DA_TABELA} WHERE {clausula_where};"

    print("\nPasso 3: Executando o comando para apagar registros incompletos...")
    # print(f"Comando SQL a ser executado: {consulta_sql}") # Descomente se quiser ver o comando
    
    start_time = time.time()
    cursor.execute(consulta_sql)

    # Verifica quantos registros foram afetados (apagados)
    registros_apagados = cursor.rowcount
    
    # Salva (commita) TODAS as alterações de uma vez só, no final.
    conn.commit()
    end_time = time.time()
    
    print("\n--- RESULTADO ---")
    print(f"Operação concluída em {end_time - start_time:.2f} segundos.")
    print(f"Sucesso! {registros_apagados} registros com valores nulos foram apagados.")

except sqlite3.Error as e:
    print(f"\nOcorreu um erro no banco de dados: {e}")
    # Se der erro, desfaz qualquer alteração que estivesse pendente
    if conn:
        conn.rollback()
finally:
    # Garante que a conexão seja sempre fechada
    if conn:
        conn.close()
        print("Conexão com o banco de dados fechada.")