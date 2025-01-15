import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "test/topic"


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


def on_message(client, userdata, msg):
    print(f"Message received on topic {msg.topic}: {msg.payload.decode()}")


def on_subscribe(client, userdata, mid, granted_qos):
    print(f"Subscribed to topic with mid={mid}, granted_qos={granted_qos}")


client = mqtt.Client()
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
