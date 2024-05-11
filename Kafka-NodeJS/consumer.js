    const { Kafka } = require("kafkajs");

    kafka = new Kafka({
        clientId: "my-app",
        brokers: ["172.31.55.197:9092"],
    });

    async function init() {
        const consumer = kafka.consumer({ groupId: 'group1' });
        await consumer.connect();

        await consumer.subscribe({ topics: ["rider-updates"], fromBeginning: true });

        await consumer.run({
            eachMessage: async ({ topic, partition, message, heartbeat, pause }) => {
            console.log(
                `${group}: [${topic}]: PART:${partition}:`,
                message.value.toString()
            );
            },
        });
    }

    init();