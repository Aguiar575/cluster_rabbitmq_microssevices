#!/usr/bin/env python
import pika
import datetime

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='rpc_queue')


def on_request(ch, method, props, body):
    n = str(body)
    i = str(props.correlation_id)
    p = str(props.cluster_id)
    t = datetime.datetime.fromtimestamp(props.timestamp).strftime('%Y-%m-%d %H:%M:%S')

    print('---------------------------')
    print("[Sucesso! - %s]" % t)
    print("Mensagem recebida: %s" % n)
    print("MicroServiceId: %s" % i)
    print("instância %s" % p)  
    print('---------------------------')

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body="[From Reciver] Mensagem recebida com sucesso!")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

print("Aguardando Mensagens...")
print('\n')
channel.start_consuming()