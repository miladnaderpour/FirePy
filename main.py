from paramiko import SSHClient
from paramiko.client import AutoAddPolicy
from Firewall.PolicyFactory import PolicyFactory as PolicyFactory

client = SSHClient()
client.set_missing_host_key_policy(AutoAddPolicy())
client.connect('10.1.3.89', username='Monitor', password='F!re$1$hc0O$um')
ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command("show firewall policy")
output = ssh_stdout.readlines()
client.close()

pf = PolicyFactory()
pf.get_policies(output)
for policy in pf.policies:
    print(f'{policy.id} {policy.name} : Src= {policy.srcif} ({policy.srcaddr}) -> Dst={policy.dstif} ({policy.dstaddr}) | {policy.service} | {policy.action}')
# cnfRegex = re.compile("edit\\s(?P<id>\\d{1,4})")
# r = cnfRegex.search("    edit 2609")
# print(r)
# for line in output:
#     r = cnfRegex.search(line)
#     print(line.strip())
#     if r is not None:
#         print(r.group('id'))
