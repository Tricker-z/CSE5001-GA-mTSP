import matplotlib.pyplot as plt

dots = [
    [37,52], [17,63], [5,64], [16,57], [7,38], [12,42], [20,26], [17,33]
]


plt.figure(figsize = (100, 100))
plt.xlim(0, 100, 1)
plt.ylim(0, 100, 1)

for idx in range(len(dots)):
    plt.plot(dots[idx][0], dots[idx][1], 'o', color='#0085c3')

for i in range(len(dots) - 1):
    start = (dots[i][0], dots[i][1])
    end = (dots[i+1][0], dots[i+1][1])
    plt.plot(start, end, color='#0085c3')

plt.show()