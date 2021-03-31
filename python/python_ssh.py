#!/usr/bin/python3

import paramiko
import sys

results = []

def ssh_conn():
    client = paramiko.SSHClient()
    client.load_system_host_key()
    client.connect('192.168.0.40',username= 'user1', password= 'Cedrick1987')

    ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command('ss _ltn')

    for line in ssh_stdout:
        results.append(line.strip('\n'))

ssh_conn()

for i in results:
    print(i.strip())

sys.exit()
