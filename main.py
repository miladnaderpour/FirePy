from paramiko import SSHClient
from paramiko.client import AutoAddPolicy
import re

client = SSHClient()
client.set_missing_host_key_policy(AutoAddPolicy())
client.connect('10.1.3.89', username='Monitor', password='F!re$1$hc0O$um')
ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command("show firewall policy 2609")
output = ssh_stdout.readlines()
client.close()

cnfRegex = re.compile("edit\\s(?P<id>\\d{1,4})")
r = cnfRegex.search("    edit 2609")
print(r)
for line in output:
    r = cnfRegex.search(line)
    if r is not None:
        print(line.strip())
        print(r.group('id'))
