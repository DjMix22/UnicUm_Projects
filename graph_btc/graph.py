import matplotlib.pyplot as plt
import matplotlib.animation as animation
from get_data import main
import numpy as np

fig, ax = plt.subplots()
times, prices = [], []


def animate(i):
    data = main()
    current_time = data[0]
    current_price = data[1]

    times.append(current_time)
    prices.append(current_price)

    if len(times) > 7:
        times.pop(0)
        prices.pop(0)

    num_points = len(times)
    if num_points > 1:
        ax.clear()
        ax.plot(times, prices, color='g')

    ax.set_xlabel('Time')
    ax.set_ylabel('Price')
    ax.set_title('Bitcoin Price Chart in USD')


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
