# Uncomment this to pass the first stage
import socket
import threading


def handle_client(conn, msg):
    with conn:
        conn.recv(1024)  # receiving 1024 bytes
        conn.send(msg.encode())
        while True:
            message = conn.recv(1024)
            if not message:
                break
            conn.send(msg.encode())


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    # server_socket.accept() # wait for client

    while True:
        conn, addr = server_socket.accept()
        msg = "+PONG\r\n"
        # for every new connection we get, we create a thread
        thread = threading.Thread(target=handle_client, args=(conn, msg))
        thread.start()


if __name__ == "__main__":
    main()
