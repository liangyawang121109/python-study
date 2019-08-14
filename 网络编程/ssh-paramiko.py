import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname='192.168.236.132',port=22,username='root',password='121109')

stdin,stdout,stderr = ssh.exec_command('df')

result = stdout.read()
print(result.decode())
ssh.close()
