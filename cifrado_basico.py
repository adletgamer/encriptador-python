from cryptography.fernet import Fernet

#Generar una clave de cifrado
clave=Fernet.generate_key()
print("Clave generada: ",clave)

#Crear un objeto Fernet usando la clave
cifrador=Fernet(clave)

#Definir el mensaje original
mensaje="Hola, este es un mensaje secreto"
print("Mensaje original: ",mensaje)

#Encriptar el mensaje
mensaje_encriptado=cifrador.encrypt(mensaje.encode())
print("Mensaje encriptado: ",mensaje_encriptado)

#Desencriptar mensaje
mensaje_desencriptado=cifrador.decrypt(mensaje_encriptado).decode()
print("Mensaje desencriptado: ",mensaje_desencriptado)