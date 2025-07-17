from cryptography.fernet import Fernet

clave = Fernet.generate_key()

with open("clave.key", "wb") as archivo_clave:
    archivo_clave.write(clave)

print("[✔] Clave generada y guardada como 'clave.key'")
