import paho.mqtt.client as mqtt
import time


def on_publish(client, userdata, mid, reason_code, properties):
    print(f"Message {mid} published! Reason: {reason_code}")


client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.on_publish = on_publish
client.tls_set()
client.username_pw_set("user", "pass")

client.connect("mqtt.blocker.example.com", 8883, 5)

client.loop_start()

result = client.publish("test/topic", "Hello TLS MQTT", qos=1)
result.wait_for_publish()

time.sleep(10)
client.loop_stop()
client.disconnect()
