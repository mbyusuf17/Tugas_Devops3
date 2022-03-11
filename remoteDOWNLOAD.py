import paramiko

transport = paramiko.Transport(("", 22))
transport.connect(None,'','')
sftp = paramiko.SFTPClient.from_transport(transport)
# Download
filepath = "/etc/passwd"
localpath = "/tmp/remotepasswd"
sftp.get(filepath,localpath)
sftp.close()
transport.close()