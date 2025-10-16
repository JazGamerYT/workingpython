import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5000))  # Cambia 'localhost' por la IP del servidor para red

while True:
    print("\nMenú de Operaciones:")
    print("1. Suma (add)")
    print("2. Resta (sub)")
    print("3. Multiplicación (mul)")
    print("4. División (div)")
    print("5. Salir (quit)")
    
    choice = input("Elige una opción (1-5): ")
    if choice == "5":
        client.send("quit".encode('utf-8'))
        break
    
    if choice in ["1", "2", "3", "4"]:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        operations = {"1": "add", "2": "sub", "3": "mul", "4": "div"}
        operation = operations[choice]
        request = f"{num1},{num2},{operation}"
        client.send(request.encode('utf-8'))
        response = client.recv(1024).decode('utf-8')
        print(f"Respuesta del servidor: {response}")
    else:
        print("Opción inválida, intenta de nuevo.")

client.close()