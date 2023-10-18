from cryptography.fernet import Fernet

clave_cifrado = Fernet.generate_key()
fernet = Fernet(clave_cifrado)

texto_cifrado = b'gAAAAABlLsTrkw03qYMtotp69BlUoDH27G1VEZYVWFXw8zCJI-GvrYKnJ17HmLkP3-XmVw1hgBxmq9KcoPaULX7FxMzv9lVsug=='
texto_descifrado = fernet.decrypt(texto_cifrado)
print(texto_descifrado)
