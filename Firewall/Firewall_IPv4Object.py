class FirewallIPv4Object:
    id = -1
    name = ''
    uuid = ''
    type = ''
    interface = ''
    subnet = ''
    start_ip = ''
    end_ip = ''

    def __init__(self, object_id):
        self.id = object_id

    def set(self, parameter, value) -> bool:
        if parameter == 'name':
            self.name = value
        elif parameter == 'uuid':
            self.uuid = value
        elif parameter == 'type':
            self.type = value
        elif parameter == 'interface':
            self.interface = value
        elif parameter == 'subnet':
            self.subnet = value
        elif parameter == 'start_ip':
            self.start_ip = value
        elif parameter == 'end_ip':
            self.end_ip = value
        elif parameter == 'id':
            self.id = value
        else:
            return False
        return True
