import hashlib

hash_file = "a61e916cc98800aef12959a2563fddd4"

file_Path = input("Ingrese la direccion del archivo de el diccionario: ")

with open(file_Path, 'r') as file:

    diccionary = [line.strip() for line in file]

    for password in diccionary:
        
        hash = hashlib.md5(password.encode()).hexdigest()
        
        if hash == hash_file:
            
            print("La contraseña es: " + password)
            break
        else:
            print("No se encontraron coincidencias")