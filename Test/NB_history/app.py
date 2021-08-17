import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('./Evolution.csv', delimiter=';', dtype=np.str0, skiprows=1, max_rows=356)

dates = []
values = []

for row in data:
    dates.append(row[0])
    values.append(row[1])

dates = np.array(dates)
values = np.array(values, dtype=np.float32)

fig, ax = plt.subplots()
ax.plot(dates, values)
ax.set(xlabel='Cost', ylabel='Dates')
plt.show()