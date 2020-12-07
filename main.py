from model.audio_db import audio_db
from Kafka import KafkaConsumer
import os


audiodata=audio_db()

consumer = KafkaConsumer(os.environ['AUDIO_UPLOAD_EVENT'],
                         group_id=os.environ['GROUP_ID'],
                         bootstrap_servers=[os.environ['KAFKA_SERVER']],
                         auto_offset_reset='earliest')
for message in consumer:
    audiodata.insert({"id":132123})


