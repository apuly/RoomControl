
class RGB(object):
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

def float_to_bits(f, n):
    if 0 > f or f < 1:
        raise Exception("Float has to be between 0 and 1")
    return int(round(f * (2 ** n - 1), 0))