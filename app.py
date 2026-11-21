# Gestor de Tareas CLI

tareas = []


def mostrar_menu():
    print("\n=== GESTOR DE TAREAS - VERSION PRINCIPAL ===")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Salir")


def agregar_tarea():
    titulo = input("Ingrese el nombre de la tarea: ")
    tareas.append({"titulo": titulo, "completada": False})
    print("Tarea agregada correctamente.")


def listar_tareas():
    if not tareas:
        print("No hay tareas registradas.")
        return

    print("\n=== LISTA DE TAREAS ===")

    for i, tarea in enumerate(tareas, start=1):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        print(f"{i}. {tarea['titulo']} - {estado}")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
