import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("TKAgg")


def selection_sort(seq):
    n = len(seq)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if seq[j] < seq[min_index]:
                min_index = j
        temp = seq[min_index]
        seq[min_index] = seq[i]
        seq[i] = temp


seq = [56, 53, 32, 66, 21, 78, 965, 64, 2, 54, 2]
print("Before sorting:", seq)

selection_sort(seq)
print("After sorting:", seq)

x = list(range(1, 10000))
plt.plot(x, [y * y for y in x])
plt.title("Selection sort time complexity is O(n)")
plt.xlabel("Input")
plt.ylabel("Time")
plt.show()
