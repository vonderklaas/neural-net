import math
import numpy as np
import matplotlib.pyplot as plt
from graphviz import Digraph


class Value:

    def __init__(self, data, _children=(), _op='', label=''):
        self.data = data
        # 0 = No effect (changing it does not change the loss function)
        self.grad = 0.0
        self._prev = set(_children)
        self._op = _op
        self.label = label

    def __repr__(self):
        return f"Value(data={self.data})"

    def __add__(self, other):
        out = Value(self.data + other.data, (self, other), '+')
        return out

    def __mul__(self, other):
        out = Value(self.data * other.data, (self, other), '*')
        return out


a = Value(2.0, label='a')
b = Value(-3.0, label='b')
c = Value(10.0, label='c')
e = a*b
e.label = 'e'
d = e + c
d.label = 'd'
f = Value(-2, label='f')
# L gonna be output of our graph
L = d * f
L.label = 'L'

# Graph of what is `d` and how it was produced.
# print(d)
# print(d._prev)
# print(d._op)


def trace(root):
    # Builds a set of all nodes and edges in a graph
    nodes, edges = set(), set()

    def build(v):
        if v not in nodes:
            nodes.add(v)
            for child in v._prev:
                edges.add((child, v))
                build(child)
    build(root)
    return nodes, edges


def draw_dot(root):
    dot = Digraph(format='svg', graph_attr={'rankdir': 'LR'})

    nodes, edges = trace(root)
    for n in nodes:
        uid = str(id(n))
        dot.node(name=uid, label="{ %s | data %.4f | grad %.4f }" %
                 (n.label, n.data, n.grad), shape='record')
        if n._op:
            dot.node(name=uid + n._op, label=n._op)
            dot.edge(uid + n._op, uid)

    for n1, n2 in edges:
        dot.edge(str(id(n1)), str(id(n2)) + n2._op)

    # Render the graph to a file, and opens it
    dot.render('output', view=True)

    return dot


# Backpropagation Algorithm (Setting Up Grads)
a.data += 0.01 * a.grad
b.data += 0.01 * b.grad
c.data += 0.01 * c.grad
f.data += 0.01 * f.grad

e = a*b
d = e + c
L = d * f

a.grad = -2.0 * -3.0
b.grad = -2.0 * 2.0
c.grad = -2.0
d.grad = -2
e.grad = -2.0
f.grad = 4.0
L.grad = 1.0

draw_dot(L)

print('what is next?')


# def lol():
#     h = 0.0001

#     a = Value(2.0, label='a')
#     b = Value(-3.0, label='b')
#     c = Value(10.0, label='c')
#     e = a*b
#     e.label = 'e'
#     d = e + c
#     d.label = 'd'
#     f = Value(-2, label='f')
#     L = d * f
#     L.label = 'L'
#     L1 = L.data

#     a = Value(2.0 + h, label='a')
#     b = Value(-3.0, label='b')
#     c = Value(10.0, label='c')
#     e = a*b
#     e.label = 'e'
#     d = e + c
#     d.label = 'd'
#     f = Value(-2, label='f')
#     L = d * f
#     L.label = 'L'
#     L2 = L.data

#     # How much does 'L' changed?
#     print((L2 - L1) / h)
