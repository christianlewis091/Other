import pysplit
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import matplotlib.gridspec as gridspec
import numpy as np
import subprocess
import pandas as pd
from os import listdir
from os.path import isfile, join

# LineSegment class is stored in lineseg.py
# from lineseg import LineSegment
names = ['raul_marin','monte_tarn','kapuni','campbell_island']
# Location of your tdump file
points = []

for j in range(0, len(names)):
    tdump_file = f'C:/trajectories/colgate/{names[j]}/'

    onlyfiles = [f for f in listdir(tdump_file) if isfile(join(tdump_file, f))]
    # Store the points in this object


    # Open the file for reading
    print("Reading trajectory information")

    for i in range(0, len(onlyfiles)):
        with open(f'C:/trajectories/colgate/{names[j]}/{onlyfiles[i]}', "r") as handle:
            # split the file into lines
            lines = handle.read().split("\n")
            # Track the number of files
            trajectory_file_count = None
            # Track the number of starting points
            starting_point_count = None
            # Flag to skip the output type line
            skip_output_type = True
            # loop through lines
            for line in lines:
                # Split the line based on spaces and remove empty ones
                data = list(filter(lambda x: not x == "", line.split(" ")))

                # Skip blank lines
                if len(data) == 0:
                    continue

                # The first line we encounter is the trajectory file count
                if trajectory_file_count is None:
                    trajectory_file_count = int(data[0])
                    continue
                # Then we skip lines equal to the trajectory file count
                if trajectory_file_count > 0:
                    trajectory_file_count -= 1
                    continue

                # Repeat for trajectory points
                if starting_point_count is None:
                    starting_point_count = int(data[0])
                    continue

                if starting_point_count > 0:
                    starting_point_count -= 1
                    continue

                # Skip the output flag line if not already done
                if skip_output_type:
                    skip_output_type = False
                    continue
                runtime = 2
                print(names[j])
                # Now we can read points from the trajectory
                points.append({
                    "location": names[j],
                    "start_point": int(data[0]),
                    "grid": int(data[1]),
                    "year": int(data[2]),
                    "month": int(data[3]),
                    "day": int(data[4]),
                    "hour": int(data[5]),
                    "minute": int(data[6]),
                    "forecast": int(data[7]),
                    "timestep": float(data[8]),
                    "y": float(data[9]),
                    "x": float(data[10]),
                    "z": float(data[11]),
                    "p": float(data[12]),
                })
        print("{} points found".format(len(points)))

points = pd.DataFrame(points)
points.to_excel('C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/points.xlsx')
rm = points.loc[points['location'] == 'raul_marin']
mt = points.loc[points['location'] == 'monte_tarn']
kp = points.loc[points['location'] == 'kapuni']
ci = points.loc[points['location'] == 'campbell_island']


rm = rm.groupby('timestep').mean().reset_index()
mt = rm.groupby('timestep').mean().reset_index()
kp = rm.groupby('timestep').mean().reset_index()
ci = rm.groupby('timestep').mean().reset_index()
# rm.to_excel('C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/rm.xlsx')
# mt.to_excel('C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/mt.xlsx')
# kp.to_excel('C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/kp.xlsx')
# ci.to_excel('C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/ci.xlsx')

"""
USING THE OUTPUT ABOVE, you can do the following: 
AVERAGE THE BACKTRAJECTORY LATS AND LONS AFTER FILTERING AT EACH TIMESTEP. 
FROM THERE YOU CAN GET A MEAN TRAJECTORY. 

DO FOR PATAGONIA SITES TOO TO SEE BIOGENIC LAND TRANSPORT OVER THE SOUTHERN MOST
"""

# # See comments here:
# #https://github.com/mscross/pysplit/blob/master/docs/examples/basic_plotting_example.py

trajgroup1 = pysplit.make_trajectorygroup(r'C:/trajectories/colgate/raul_marin/*')
trajgroup2 = pysplit.make_trajectorygroup(r'C:/trajectories/colgate/monte_tarn/*')
trajgroup3 = pysplit.make_trajectorygroup(r'C:/trajectories/colgate/kapuni/*')
trajgroup4 = pysplit.make_trajectorygroup(r'C:/trajectories/colgate/campbell_island/*')
#
mapcorners1 =  [-55-80, -60, -55, -30]
mapcorners2 =  [-55-80, -60, -55, -30]
mapcorners3 =  [100, -60, 180, -30]
mapcorners4 =  [100, -60, 180, -30]
standard_pm = None

tra = [trajgroup1, trajgroup2, trajgroup3, trajgroup4]
maps = [mapcorners1, mapcorners2, mapcorners3, mapcorners4]
names = ['RaulMarin','MonteTarn','Kapuni','CampbellIsland']


for i in range(0, 4):
    bmap_params = pysplit.MapDesign(maps[i], standard_pm)

    """
    Once the ``MapDesign`` is initialized it can be used to draw a map:
    """
    bmap = bmap_params.make_basemap()

    """
    Plotting ``Trajectory`` Paths
    -----------------------------
    For this example, we will color-code by initialization (t=0) altitude,
    (500, 1000, or 1500 m), which can be accessed via ``Trajectory.data.geometry``,
     a ``GeoSeries`` of Shapely ``Point`` objects.
    We can store the trajectory color in ``Trajectory.trajcolor`` for convenience.
    """
    color_dict = {10 : 'blue'}

    for traj in tra[i]:
        altitude0 = traj.data.geometry.apply(lambda p: p.z)[0]
        traj.trajcolor = color_dict[altitude0]

    """
    For display purposes, let's plot only every fifth ``Trajectory``.  The lats,
    lons are obtained by unpacking the ``Trajectory.Path``
    (Shapely ``LineString``) xy coordinates.
    """
    # for traj in tra[i][::5]:
    for traj in tra[i]:
        bmap.plot(*traj.path.xy, c=traj.trajcolor, latlon=True, zorder=20, alpha=0.1)

    plt.savefig(f'C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/{names[i]}_trajectory.png')

"""
Want to plot just the mean trajectories
"""
# rm = rm.groupby('timestep').mean().reset_index()
# mt = rm.groupby('timestep').mean().reset_index()
# kp = rm.groupby('timestep').mean().reset_index()
# ci = rm.groupby('timestep').mean().reset_index()
#
mapcorners1 =  [-55-80, -60, -55, -30]
mapcorners2 =  [-55-80, -60, -55, -30]
mapcorners3 =  [100, -60, 180, -30]
mapcorners4 =  [100, -60, 180, -30]

# BHD MAP
plt.close()
fig = plt.figure(figsize=(16, 4))
gs = gridspec.GridSpec(4, 4)
gs.update(wspace=.25, hspace=0.1)

xtr_subsplot = fig.add_subplot(gs[0:2, 0:2])
maxlat = mapcorners1[3]
minlat = mapcorners1[1]
nz_max_lon = mapcorners1[2]
nz_min_lon = mapcorners1[1]
map = Basemap(llcrnrlat=minlat, urcrnrlat=maxlat, llcrnrlon=nz_min_lon, urcrnrlon=nz_max_lon, resolution='l')
map.drawmapboundary(fill_color='lightgrey')
map.fillcontinents(color='darkgrey')
map.drawcoastlines(linewidth=0.1)


x, y = map(rm['y'], rm['x'])
x2, y2 = map(mt['y'], mt['x'])
map.scatter(x, y, marker='o', edgecolor='black', facecolors='black')
map.scatter(x2, y2, marker='o', edgecolor='black', facecolors='black')
plt.legend()
map.drawparallels(np.arange(-90, 90, 10), labels=[True, False, False, False], linewidth=0.5)
map.drawmeridians(np.arange(-180, 180, 10), labels=[1, 1, 0, 1], linewidth=0.5)
plt.show()


xtr_subsplot = fig.add_subplot(gs[0:2, 0:2])