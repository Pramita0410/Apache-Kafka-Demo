from kafka import KafkaConsumer
import json
group_id = "food-item-group1"

consumer = KafkaConsumer(
 client_id = "client1",
 group_id = group_id,
 bootstrap_servers = "172.31.55.197:9092",

 value_deserializer = lambda v: json.loads(v.decode('ascii')),
 key_deserializer = lambda v: json.loads(v.decode('ascii')),
 max_poll_records = 10
)

consumer.subscribe(topics=["food-delivery-updates"])


for message in consumer:
    print ("%d:%d: k=%s v=%s" % (message.partition,
                                 message.offset,
                                 message.key,
                                 message.value))