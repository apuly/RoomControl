class ItemController(object):
    pass

class SerialItemController(ItemController):
    def __init__(self, com_port):
        self._port = com_port

