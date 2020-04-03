import pika, os, logging
import requests

logging.basicConfig()

# RabbitMQ configurations
url = os.environ.get('AMQP_URL', 'amqp://admin:admin@127.0.0.1/%2f')
params = pika.URLParameters(url)
params.socket_timeout = 5

# Connect to rabbitmq
connection = pika.BlockingConnection(params)

# start a channel
channel = connection.channel()

# Declare a queue
channel.queue_declare(queue='morse')

# Encode message using Morse API
url = "http://127.0.0.1:8000/api/morse/"
payload = {'input': 'This is a test for Morse API'}
files = [
]
headers= {}

response = requests.request("POST", url, headers=headers, data = payload, files = files)
print(response.text.encode('utf8'))

# send message to rabbitmq
channel.basic_publish(exchange='', routing_key='morse', body=response.text.encode('utf8'))

print ("[x] Message sent to consumer")

connection.close()
