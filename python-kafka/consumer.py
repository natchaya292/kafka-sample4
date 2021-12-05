from kafka import KafkaConsumer
consumer = KafkaConsumer(bootstrap_servers='54.173.101.222:9093')
consumer.subscribe(['btc'])
for msg in consumer:
    #assert isinstance(msg.value, dict)
    print(msg.value)