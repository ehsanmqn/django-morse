import pika, os, time

def on_message_recieved(msg):
  print(" [x] Received message: " + str(msg))

  time.sleep(5) # delays for 5 seconds
  print(" Message processing finished");
  return;

# RabbitMQ configurations
url = os.environ.get('AMQP_URL', 'amqp://admin:admin@127.0.0.1:5672/%2f')
params = pika.URLParameters(url)

# Connect to rabbitmq
connection = pika.BlockingConnection(params)

# Setup the channel
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue='morse')

# Callback function
def callback(ch, method, properties, body):
  on_message_recieved(body)

# Subscribe to the queue
channel.basic_consume('morse',
  callback,
  auto_ack=True)

# start consuming
channel.start_consuming()
connection.close()
