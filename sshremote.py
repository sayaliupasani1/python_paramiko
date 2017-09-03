import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('127.0.0.1', username='sayaliupasani', password='tvddftt@NOI1')
stdin, stdout, stderr  = client.exec_command('ifconfig')
ifconf = stdout.readlines()
print ifconf
