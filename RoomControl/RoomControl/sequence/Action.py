from abc import ABCMeta


class Action(object):

    __metaclass__ = ABCMeta

    _R_WEIGHT = .2126
    _G_WEIGHT = .7152
    _B_WEIGHT = .0722

    def __init__(self, *v):
        self.v = v
        self._r = .0
        self._g = .0
        self._b = .0
        self._t = .0


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
    def g(self, g): self._g = g

# Blue
    @property
    def b(self): return self._b
    @b.setter
    def b(self, b): self._b = b


    def rgb(self):
        return self.r, self.g, self.b

# This would be called instead of rgb when sending to a dimmerlamp
    def luminosity(self):
        return self.r * self._R_WEIGHT\
             + self.g * self._G_WEIGHT\
             + self.b * self._B_WEIGHT


    @property
    def t(self): return self._t
    @t.setter
    def t(self, t): self._t = t

    @property
    def time(self): return self.t # Because Paul is stupid <3
    @time.setter
    def time(self, t): self._t = t