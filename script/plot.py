import matplotlib.pyplot as plt

routes = [
[[37, 52], [31, 62], [37, 69], [43, 67], [49, 49], [52, 41], [38, 46], [45, 35], [52, 33], [56, 37], [37, 52]],
[[37, 52], [48, 28], [51, 21], [25, 55], [36, 16], [39, 10], [46, 10], [59, 15], [58, 27], [5, 64], [16, 57], [27, 68], [32, 39], [30, 48], [37, 52], [17, 63], [62, 42], [58, 48], [57, 58], [63, 69], [62, 63], [37, 52]], 
[[37, 52], [52, 64], [42, 57], [42, 41], [40, 30], [30, 40], [21, 47], [37, 52]], 
[[37, 52], [25, 32], [31, 32], [17, 33], [20, 26], [27, 23], [32, 22], [30, 15], [21, 10], [13, 13], [10, 17], [5, 6], [37, 52]], 
[[37, 52], [5, 25], [7, 38], [12, 42], [8, 52], [61, 33], [37, 52]] 
]

colors = ['#0085c3', '#6600cc', '#ff3333', '#ff8000', '#009999']


plt.figure(figsize = (75, 75))
plt.xlim(0, 75, 1)
plt.ylim(0, 75, 1)

for i, dots in enumerate(routes):

    for idx in range(len(dots)):
        plt.plot(dots[idx][0], dots[idx][1], 'o', color=colors[i])

    for idx in range(len(dots) - 1):
        start = (dots[idx][0], dots[idx+1][0])
        end   = (dots[idx][1], dots[idx+1][1])
        plt.plot(start, end, color=colors[i])

plt.show()