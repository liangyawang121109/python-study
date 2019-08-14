import paramiko

transport = paramiko.Transport(('192.168.236.132',22))

transport.connect(username='root',password='121109')
sftp = paramiko.SFTPClient.from_transport(transport)

#sftp.get('/tmp/liangyawang','liangyawang')
sftp.put('liangyawang','/tmp/liangyawang')
transport.close()