from ItemController import ItemController
from abc import ABCMeta

class AbstractLamp(object):
    def __init__(self, controller):
        self._controller = controller

    def on():
        pass

    def off():
        pass

    __metaclass__ = ABCMeta

class DimmerLamp(AbstractLamp):
    def __init__(self, controller):
        return super().__init__(controller)

class RGBLamp(AbstractLamp):
    def __init__(self, controller):
        return super().__init__(controller)

class Lamp(AbstractLamp):
    def __init__(self, controller):
        return super().__init__(controller)


#lol