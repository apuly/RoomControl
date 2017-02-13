from abc import ABCMeta


class Action(object):

    __metaclass__ = ABCMeta

    def __init__(self, *_v):
        self.v = _v
        self._r = 0
        pass


# Red
    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, r):
        self._r = r
# Green
    @property
    def g(self): return self.g
    @g.setter
    def g(self, _g): self.g = _g

# Blue
    @property
    def b(self): return self.b
    @b.setter
    def b(self, _b): self.b = _b


    def rgb(self):
        return self.r, self.g, self.b

# This would be called instead of rgb when sending to a dimmerlamp
    def intensity(self):
        r_wgt = .2126
        g_wgt = .7152
        b_wgt = .0722
        return self.r * r_wgt




    @property
    def t(self): return self.t

    def time(self): return self.t() # Because Paul is stupid <3