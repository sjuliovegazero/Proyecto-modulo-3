# Sistema_Gestión_Contactos

# Su creación fue basada en un código pero fue escrita por mi manualmente linea por linea para aprender y trabajar en la sintaxis.

def pedir_contacto():
    nombre = input("Nombre del contacto: ").strip()
    telefono = input("Numero de telefono: ").strip()
    correo = input("Correo electronico: ").strip()
    direccion = input("Ingrese la direccion: ").strip()
    contacto = {
        "nombre": nombre,
        "telefono": telefono,
        "correo": correo,
        "direccion": direccion
    }
    return contacto

def agregar_contacto(contactos):        # Se determino filtar el agregar contactos a todas las categorias por un tema estético de código y para aprender a que se puede hacer.
    print("\n --- AGREGAR CONTACTO ---")
    contacto = pedir_contacto()

    for p in contactos:
        if p["nombre"].strip().lower() == contacto["nombre"].strip().lower() and contacto["nombre"] != "":
            print("Este contacto ya se encuentra en sistema. No se duplicará.")
            return
        
        elif p["telefono"].strip().lower() == contacto["telefono"].strip().lower() and contacto["telefono"] != "":
            print("Este contacto ya se encuentra en sistema. No se duplicará.")
            return
        
        elif p["correo"].strip().lower() == contacto["correo"].strip().lower() and contacto["correo"] != "":
            print("Este contacto ya se encuentra en sistema. No se duplicará.")
            return
        
        elif p["direccion"].strip().lower() == contacto["direccion"].strip().lower() and contacto["direccion"] != "":
            print("Este contacto ya se encuentra en sistema. No se duplicará.")
            return
    
    contactos.append(contacto)
    print("Contacto registrado")

def listar_contactos(contactos):
    print("\n --- LISTA DE CONTACTOS ---")
    if len(contactos) == 0:
        print("No se encuentran contactos registrados")
        return
    
    for i, p in enumerate(contactos):
        print(f"[{i}] {p['nombre']} | {p['telefono']} | {p['correo']} | {p['direccion']}")

def buscar_contacto(contactos):       # Las categorias de busqueda se limitaron a nombre o telefono que es lo que habitualmente usan los usuarios.
    print("\n --- BUSCAR CONTACTO ---")
    texto = input("Buscar contacto por nombre o telefono: ").strip().lower()

    encontrados = 0
    for i, p in enumerate(contactos):
        if (texto in p["nombre"].lower()) or (texto in p ["telefono"].lower()):
            print(f"Resultado busqueda: [{i}] {p['nombre']} | {p['telefono']} | {p['correo']} | {p['direccion']}")
            encontrados += 1
    
    if encontrados == 0:
        print("No se encontró el contacto")

def editar_contacto(contactos):
    print("\n --- EDITAR CONTACTO ---")
    listar_contactos(contactos)

    if len(contactos) == 0:
        return

    idx_txt = input("Índice del contacto a editar: ").strip()
    if not idx_txt.isdigit():
        print("Debes ingresar un número")
        return
    
    idx = int(idx_txt)
    if idx < 0 or idx >= len(contactos):
        print("Índice inválido")
        return
    
    print("\nIngrese los nuevos datos del contacto:")
    contacto_nuevo = pedir_contacto()
    contactos[idx] = contacto_nuevo
    print("Contacto actualizado correctamente")



def eliminar_contacto(contactos):
    print("\n --- ELIMINAR CONTACTO ---")
    listar_contactos(contactos)
    if len(contactos) == 0:
        return

    idx_txt = input("Índice del contacto a eliminar: ").strip()
    if not idx_txt.isdigit():
        print("Debes ingresar un número")
        return
    
    idx = int(idx_txt)
    if idx < 0 or idx >= len(contactos):
        print("Índice inválido")
        return
    eliminado = contactos.pop(idx)
    print("El contacto",eliminado["nombre"],"ha sido eliminado")

def mostrar_menu():
    print("\n --- MENÚ CONTACTOS ---")
    print("1) Agregar un contacto")
    print("2) Listar contactos")
    print("3) Buscar contacto")
    print("4) Editar contacto")
    print("5) Eliminar contacto")
    print("6) Salir")

def main():
    contactos = []

    while True:
        mostrar_menu()
        op = input("Opción: ").strip()

        if op == "1":
            agregar_contacto(contactos)
        elif op == "2":
            listar_contactos(contactos)
        elif op =="3":
            buscar_contacto(contactos)
        elif op == "4":
            editar_contacto(contactos)
        elif op == "5":
            eliminar_contacto(contactos)
        elif op == "6":
            print("Ha salido del sistema")
            break
        else:
            print("Opción no válida, intente nuevamente")
        

if __name__ == "__main__":
    main()