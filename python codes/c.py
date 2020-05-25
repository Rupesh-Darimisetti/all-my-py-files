from array import array
import math
import reprlib

class Vector:
    typecode='d'

    def __str__(self):
        return str(tuple(self))

    def __repr__(self):
        components = replib.repr(self._component)
        
