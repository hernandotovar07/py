usuario = { "nombre": "juan", "apellido":"perez", "edad":30}
print ( usuario["nombre"])


usuario["profesion"] = "desarrollador de sotfware"
print(usuario)
listaClaves = usuario.keys()
del usuario ["edad"]
print(listaClaves)