import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, s=1, c=y_values, cmap=plt.cm.get_cmap('Blues'), edgecolor='none')

#Set chart label and axes
plt.title("Cubed Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

#Set size of tick labels
plt.tick_params(axis='both', which='major', labelsize=10)

#Set axis range
plt.axis([0,1030,0,1100000000])

plt.show()