import hashlib
import os

def calcular_hash_arquivo(caminho_arquivo: str) -> str:
    sha256 = hashlib.sha256()
    with open(caminho_arquivo, "rb") as arquivo:
        for bloco in iter(lambda: arquivo.read(4096), b""):
            sha256.update(bloco)
    return sha256.hexdigest()

def verificar_integridade(caminho_arquivo: str, hash_esperado: str) -> bool:
    hash_atual = calcular_hash_arquivo(caminho_arquivo)
    return hash_atual == hash_esperado.lower()

# Simulação de uso
nome_arquivo = "documento_confidencial.txt"
with open(nome_arquivo, "w", encoding="utf-8") as f:
    f.write("Conteúdo original protegido.")

hash_original = calcular_hash_arquivo(nome_arquivo)
print(f"Hash original: {hash_original}")
print("Arquivo íntegro?", verificar_integridade(nome_arquivo, hash_original))

# Simulando adulteração no arquivo
with open(nome_arquivo, "a", encoding="utf-8") as f:
    f.write(" ")

print("Integridade após alteração:", verificar_integridade(nome_arquivo, hash_original))
os.remove(nome_arquivo)
