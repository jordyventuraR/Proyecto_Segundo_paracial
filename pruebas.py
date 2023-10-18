from cryptography.fernet import Fernet

# Aquí debes insertar tu clave en el formato de bytes
clave = b'd3iXJXBhYZ0ZasXWw_lIafJ3HyDHZoAmsD7ysmEbjtA='
fernet = Fernet(clave)

mensaje_cifrado  = b'gAAAAABlL0LB1CAofOzkVR0SGYHEjQ_t_15oLsXj-rhXpPlDU8mCkVsb5MriqdP_QY3CF8SYAhJ9aeWHussMdK_Svn9cydF5Ug=='
mensaje_cifrado2 = b'gAAAAABlL0axtR8wDNb0ZToO0Qn1B-bUjexM5_sEoQAX_mJzEM5rtTqhCtfc5VcTCZzRuTKWwBXbjYFeiPE6Z0j1kWcFtsYCXQ=='

mensaje_descifrado = fernet.decrypt(mensaje_cifrado)
mensaje_descifrado2 = fernet.decrypt(mensaje_cifrado2)
print(mensaje_descifrado)
print(mensaje_descifrado2)
