from abc import abstractmethod

class Action(object):

    def __init__(self, *_v):
        self.v = _v
        pass


    @abstractmethod
    def r(self):
        return self.r

    @abstractmethod
    def g(self):
        return self.g

    @abstractmethod
    def b(self):
        return self.b

    @abstractmethod
    def t(self):
        return self.t