import math
import numpy as np
import matplotlib.pyplot as plt


class Value:

    def __init__(self, data, _children=(), _op=''):
        self.data = data
        self._prev = set(_children)
        self._op = _op

    def __repr__(self):
        return f"Value(data={self.data})"

    def __add__(self, other):
        out = Value(self.data + other.data, (self, other), '+')
        return out

    def __mul__(self, other):
        out = Value(self.data * other.data, (self, other), '*')
        return out


a = Value(2.0)
b = Value(-3.0)
c = Value(10.0)
d = a*b + c

# Graph of what is `d` and how it was produced.
print(d)  # Value(data=4.0)
print(d._prev)  # {Value(data=10.0), Value(data=-6.0)}
print(d._op)  # +
