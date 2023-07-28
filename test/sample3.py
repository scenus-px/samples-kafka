#
# Copyright (C) scenüs, 2023.
# All rights reserved.
# Ehsan Haghpanah; ehsan@scenus.com
#

from kafka import KafkaConsumer

# consuming latest messages and auto-commit offsets
consumer = KafkaConsumer('Diba.Infra.OmIncoming.OrderError', bootstrap_servers= ['172.16.51.121:9092'])
a = consumer.topics()
print(a)
