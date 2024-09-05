# Topic Consumer

from channels.consumer import SyncConsumer , AsyncConsumer

class MySyncConsumer(SyncConsumer):

    def websocket_connect(self,event):
        print("Websocket connected...")

    def websocket_receive(self,event):
        print("Message received...")

    def websocket_disconnect(self,event):
        print("Websocket Disconnected...")


class MyAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self,event):
        print("Websocket connected...")

    async def websocket_receive(self,event):
        print("Message received...")

    async def websocket_disconnect(self,event):
        print("Websocket Disconnected...")
