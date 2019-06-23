import matplotlib.pyplot as plt

x_values = list(range(1, 6))
y_values = [x**3 for x in x_values]

#define scatter and color map
plt.scatter(x_values, y_values, s=20)

#Set chart label and axes
plt.title("Cubed Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

#Set size of tick labels
plt.tick_params(axis='both', which='major', labelsize=10)

#Set axis range
plt.axis([0,6,0,150])

plt.show()