
from kafka.admin import KafkaAdminClient, NewTopic


admin = KafkaAdminClient(
        client_id ='admin',
        bootstrap_servers="172.31.55.197:9092",
    )

topic_name_partitioned="food-delivery-updates"

topic=NewTopic(name=topic_name_partitioned, num_partitions=2, replication_factor=1)

admin.create_topics([topic])