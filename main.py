import pandas as pd
import networkx as nx
import numpy as np
from datetime import datetime
from datetime import timedelta

from matplotlib import pyplot as plt


from mpl_toolkits.basemap import Basemap


filename = 'orders_autumn_2020.csv'

order_data = pd.read_csv(filename)

## Constants

helsinki_coords = [60.169825, 24.938500]


#
## Draw a map
#
# Define map area


## Parameters
# Define parameters 

lower_left = [60.113705, 24.773302]
upper_right = [60.281659, 25.163669]

fig = plt.figure(figsize=(8,8))

m = Basemap(projection='merc',
            llcrnrlat=lower_left[0],
            urcrnrlat=upper_right[0],
            llcrnrlon=lower_left[1],
            urcrnrlon=upper_right[1],
            resolution='c')

m.drawcoastlines()
m.shadedrelief()
m.fillcontinents(color='tan',lake_color='lightblue', zorder=0.5)
m.drawcountries(color='gray')
m.drawmapboundary(fill_color='lightblue')


filtered_data = filter_data(data=order_data,
                            lat_data=order_data['VENUE_LAT'], 
                            lon_data=order_data['VENUE_LONG'], 
                            lower_left_crnr=lower_left, 
                            upper_right_crnr=upper_right)


# Filter data based on timestamp
dummy_stamp = "2020-09-30 19:27:00.000"


# Create bin data to clusters
step = 0.001
to_bin = lambda x: np.floor(x / step) * step
order_data["latbin"] = order_data['VENUE_LAT'].map(to_bin)
order_data["lonbin"] = order_data['VENUE_LONG'].map(to_bin)

m.scatter(lon_binned.values, lat_binned.values, latlon=True)

plt.show()

# Create colorbar & legend


#####
## Helper functions
#####
def string_to_date(date_string):
    return datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S.%f')

def date_to_string(date):
    return str(date)

####
## Actual functions
####
def cluster_data(radius, lat, lon):
    """
    

    Parameters
    ----------
    radius : TYPE
        DESCRIPTION.
    lat : TYPE
        DESCRIPTION.
    lon : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """



def filter_data(data, hours, current_time):
    """
    Return datapoints which fall within certain limits given the current time and the limit resolution.

    Parameters
    ----------
    data : pandas.DataFrame
        Input data to be filtered.
    current_time : DateTime
        format yyyy-MM-dd HH:mm:ss.SSS
    hours: float
        resolution in hours.

    Returns
    -------
    filtered_data : pandas.DataFrame
        Data that is filtered based on resolution around current timestamp.

    """
    time_difference = order_data['TIMESTAMP'].map(string_to_date) - current_time
    upper_limit = timedelta(hours=hours)
    lower_limit = timedelta(hours=-1*hours)
    
    
    filtered_data = data[(lower_limit < time_difference) & (time_difference < upper_limit)]

    return filtered_data
        


    



m, ax = draw_map("Helsinki", lower_left, upper_right)    
plot_point(helsinki_coords[0], helsinki_coords[1])

