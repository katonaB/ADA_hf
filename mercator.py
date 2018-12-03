#!/Program Files/Python37/python -d

import webbrowser
print("Content-Type: text/html;charset=ansi\n")


import numpy as np
def degrees2meters(lat,long) :
    x = long * 20037508.34 / 180;
    y = np.log(np.tan((90 + lat) * np.pi / 360)) / (np.pi / 180);
    y = y * 20037508.34 / 180;
    return x, y

def from_lat_long_to_mercator_array(lat, long):
  points = list()
  for value_lat, value_long in zip(lat, long) :
      points.append((degrees2meters(value_lat,value_long)))

  points = np.array(points)
  return points

lat = [1, 2, 3, 4]
long = [10, 20, 30, 40]


print(from_lat_long_to_mercator_array(lat,long) )
