import pandas as pd
import networkx as nx


filename = 'orders_autumn_2020.csv'

order_data = pd.read_csv(filename)

#
## Draw a map
#

# Define map area
left_lower_corner = [60.191396, 20.077349]
right_lower_corner = [59.589672, 30.909586]
right_upper_corner = [70.374975, 33.670111]
left_upper_corner = [70.453271, 19.203909]

f