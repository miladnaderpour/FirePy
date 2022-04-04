class FirewallPolicy:
    id = -1
    name = ''
    uuid = ''
    srcif = ''
    dstif = ''
    srcaddr = ''
    dstaddr = ''
    service = ''
    action = ''
    schedule = ''
    logtraffic = ''

    def __init__(self, ruleid):
        self.id = ruleid

    def set(self, parameter, value) -> bool:
        if parameter == 'name':
            self.name = value
        elif parameter == 'uuid':
            self.uuid = value
        elif parameter == 'srcintf':
            self.srcif = value
        elif parameter == 'dstintf':
            self.dstif = value
        elif parameter == 'srcaddr':
            self.srcaddr = value
        elif parameter == 'dstaddr':
            self.dstaddr = value
        elif parameter == 'action':
            self.action = value
        elif parameter == 'service':
            self.service = value
        elif parameter == 'schedule':
            self.schedule = value
        elif parameter == 'logtraffic':
            self.logtraffic = value
        elif parameter == 'id':
            self.id = value
        else:
            return False
        return True
