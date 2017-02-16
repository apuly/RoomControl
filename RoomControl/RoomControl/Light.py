from abc import ABCMeta, abstractmethod


"""
This class is here to join luminosity and rgb as a common class, in this way they can be used interchangably with dimmer- and rgb-lights
"""
class Light(metaclass = ABCMeta):
    @staticmethod
    def float_to_bits(f, n):
        if 0 > f or f < 1:
            raise Exception("Float has to be between 0 and 1")
        return int(round(f * (2 ** n - 1), 0))

    @abstractmethod
    def rgb(self):
        pass

    @abstractmethod
    def luminosity(self):
        pass


class RGB(Light):
    # Weights for luminosity conversion
    _R_WEIGHT = .2126
    _G_WEIGHT = .7152
    _B_WEIGHT = .0722

    def __init__(self, *v):
        if len(v) is 3:
            self.r = v[0]
            self.g = v[1]
            self.b = v[2]
        else:
            self.r = .0
            self.g = .0
            self.b = .0

    # Red
    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, r):
        self._r = r
        # Green

    @property
    def g(self):
        return self._g

    @g.setter
    def g(self, g):
        self._g = g

    # Blue
    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, b):
        self._b = b

    def rgb(self):
        return self.r, self.g, self.b

    # This would be called instead of rgb when sending to a dimmerlamp
    def luminosity(self):
        return self.r * self._R_WEIGHT\
             + self.g * self._G_WEIGHT\
             + self.b * self._B_WEIGHT
# END RGB

class Luminosity(Light):

    def __init__(self, l = .0):
        self._l = l


    @property
    def l(self): return self._l
    @l.setter
    def l(self, l): self._l = l

# From parentclass
    def rgb(self):
        return self.l, self.l, self.l

    def luminosity(self):
        return self.l

