https://www.youtube.com/watch?v=qbROwuuDOJA&t=1183s

Architecture:
admin.py: creates 1 topic with 2 partitions
producer.py: pushes data into kafka with id, if id is even it goes to parition 0, if id is odd it goes to partition 1. Kafka by default does modulo operation on id and decides the partition
consumer1/2.py: takes data from kafka