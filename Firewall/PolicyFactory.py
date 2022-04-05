from re import Match
from typing import List
from Firewall.FirewallPolicy import FirewallPolicy as Policy
import re


class PolicyFactory:
    policies: List[Policy] = []
    policy: Policy = None
    state: int = 0
    edit_re = re.compile('edit\\s(?P<policy_id>\\d{1,4})')
    set_re = re.compile('set\\s(?P<parameter>\\w+)\\s(?P<value>\\S+)')

    def create_new_policy(self, result: Match) -> bool:
        p = Policy(result.group('policy_id'))
        self.policy = p
        self.state = 1
        return True

    def set_policy_parameter(self, result: Match) -> bool:
        self.policy.set(result.group('parameter'), result.group('value'))
        return True

    def new(self, line: str) -> bool:
        if self.state != 0:
            return False
        result = self.edit_re.search(line)
        if result is not None:
            return self.create_new_policy(result)
        return True

    def set(self, line) -> bool:
        if self.state != 1:
            return False
        result = self.set_re.search(line)
        if result is not None:
            return self.set_policy_parameter(result)
        return False

    def check_config_line(self, line: str) -> bool:
        print(line)
        if self.state == 0:
            return self.new(line)
        elif line == 'next':
            self.policies.append(self.policy)
            self.state = 0
            return True
        elif line == 'end':
            self.state = 0
            return False
        return self.set(line)

    def get_policies(self, lines):
        for line in lines:
            self.check_config_line(str(line).strip())
