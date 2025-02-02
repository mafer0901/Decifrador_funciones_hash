import hashlib

hash_file = "951skdmxcniiiklñjkcmmpoqqimd55871"

dic_file = input("Ingrse la direccion del archivo del diccionario:")

with open(dic_file, 'r' ) as file:

    diccionario = [ line.strip () for line in file ]

    for password in diccionario:

        hash_calculado = hashlib.sha256(password.encode()).hexdigest()

        if hash_calculado == hash_file :

            print("La contraseña original es: " + password)
            break

        else:
            print("La contraseña no se encuentra")
