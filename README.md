# 🔐 Proyecto Semana 5 – Encriptación Básica con Python

Este proyecto de **Code Hers** te enseña los fundamentos de la encriptación mediante un ejemplo real en Python usando la librería `cryptography`. Aprenderás cómo cifrar y descifrar mensajes de forma segura, usando claves generadas aleatoriamente.

> 💡 Este es el primer paso hacia un encriptador de archivos personalizado que crearemos en la segunda parte.

---

## 📚 ¿Qué aprenderás?

- Qué es la encriptación y por qué se usa
- Cómo funciona el cifrado simétrico
- Cómo usar `Fernet` de la librería `cryptography` en Python
- Cómo crear scripts seguros y legibles desde cero

---

## ⚙️ Requisitos

- Python 3.8 o superior
- pip
- Terminal o VSCode
- Librería `cryptography`

---

## 🛠️ Instalación paso a paso

```bash
# 1. Clona el repositorio
git clone https://github.com/adletgamer/encriptador-python
cd encriptador-python-basico

# 2. Crea entorno virtual
py -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux

# 3. Instala dependencia
pip install cryptography

# 4. Guarda dependencias (opcional)
pip freeze > requirements.txt
