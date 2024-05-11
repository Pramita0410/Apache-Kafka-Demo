const { Kafka } = require("kafkajs");

kafka = new Kafka({
    clientId: "my-app",
    brokers: ["172.31.55.197:9092"],
});

async function init() {
    const producer = kafka.producer();
    console.log("Connecting Producer");
    await producer.connect();
    console.log("Producer Connected Successfully");

    await producer.send({
        topic: 'rider-updates',
        messages: [
            {
              partition: 0,
              key: "location-update",
              value: JSON.stringify({ name: 'tony', loc:'Hyd' }),
            },
          ]
    })

    await producer.disconnect();
}

init();