import websocket
import threading


def on_message(ws, message):
    print(f"Получено сообщение: {message}")


def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("Соединение закрыто")


def on_open(ws):
    print("Соединение установлено!")

    def run(*args):
        while True:
            command = input("Введите команду: ")
            ws.send(command)

    threading.Thread(target=run).start()


if __name__ == "__main__":
    ws = websocket.WebSocketApp("ws://127.0.0.1:8000/ws",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()
