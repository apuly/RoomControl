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
        self._percent = 0

    @property
    def percent(self):
        return self._percent

    @percent.setter
    def percent(self, x):
        if 0 < x < 100:
            self._percent = x

class RGBLamp(AbstractLamp):
    def __init__(self, controller):
        return super().__init__(controller)
        self._r = 0
        self._g = 0
        self._b = 0

    @property
    def r(self):
        return self._r

    @property
    def g(self):
        return self._g

    @property
    def b(self):
        return self._b

    @r.setter
    def r(self, x):
        if 0 < x < 255:
            self._r = x

    @g.setter
    def g(self, x):
        if 0 < x < 255:
            self._g = x

    @b.setter
    def b(self, x):
        if 0 < x < 255:
            self._b = x

class Lamp(AbstractLamp):
    def __init__(self, controller):
        return super().__init__(controller)


#lol