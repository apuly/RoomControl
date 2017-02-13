from abc import ABCMeta, abstractmethod
from serial import Serial

class ItemController(metaclass=ABCMeta):

    @abstractmethod
    def turn_on():
        pass

    @abstractmethod
    def turn_off():
        pass


class SerialItemController(ItemController):
    def __init__(self, com_port):
        self._serial = Serial(com_port)
        if self._serial.is_open:
            pass
        else:
           self._serial.open()