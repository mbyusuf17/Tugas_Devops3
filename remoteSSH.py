import paramiko

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.WarningPolicy())
print("*** Connecting...")
client.connect('', username='', password='')
stdin, stdout, stderr = client.exec_command('ls')
for line in stdout:
print("#result => “ + line.strip(\n")