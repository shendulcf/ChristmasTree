import matplotlib.pyplot as plt

plt.title("Christmas Tree")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.plot([0, 0], [0, 1], color="green")
plt.scatter(0, 1, color="red")

plt.plot([0, 0], [0, 1], color="darkgreen", linewidth=10)
plt.plot([-0.5, 0.5], [0, 1], color="darkgreen", linewidth=10)
plt.scatter(-0.3, 0.5, color="darkgreen", s=100)
plt.scatter(0.3, 0.5, color="darkgreen", s=100)
plt.show()