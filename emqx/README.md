- [Get Started with EMQX](https://docs.emqx.com/en/emqx/latest/getting-started/getting-started.html)

### Getting started

```sql
CREATE TABLE mqtt_messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    topic VARCHAR(255) NOT NULL,
    payload TEXT NOT NULL,
    qos TINYINT NOT NULL,
    client_id VARCHAR(255) NOT NULL,
    received_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

* login

```
admin
public
```
