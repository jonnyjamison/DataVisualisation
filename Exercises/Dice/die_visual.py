from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value) #counts how many time each value appears in the list
    frequencies.append(frequency)
    
# Visualize the results.
x_values = list(range(1, die.num_sides+1)) #plotly doesnt accept output of range directly, need to convert to list 
data = [Bar(x=x_values, y=frequencies)] #represents a dataset that will be represented as a bar chart
#^must be wrapped in square brackets because a data set can have multiple elements 
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 1000 times', xaxis=x_axis_config, yaxis=y_axis_config) #Layout class returns an object that specifies layout as a whole 
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html') #This function needs a dictionary containing the data and layout OBJECTS
#offline plot wil show visualisation in a browser 