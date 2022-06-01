from re import Match
from typing import List
from Firewall.Firewall_IPv4Object import FirewallIPv4Object as Object
import re
import ipaddress


class IPObjectFactory:
    objects: List[Object] = []
    object: Object = None
    state: int = 0
    edit_re = re.compile('edit\\s"(?P<object_name>.*)"')
    set_re = re.compile('set\\s(?P<parameter>[\w,-]+)\\s(?P<value>\\S+)')

    def create_new_object(self, result: Match) -> bool:
        p = Object(result.group('object_name'))
        self.object = p
        self.state = 1
        return True

    def set_object_parameter(self, result: Match) -> bool:
        self.object.set(result.group('parameter'), result.group('value'))
        return True

    def new(self, line: str) -> bool:
        if self.state != 0:
            return False
        result = self.edit_re.search(line)
        if result is not None:
            return self.create_new_object(result)
        return True

    def set(self, line) -> bool:
        if self.state != 1:
            return False
        result = self.set_re.search(line)
        if result is not None:
            return self.set_object_parameter(result)
        return False

    def check_config_line(self, line: str) -> bool:
        print(line)
        if self.state == 0:
            return self.new(line)
        elif line == 'next':
            self.objects.append(self.object)
            self.state = 0
            return True
        elif line == 'end':
            self.state = 0
            return False
        return self.set(line)

    def get_objects(self, lines):
        for line in lines:
            self.check_config_line(str(line).strip())
