# Versión 1
# Este programa registra el nombre del cliente, su pedido y si ya pagó.
# Definimos una función llamada "registrar_pedido"

def registrar_pedido():
    # Solicita el nombre del cliente y lo guarda en la variable "nombre"
    nombre = input("Nombre del cliente: ")

    # Solicita el pedido que hizo el cliente y lo guarda en la variable "pedido"
    pedido = input("¿Qué pidió?: ")

    # Pregunta si el cliente ya pagó
    # .strip() elimina espacios extra al inicio/fin
    # .lower() convierte la respuesta a minúsculas para evitar errores xd
    pago = input("¿Ya pagó? (si/no): ").strip().lower()

    # Verifica si la respuesta fue "sí" o "no"
    # Si fue "Sí", se guarda como True (pagado)
    # Si fue "No", se guarda como False (no pagado)
    if pago == "si":
        estado_pago = True
    elif pago == "no":
        estado_pago = False
    else:
        # Si la respuesta no es válida, se registra como no pagado
        print("Respuesta inválida. Se registrará como no pagado.")
        estado_pago = False

    # Crea un diccionario (estructura clave-valor) con la información del pedido
    # Esto permite guardar los datos de forma organizada
    pedido_info = {
        "cliente": nombre,
        "pedido": pedido,
        "pagado": estado_pago
    }

    # Muestra la información registrada en pantalla
    print("\nPedido registrado:")
    print(f"Cliente: {pedido_info['cliente']}")
    print(f"Pedido: {pedido_info['pedido']}")
    print(f"Pagado: {'si' if pedido_info['pagado'] else 'no'}")

    # Mensaje adicional según el estado del pago
    # Si ya pagó → mensaje de confirmación
    # Si no ha pagado → mensaje para que pase a pagar
    if pedido_info['pagado']:
        print("Bien! tu pedido está confirmado :D")
    else:
        print("Por favor pasa a pagar -_-")

# Llama a la función para ejecutar el registro de pedido
registrar_pedido()