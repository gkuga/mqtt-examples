- [Eclipse Mosquitto](https://mosquitto.org/)
- [How to start using Mosquitto](https://www.stackhero.io/en/services/Mosquitto/documentations/Getting-started)

### Testing mosquitto

```console
# Subscriber
docker compose exec broker mosquitto_sub -d -t /#

# Publisher
docker compose exec broker mosquitto_pub -d -t /devices/a -m 'hello world!'
```
