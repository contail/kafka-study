from confluent_kafka import Producer


p = Producer({'bootstrap.servers': 'localhost:9092'})

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))


def stock_list():
    return ['삼성전자', '삼성카드']

def send_message():
    pass

for data in range(11):
    # Trigger any available delivery report callbacks from previous produce() calls
    p.poll(0)
    data = str(data) + " 1 2 3"
    # Asynchronously produce a message, the delivery report callback
    # will be triggered from poll() above, or flush() below, when the message has
    # been successfully delivered or failed permanently.
    p.produce('mytopic', str(data).encode('utf-8'), callback=delivery_report)
    p.flush()
