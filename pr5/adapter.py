from abc import ABC, abstractmethod

class LightControlInterface(ABC):
    @abstractmethod
    def turn_on_light(self) -> None:
        pass

    @abstractmethod
    def turn_off_light(self) -> None:
        pass

class HttpLightControl(LightControlInterface):
    def turn_on_light(self) -> None:
        print("Включить свет через HTTP")

    def turn_off_light(self) -> None:
        print("Выключить свет через HTTP")

class WebSocketLightControl(LightControlInterface):
    def turn_on_light(self) -> None:
        print("Включить свет через WebSocket")

    def turn_off_light(self) -> None:
        print("Выключить свет через WebSocket")
class HttpToWebSocketAdapter(LightControlInterface):
    def __init__(self, http_control: HttpLightControl, websocket_control: Web-SocketLightControl):
        self.http_control = http_control
        self.websocket_control = websocket_control

    def turn_on_light(self) -> None:
        self.http_control.turn_on_light()
        self.websocket_control.turn_on_light()

    def turn_off_light(self) -> None:
        self.http_control.turn_off_light()
        self.websocket_control.turn_off_light()
def main():
    http_control = HttpLightControl()
    websocket_control = WebSocketLightControl()
    adapter = HttpToWebSocketAdapter(http_control, websocket_control)

    adapter.turn_on_light()
    adapter.turn_off_light()

if __name__ == "__main__":
    main()
