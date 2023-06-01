import pysplit
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import matplotlib.gridspec as gridspec
import numpy as np
import subprocess
import seaborn as sns

import pandas as pd
import shapely
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import warnings
from shapely.errors import ShapelyDeprecationWarning
warnings.filterwarnings("ignore", category=ShapelyDeprecationWarning)

#Generate some nice colors
seshadri = ['#c3121e', '#0348a1', '#ffb01c', '#027608', '#0193b0', '#9c5300', '#949c01', '#7104b5']
#            0sangre,   1neptune,  2pumpkin,  3clover,   4denim,    5cocoa,    6cumin,    7berry
#Or try a color from seaborn
colors=sns.color_palette("rocket",6)

"""
6/1/23: version 2 of this file that prepares the Hysplit output for plotting: 
Needs updating to do trajectories for everty site. Old version commented out below
"""
# We're still going to loop through each site using the codenames listed in the previous scripts as well
easy_access = pd.read_excel(r'C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/easy_access2.xlsx')
codenames = easy_access['Codename']
code = easy_access['Code']
lat = easy_access['NewLat']
lon = easy_access['ChileFixLon']

# Read in the sheet that was made from the prvious script (hysplit_prepare_output.py)
means_dataframe = pd.read_excel('C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/means_dataframe.xlsx')

# Read in the sheet that was made from the prvious script (hysplit_prepare_output.py)
points = pd.read_excel('C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/points.xlsx')

# Loop through the codenames
for i in range(0, len(codenames)):
    # which region are we looking at?
    country_code = code[i]
    lat_i = lat[i]
    lon_i = lon[i]

    # here are the POINTS that we'll be plotting
    site_points = points.loc[points['location'] == codenames[i]]

    # isolate the different starting altitudes
    heights = np.unique(site_points['starting_height'])
    h1 = site_points.loc[site_points['starting_height'] == heights[0]]
    h2 = site_points.loc[site_points['starting_height'] == heights[1]]
    h3 = site_points.loc[site_points['starting_height'] == heights[2]]

    # here are the means that we'll be plotting:
    site_means = means_dataframe.loc[means_dataframe['Codename'] == codenames[i]]

    # Initialize the Figure
    fig = plt.figure(figsize=(6, 8))
    gs = gridspec.GridSpec(6, 4)
    gs.update(wspace=.25, hspace=0.03)

    # Initialize first subplot
    xtr_subsplot = fig.add_subplot(gs[0:4, 0:2])

    mapcorners = [lon_i-60, -70, lon_i+20, -20]
    maxlat = mapcorners[3]
    minlat = mapcorners[1]
    maxlon = mapcorners[2]
    minlon = mapcorners[0]

    # build the map
    map = Basemap(llcrnrlat=minlat, urcrnrlat=maxlat, llcrnrlon=minlon, urcrnrlon=maxlon, resolution='l', lon_0=-180)
    map.drawmapboundary(fill_color='lightgrey')
    map.fillcontinents(color='darkgrey')
    map.drawcoastlines(linewidth=0.1)


    # add the trajectories
    y, x = (h1['y'], h1['x'])
    map.scatter(x, y, marker='.', color='black', alpha=1, s=1)
    y, x = (h2['y'], h2['x'])
    map.scatter(x, y, marker='.', color='red', alpha=1, s=1)
    y, x = (h3['y'], h3['x'])
    map.scatter(x, y, marker='.', color='blue', alpha=1, s=1)

    # add the means
    y_mean, x_mean = (site_means['y'], site_means['x'])
    map.scatter(x_mean, y_mean, marker='.', color='brown', alpha=1)

    map.drawparallels(np.arange(-90, 90, 20), labels=[True, False, False, False], linewidth=0.5)
    map.drawmeridians(np.arange(-180, 180, 20), labels=[1, 1, 0, 1], linewidth=0.5)

    # Initialize second subplot (ZOOM IN)
    xtr_subsplot = fig.add_subplot(gs[0:4, 2:4])

    mapcorners = [lon_i-2, lat_i-2, lon_i+2, lat_i+2]
    maxlat = mapcorners[3]
    minlat = mapcorners[1]
    maxlon = mapcorners[2]
    minlon = mapcorners[0]

    # build the map
    map = Basemap(llcrnrlat=minlat, urcrnrlat=maxlat, llcrnrlon=minlon, urcrnrlon=maxlon, resolution='l', lon_0=-180)
    map.drawmapboundary(fill_color='lightgrey')
    map.fillcontinents(color='darkgrey')
    map.drawcoastlines(linewidth=0.1)


    # add the trajectories
    y, x = (h1['y'], h1['x'])
    map.scatter(x, y, marker='.', color=colors[2], alpha=1, s=1, label=str(heights[0]))
    y, x = (h2['y'], h2['x'])
    map.scatter(x, y, marker='.', color=colors[3], alpha=1, s=1, label=str(heights[1]))
    y, x = (h3['y'], h3['x'])
    map.scatter(x, y, marker='.', color=colors[4], alpha=1, s=1, label=str(heights[2]))

    # add the means
    y_mean, x_mean = (site_means['y'], site_means['x'])
    map.scatter(x_mean, y_mean, marker='.', color='brown', alpha=1)

    map.drawparallels(np.arange(-90, 90, 20), labels=[True, False, False, False], linewidth=0.5)
    map.drawmeridians(np.arange(-180, 180, 20), labels=[1, 1, 0, 1], linewidth=0.5)


    # Third subplot = altitudes
    xtr_subsplot = fig.add_subplot(gs[4:6, 0:4])
    plt.scatter(h1['timestep'], h1['z'], color)
    plt.scatter(h2['timestep'], h2['z'])
    plt.scatter(h3['timestep'], h3['z'])

    plt.savefig(f'C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/plots/{codenames[i]}.png',
                dpi=300, bbox_inches="tight")

