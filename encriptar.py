from cryptography.fernet import Fernet
#Leer clave
with open("clave.key","rb") as archivo_clave:
    clave=archivo_clave.read()

cifrador=Fernet(clave)

#Leer archivo
with open("archivo.txt","rb") as archivo:
    datos=archivo.read()

#Encriptado de archivo
datos_encriptados=cifrador.encrypt(datos)

#Sobrescribir archivo cifrado

with open("archivo.txt","wb") as archivo:
    archivo.write(datos_encriptados)

print("[🔒] Archivo encriptado")