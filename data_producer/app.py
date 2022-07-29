import datetime
import hashlib
import json
import logging
import sys
import time

from confluent_kafka import Producer
from faker import Faker

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(asctime)s %(message)s",
    datefmt="%Y-%m-%d %I:%M:%S %p",
    handlers=[logging.FileHandler("example.log"), logging.StreamHandler()],
)

logging.info("STARTING SCRIPT ...")

def generate_fake_msg(faker_obj: Faker):
    name = faker_obj.name()
    scrape_ts = datetime.datetime.now()

    # hash concat with current timestamp for pk bc there might be 2 ppl who have the same exact name
    payload = {
        "id": hashlib.md5((name + str(scrape_ts)).encode("utf-8")).hexdigest(),
        "name": name,
        "scrape_ts": scrape_ts,
    }

    # first dump then loads - have to convert datetime obj to string then load everything back to dict
    # in order to store the timestamps to dynamodb as a string

    logging.info(f"Generating payload for {name} at {scrape_ts}")
    return payload

# this is an acknowledgement function from 
# https://docs.confluent.io/clients-confluent-kafka-python/current/overview.html
# this ensures a notification upon delivery or failure of any message.
def acked(err, msg):
    if err is not None:
        logging.info(f"Failed to deliver message: {msg.value()}: {err.str()}")
    else:
        logging.info(f"Message produced: {msg.value()}")

# this takes the data out of a datetime.date(2022, 04, 06) datetime format and into a human readable date as a string
def json_serializer(obj):
    if isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat()
    raise "Type %s not serializable" % type(obj)

if __name__ == "__main__":
    p = Producer({'bootstrap.servers': 'kafka:29092'})

    fake = Faker()
    starttime = time.time()
    invocations = 0

    try:
        while True:
            if invocations > 100:
                p.flush()
                logging.info(f"Exiting out ...")
                break
            else:
                p.poll(0.0)
                payload = generate_fake_msg(fake)
                invocations += 1
                p.produce(topic='jacobs-topic', key=payload['id'], value=json.dumps(payload, default=json_serializer, ensure_ascii=False).encode('utf-8'), callback=acked)
                time.sleep(
                    5 - ((time.time() - starttime) % 5)
                ) # write a message every 5 seconds

    except Exception as e:
        logging.info(f"Error Occurred, {e}")
        sys.exit(1)
