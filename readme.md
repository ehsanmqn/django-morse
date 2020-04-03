The Morse project for Saman PR

## Table of contents

- [Requirements](#requirements)
- [Getting started](#getting-started)

## Requirements

* [RabbitMQ](https://www.rabbitmq.com/)

## Project overview

The project is a [Django](https://www.djangoproject.com/start/) application. 

## Getting started

#### Clone the repository

```bash
git clone https://github.com/ehsanmqn/MorseProject
```

#### Prepare and run Morse API and RabbitMQ
```bash
cd MorseProject
docker-compose up
```

After running containers, the Morse API can be accessed through port 8000

#### Prepare and run subscriber client
Go to SimpleSubscriber folder and run following commands:

```bash
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
python subscriber.py
```
The last command will run subscriber client. The subscriber client, subscribe in '/morse' channel and wait for incomming 
messages. Everytime a message arrive, the subscriber will print the message into CLI.

#### Prepare and run publisher client
Go to SimplePublisher folder and run following commands:

```bash
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
python publisher.py
```

The last command will run message publisher client. The publisher client uses Morse API to encode a message () then 
publish the encoded message into '/morse' channel.

#### Happy coding!

