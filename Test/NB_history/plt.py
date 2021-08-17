import matplotlib.pyplot as plt

a = [1, 2, 3]
b = [1, 2, 3]
fig, ax = plt.subplots()
ax.plot(a, b)
ax.set(xlabel='X', ylabel='Y', title='Test plot')
plt.show()