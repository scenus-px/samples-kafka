#
# Copyright (C) scenüs, 2023.
# All rights reserved.
# Ehsan Haghpanah; ehsan@scenus.com
#

from confluent_kafka import Producer
import socket

configs = {
     'bootstrap.servers': "172.16.51.121:9092,172.16.51.121:9092,172.16.51.123:9092",
     'client.id': socket.gethostname()
}

producer = Producer(configs)
topic: str = 'python'
producer.produce(topic, key= "Orders", value= "10")
# producer.flush()
