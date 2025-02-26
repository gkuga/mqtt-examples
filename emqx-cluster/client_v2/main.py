import paho.mqtt.client as mqtt

BROKER = ""
PORT = 8883
TOPIC = "test/topic"


def on_connect(client, userdata, flags, reason_code, properties):
    print("Connected with result code " + str(reason_code))


def on_message(client, userdata, msg):
    print(f"Message received on topic {msg.topic}: {msg.payload.decode()}")


def on_subscribe(client, userdata, mid, reason_code, properties):
    print(f"Subscribed to topic with mid={mid}, reason_code={reason_code}")


client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.tls_set()
client.username_pw_set("", "")
client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe


try:
    client.connect(BROKER, PORT, 60)
    client.subscribe(TOPIC)
except Exception as e:
    print(f"Could not connect to broker: {e}")
    exit(1)

client.loop_start()

try:
    while True:
        message = input("Enter message to send (or 'exit' to quit): ")
        if message.lower() == "exit":
            break
        client.publish(TOPIC, message)
except KeyboardInterrupt:
    print("\nExiting...")
finally:
    client.loop_stop()
    print("Disconnected from broker.")
