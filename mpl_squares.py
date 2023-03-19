import matplotlib.pyplot as plt #we do this so that we dont have to type pyplot repeatidly

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.style.use('seaborn') #lots of different styles available 
fig, ax = plt.subplots() #sub plots can generate one or more plots in the same figure. 
#fig represents the entire collection of plots
#ax represents a single plot in the figure

ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()