
from RGB import *

class Action(object):
    def __init__(self, *, rgb = RGB(0, 0, 0)):
        self._rgb = rgb
        self._t = .0


    @property
    def t(self):
        return self._t
    @t.setter
    def t(self, t):
        self._t = t

    @property
    def time(self):
        return self.t
    @time.setter
    def time(self, t):
        self.t = t

    @property
    def rgb(self):
        return self._rgb
    @rgb.setter
    def rgb(self, rgb):
        self._rgb = rgb

# for fancy actions
    def update(self, *v):
        return