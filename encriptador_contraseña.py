import hashlib
import random
import string
#creo la funcion para generar los hash
def generate_password_hash(password):
    #creo una instancia para asegurarme la longitud de la contraseña sea lña aducuada
    if len(password) < 6 or len(password) > 12:
        raise ValueError("El password debe tener entre 6 y 12 caracteres")

    # Semilla fija para generar la cadena aleatoria
    random.seed(12345)

    # Agregar una cadena aleatoria al final del password para hacerlo más seguro
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
    password = password + random_string

    # Generar el hash MD5 del password
    password_hash = hashlib.md5(password.encode()).hexdigest()

    # Devolver el hash
    return password_hash

print(generate_password_hash("sarabe"))
print(generate_password_hash("sarabe"))
print(generate_password_hash("charolaasa"))
