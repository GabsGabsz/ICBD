def lenIdNull():
    vetIdNulls = []
    with open("../database/idsNull.txt", "r") as f:
        for linha in f:
            vetIdNulls.append(linha.replace("\n",""))

    return vetIdNulls