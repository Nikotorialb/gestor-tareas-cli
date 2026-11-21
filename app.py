# Gestor de Tareas CLI

tareas = []


def mostrar_menu():
    print("\n=== GESTOR DE TAREAS ===")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")


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


def completar_tarea():
    if not tareas:
        print("No hay tareas registradas.")
        return

    listar_tareas()

    try:
        numero = int(input("Ingrese el número de tarea a completar: "))

        if 1 <= numero <= len(tareas):
            tareas[numero - 1]["completada"] = True
            print("Tarea completada correctamente.")
        else:
            print("Número de tarea no válido.")

    except ValueError:
        print("Debe ingresar un número válido.")


def eliminar_tarea():
    if not tareas:
        print("No hay tareas registradas.")
        return

    listar_tareas()

    try:
        numero = int(input("Ingrese el número de tarea a eliminar: "))

        if 1 <= numero <= len(tareas):
            eliminada = tareas.pop(numero - 1)
            print(f"Tarea '{eliminada['titulo']}' eliminada.")
        else:
            print("Número de tarea no válido.")

    except ValueError:
        print("Debe ingresar un número válido.")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            completar_tarea()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
