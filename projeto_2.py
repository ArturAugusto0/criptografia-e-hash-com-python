import hashlib
import secrets

class CofreSenhas:
    def __init__(self):
        self.banco_usuarios = {}

    def cadastrar_usuario(self, usuario: str, senha: str) -> None:
        salt = secrets.token_bytes(16)
        chave_derivada = hashlib.pbkdf2_hmac(
            hash_name="sha256",
            password=senha.encode("utf-8"),
            salt=salt,
            iterations=100_000
        )
        self.banco_usuarios[usuario] = {
            "salt": salt.hex(),
            "hash": chave_derivada.hex()
        }

    def autenticar(self, usuario: str, senha_digitada: str) -> bool:
        if usuario not in self.banco_usuarios:
            return False

        registro = self.banco_usuarios[usuario]
        salt = bytes.fromhex(registro["salt"])
        hash_salvo = registro["hash"]

        novo_hash = hashlib.pbkdf2_hmac(
            hash_name="sha256",
            password=senha_digitada.encode("utf-8"),
            salt=salt,
            iterations=100_000
        ).hex()

        return secrets.compare_digest(novo_hash, hash_salvo)

# Simulação de uso
cofre = CofreSenhas()
cofre.cadastrar_usuario("admin", "SenhaForte#2026")

print("Login com senha correta:", cofre.autenticar("admin", "SenhaForte#2026"))
print("Login com senha errada:", cofre.autenticar("admin", "SenhaErrada123"))
