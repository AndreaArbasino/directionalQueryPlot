import numpy as np
import math

import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

print("\n" * 25)


def score_lin(point, query):
    score = sum(q * v for q, v in zip(query, point))
    return score


def dist_line_point(point, query):
    distanze = []
    distanze = np.zeros((998, 998))

    for i in range(len(point[1])):
        for o in range(len(point[1])):
            den = query[0] * query[0] + query[1] * query[1]
            num = query[0] * point[0][0, i] + query[1] * point[1][o, 0]
            d = (point[0][0, i] - (query[0] * num / den)) * (point[0][0, i] - (query[0] * num / den)) + \
                (point[1][o, 0] - (query[1] * num / den)) * (point[1][o, 0] - (query[1] * num / den))

            distanze[i, o] = np.sqrt(d)

    return np.array(distanze)


if __name__ == "__main__":
    """def score(q, alpha):
        return q * abs(xx - yy)**alpha + (1 - q) * abs(xx + yy)**alpha"""


    def score(q, alpha):
        b = q
        q1 = 0.5
        q2 = 1 - q1
        point = [xx, yy]
        q = [q1, q2]

        avgavg = xx * (q1 / np.linalg.norm(q)) + yy * (q2 / np.linalg.norm(q))
        # varvar = abs(xx - yy * (q1 / q2)) + abs(yy - xx * (q2 / q1))
        distdist = dist_line_point([xx, yy], q)

        return b * (avgavg ** alpha) + (1 - b) * (distdist ** alpha)


    """def score(q, alpha):
        return q * xx + (1 - q) * yy"""

    init_q = 0.66
    init_alpha = 1

    x = np.linspace(0, 1, num=1000)[1:-1]
    y = np.linspace(0, 1, num=1000)[1:-1]
    xx, yy = np.meshgrid(x, y, sparse=True)

    fig, ax = plt.subplots()

    plt.contourf(x, y, score(init_q, init_alpha))
    plt.subplots_adjust(left=0.05, bottom=0.25)
    plt.axis('scaled')
    plt.colorbar()

    # Make a horizontal slider to control the frequency.
    ax_query = plt.axes([0.25, 0.15, 0.65, 0.03])
    query_slider = Slider(
        ax=ax_query,
        label='Query Coeff',
        valmin=0.00,
        valmax=1.00,
        valinit=init_q,
    )

    # Make a vertically oriented slider to control the amplitude
    ax_alpha = plt.axes([0.25, 0.10, 0.65, 0.03])
    alpha_slider = Slider(
        ax=ax_alpha,
        label="Alpha",
        valmin=0,
        valmax=5,
        valinit=init_alpha
    )


    # The function to be called anytime a slider's value changes
    def update(val):
        ax.contourf(x, y, score(query_slider.val, alpha_slider.val))
        fig.canvas.draw()


    # register the update function with each slider
    query_slider.on_changed(update)
    alpha_slider.on_changed(update)

    # Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
    resetax = plt.axes([0.8, 0.05, 0.1, 0.04])
    button = Button(resetax, 'Reset', hovercolor='0.975')


    def reset(event):
        query_slider.reset()
        alpha_slider.reset()


    button.on_clicked(reset)

    plt.show()
