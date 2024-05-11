from kafka import KafkaProducer
import json


producer = KafkaProducer(
        bootstrap_servers="172.31.55.197:9092",
        value_serializer=lambda v: json.dumps(v).encode('ascii'),
        key_serializer=lambda v: json.dumps(v).encode('ascii')   
    )
topic_name = "rider-updates"

producer.send(
 topic_name,
 key={"id":1},
 value={"name":"👨 Francesco", "pizza":"Margherita 🍕"}
)
producer.send(
 topic_name,
 key={"id":2},
 value={"name":"👩 Adele", "pizza":"Hawaii 🍕+🍍+🥓"}
)

producer.send(
 topic_name,
 key={"id":3},
 value={"name":"👦 Mark", "pizza":"Choccolate 🍕+🍫"}
)

producer.flush()