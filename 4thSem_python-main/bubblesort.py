import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("TKAgg")

def bubble_sort(seq):
    n = len(seq)
    for i in range(n - 1):
        for j in range(n - 1):
            if seq[j] > seq[j + 1]:
                temp = seq[j]
                seq[j] = seq[j + 1]
                seq[j + 1] = temp


seq = [10, 70, 15, 8, 90, 20]
print("Before sorting:", seq)

bubble_sort(seq)
print("After sorting:", seq)
x = list(range(1, 10000))
plt.plot(x, [y * y for y in x])
plt.title("Bubble sort time complexity is O(Ωn²)")
plt.xlabel("Input")
plt.ylabel("Time")
plt.show()
