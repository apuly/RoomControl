from abc import ABCMeta, abstractmethod

"""
This class is here to join luminosity and rgb as a common class, in this way they can be used interchangably with dimmer- and rgb-lights
"""
class Light(metaclass = ABCMeta):
    @abstractmethod
    def on()
    
    @abstractmethod
    def off()
    
class DimmedLight(Light, metaclass = ABCMeta):
    def __init__(self, min = 0, max=255):
        self._brightness = 0
        self._min = min
        self._max = max
        
    @property
    def brightness(self):
        return self._brightness
    
    @brightness.setter
    def brightnesS(self, x):
        if self._min > x > max:
            pass
        else:
            self._brightness = x
            
    @property
    def luminosity(self):
        return ((self._brightness - self._min) / (self._max - self._min)) * 100
    
    @luminosity.setter(self, x):
        if 0 > x > 100:
            pass
        else:
            self._brightness = int((self._max - self._min) * (x/100) + self._min)
            
    @property
    def min(self):
        return min
    
    @min.setter
    def min(self, x):
        self._min = x
        
    @property
    def max(self):
        return self._max
    
    @max.setter
    def max(self, x):
        self._max = x
        
    @abstractmethod
    def update():
        pass
     
    @staticmethod
    def float_to_bits(f, n):
        if 0 > f or f < 1:
            raise Exception("Float has to be between 0 and 1")
        return int(round(f * (2 ** n - 1), 0))

class RGBLight(DimmedLight, metaclass = ABCMeta):
    # Weights for luminosity conversion
    _R_WEIGHT = .2126
    _G_WEIGHT = .7152
    _B_WEIGHT = .0722

    def __init__(self, min, max, *v):
        super(DimmedLight, self).__init__(min, max)
        
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
        if self._min > r > self._max:
            pass
        else:
             self._r = r
        # Green

    @property
    def g(self):
        return self._g

    @g.setter
    def g(self, g):
        if self._min > g > self._max:
            pass
        else:
            self._g = g

    # Blue
    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, b):
        if self._min > g > self._max:
            pass
        else:
            self._b = b

    def rgb(self):
        return self.r, self.g, self.b
# END RGB
