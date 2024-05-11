from kafka import KafkaProducer
import json


producer = KafkaProducer(
        bootstrap_servers="172.31.55.197:9092",
        value_serializer=lambda v: json.dumps(v).encode('ascii'),
        key_serializer=lambda v: json.dumps(v).encode('ascii')   
    )
topic_name = "food-delivery-updates"

producer.send(
 topic_name,
 key={"id":0},
 value={"name":"deril", "food-item":"pizza", "price": 15}
)
producer.send(
 topic_name,
 key={"id":1},
 value={"name":"pramita", "food-item":"biryani", "price": 10}
)
producer.flush()