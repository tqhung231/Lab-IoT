import sys

from Adafruit_IO import MQTTClient


class Adafruit_MQTT:
    AIO_FEED_IDs = ["button1", "button2"]
    AIO_USERNAME = "tqhung231"
    # Check if key.txt exists
    try:
        with open("key.txt", "r") as f:
            AIO_KEY = f.read()
    except:
        # Dummy key
        AIO_KEY = "aio_hSTD28Ft6JP4rmstd4f1KnbSwIrM"

    def connected(self, client):
        print("Connected ...")
        for feed in self.AIO_FEED_IDs:
            client.subscribe(feed)

    def subscribe(self, client, userdata, mid, granted_qos):
        print("Subscribeb...")

    def disconnected(self, client):
        print("Disconnected...")
        sys.exit(1)

    def message(self, client, feed_id, payload):
        print("Received: " + payload + " from " + feed_id)

    def __init__(self):
        client = MQTTClient(self.AIO_USERNAME, self.AIO_KEY)
        client.on_connect = self.connected
        client.on_disconnect = self.disconnected
        client.on_message = self.message
        client.on_subscribe = self.subscribe
        client.connect()
        client.loop_background()
        self.client = client
