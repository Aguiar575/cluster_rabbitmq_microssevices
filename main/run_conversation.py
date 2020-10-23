#!/usr/bin/env python
import threading
import os
import pika
import uuid
import time
import datetime

#essa função irá rodar os dois scripts ao mesmo tempo 
def run_conversation(nome_arquivo):
    os.system('py -3.8 {}'.format(nome_arquivo))

#início
if __name__ == "__main__":

    arquivos = ['reciver_RPC.py','sender_RPC.py']

    processos = []
    for arquivo in arquivos:
        processos.append(threading.Thread(target=run_conversation, args=(arquivo,)))

    for processo in processos:
        processo.start()