# Gestor de Tareas CLI

tareas = []


def mostrar_menu():
    print("\n=== GESTOR DE TAREAS AVANZADAS ===")
    print("1. Completar tarea")
    print("2. Eliminar tarea")
    print("3. Salir")


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


def listar_tareas():
    for i, tarea in enumerate(tareas, start=1):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        print(f"{i}. {tarea['titulo']} - {estado}")


def main():
    mostrar_menu()


if __name__ == "__main__":
    main()
