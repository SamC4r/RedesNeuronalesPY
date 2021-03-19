import numpy as np
import matplotlib.pyplot as plt
import keyboard as key
plt.axis([0, 10, 0, 1])
i = 0
while True:
    i+=1
    y = np.random.random()
    plt.scatter(i, y)
    plt.pause(0.05)
    if key.is_pressed('q'):break

plt.show()