import socket
import threading

def handle_client(client_socket, address):
    print(f"Cliente conectado desde {address}")
    while True:
        data = client_socket.recv(1024).decode('utf-8').strip()
        if not data or data == "quit":
            break
        try:
            num1, num2, operation = data.split(',')
            num1, num2 = float(num1), float(num2)
            if operation == "add":
                result = num1 + num2
            elif operation == "sub":
                result = num1 - num2
            elif operation == "mul":
                result = num1 * num2
            elif operation == "div":
                if num2 == 0:
                    raise ValueError("División por cero")
                result = num1 / num2
            else:
                raise ValueError("Operación desconocida")
            response = f"RESULT:{result}"
        except ValueError as e:
            response = f"ERROR:{str(e)}"
        client_socket.send(response.encode('utf-8'))
    print(f"Cliente desconectado desde {address}")
    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('172.17.130.182', 5000))  # Escucha en todas las interfaces
server.listen(5)
print("Servidor escuchando en el puerto 5000...")

while True:
    client_socket, address = server.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
    client_thread.start()