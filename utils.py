#! /usr/bin/env python3
import matplotlib.pyplot as plt
import math
import io

adj = math.sin(45*math.pi/180.0)
config = {'r0': (0,0,1), 'r1': (0,1,1), 'r2': (adj,-adj,1), 'r3': (-adj, -adj, 1)}

def plot_svg(c):
    fig, _ = plt.subplots()
    plt.axis('equal')
    ax = plt.gca()
    ax.cla()
    ax.set_xlim(-5,5)
    ax.set_ylim(-5,5)
    for e in [('r0', 'r'), ('r1', 'g'), ('r2', 'b'), ('r3', 'black')]:
        (x,y,z) = c[e[0]]
        ax.add_patch(plt.Circle((x,y), z, color=e[1], fill=False))
    f = io.BytesIO()
    plt.savefig(f, format='svg')
    return f.getvalue()

def test():
    return plot_svg(config)

if __name__ == '__main__':
    print(test())
