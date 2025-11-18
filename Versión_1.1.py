#Versión 1.1
# El programa tiene un menú interactivo para registrar pedidos

# Lista global donde se guardarán todos los pedidos registrados
pedidos = []

# Función para registrar un pedido

def registrar_pedido():
    # Solicita el nombre del cliente
    nombre = input("Nombre del cliente: ")

    # Solicita el pedido que hizo el cliente
    pedido = input("¿Qué pidió?: ")

    # Pregunta si el cliente ya pagó
    # .strip() elimina espacios extra
    # .lower() convierte la respuesta a minúsculas
    pago = input("¿Ya pagó? (si/no): ").strip().lower()

    # Verifica si la respuesta fue válida
    if pago == "si":
        estado_pago = True   # Pagado
    elif pago == "no":
        estado_pago = False  # No pagado
    else:
        # Si la respuesta no es válida, se registra como no pagado
        print("Respuesta inválida. Se registrará como no pagado.")
        estado_pago = False

    # Crea un diccionario con la información del pedido
    pedido_info = {
        "cliente": nombre,
        "pedido": pedido,
        "pagado": estado_pago
    }

    # Agrega el pedido a la lista global
    pedidos.append(pedido_info)

    # Muestra la información registrada
    print("\nPedido registrado:")
    print(f"Cliente: {pedido_info['cliente']}")
    print(f"Pedido: {pedido_info['pedido']}")
    print(f"Pagado: {'si' if pedido_info['pagado'] else 'no'}")

    # Mensaje adicional según el estado del pago
    if pedido_info['pagado']:
        print("Bien! tu pedido está confirmado :D")
    else:
        print("Por favor pasa a pagar -_-")

# Función para mostrar todos los pedidos
def mostrar_pedidos():
    # Si la lista está vacía, avisa
    if not pedidos:
        print("\nNo hay pedidos registrados todavía.")
    else:
        # Recorre la lista y muestra cada pedido
        print("\n--- Lista de pedidos ---")
        for i, p in enumerate(pedidos, start=1):
            print(f"{i}. Cliente: {p['cliente']} | Pedido: {p['pedido']} | Pagado: {'si' if p['pagado'] else 'no'}")


# Función del menú principal
def menu():
    # Bucle infinito hasta que el usuario elija salir
    while True:
        print("\n--- MENÚ ---")
        print("1. Registrar pedido")
        print("2. Mostrar pedidos")
        print("3. Salir")

        # Solicita la opción al usuario
        opcion = input("Elige una opción: ")

        # Ejecuta la acción según la opción elegida
        if opcion == "1":
            registrar_pedido()
        elif opcion == "2":
            mostrar_pedidos()
        elif opcion == "3":
            print("Su pedido estara pronto... ¡Hasta luego!")
            break   # Rompe el bucle y termina el programa
        else:
            # Si la opción no es válida
            print("Opción inválida, intenta de nuevo.")

# Punto de entrada del programa
menu()