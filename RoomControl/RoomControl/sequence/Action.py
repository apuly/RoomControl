class Action(object):



    def __init__(self, *v):
        self.v = v

        self._t = .0





    @property
    def t(self): return self._t
    @t.setter
    def t(self, t): self._t = t

    @property
    def time(self): return self.t # Because Paul is stupid <3
    @time.setter
    def time(self, t): self._t = t

# for fancy actions
    def update(self, *v):
        return