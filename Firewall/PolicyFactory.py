from FirewallPolicy import FirewallPolicy as fp


class PolicyFactory:
    policy: fp = None
    state: int

    def New(self, ruleid: str) -> bool:
        if self.state != 0:
            return False
        else:
            p = fp(ruleid)
            self.policy = p
            self.state = 1

    def Set(self, parameter, value) -> bool:
        if self.state != 1:
            return False
        else:
            self.policy.set(parameter, value)
