import paramiko

transport = paramiko.Transport(("", 22))
transport.connect(None,'','')
sftp = paramiko.SFTPClient.from_transport(transport)
# Upload
filepath = "/tmp/remotehosts"
localpath = "/etc/hosts"
sftp.put(localpath,filepath)
sftp.close()
transport.close()