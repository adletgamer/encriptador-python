from cryptography.fernet import Fernet

with open("clave.key","rb") as archivo_clave:
    clave=archivo_clave.read()

cifrador=Fernet(clave)

with open("archivo.txt","rb") as archivo:
    datos_cifrados=archivo.read()

datos_desencriptados=cifrador.decrypt(datos_cifrados)

with open("archivo.txt","wb") as archivo:
    archivo.write(datos_desencriptados)

print("[🔓] Archivo desencriptado")