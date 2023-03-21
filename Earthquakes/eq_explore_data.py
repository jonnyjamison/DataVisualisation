import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'Earthquakes/data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f) #'load' converts the data into a format that python can work with - in this case, a dictionary

#readable_file = 'Earthquakes/data/readable_eq_data.json'
#with open(readable_file, 'w') as f:
    #json.dump(all_eq_data, f, indent=4) #'dump' takes a file object and a JSON data object and writes data to the file
    ##'indent = 4' arguement tells dump to format the data using indentation that matches the data's structure
    
all_eq_dicts = all_eq_data['features'] #taking all the data associated with the key 'feaetures'


mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0] #eq_dict[geometry] accesses the dictionary element representing grometry
    #the second key represents pulls the list of values associated with 'coordinates'. 0 is the first element and represents long.
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)
    
    # Map the earthquakes.
data = [{
'type': 'scattergeo',
'lon': lons,
'lat': lats,
'marker': {
'size': [5*mag for mag in mags],
'color': mags,
'colorscale': 'Viridis',
'reversescale': True,
'colorbar': {'title': 'Magnitude'},
},
}] #plotly offers lots of ways to customise - each of which can be expressed as a key-value pair
#list comprehension for 'size' (instead of creating a for loop)
my_layout = Layout(title='Global Earthquakes')
fig = {'data': data, 'layout': my_layout} #dictionary called fig which contains data and layout
offline.plot(fig, filename='global_earthquakes.html')
    
