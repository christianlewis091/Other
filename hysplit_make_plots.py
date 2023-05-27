import pysplit
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import subprocess
import pandas as pd
from os import listdir
from os.path import isfile, join

# LineSegment class is stored in lineseg.py
# from lineseg import LineSegment

# Location of your tdump file
tdump_file = r'C:/trajectories/colgate_testing/raul_marin/'

onlyfiles = [f for f in listdir(tdump_file) if isfile(join(tdump_file, f))]
# Store the points in this object
points = []

# Open the file for reading
print("Reading trajectory information")

for i in range(0, len(onlyfiles)):
    with open(f'C:/trajectories/colgate_testing/raul_marin/{onlyfiles[i]}', "r") as handle:
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

            # Now we can read points from the trajectory
            points.append({
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
points.to_excel('C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/test.xlsx')

"""
USING THE OUTPUT ABOVE, you can do the following: 
AVERAGE THE BACKTRAJECTORY LATS AND LONS AFTER FILTERING AT EACH TIMESTEP. 
FROM THERE YOU CAN GET A MEAN TRAJECTORY. 

I.E. 
groupby.mean(timestep)
then plot...
"""














#
#
#
#
#
#
#
# # See comments here:
# #https://github.com/mscross/pysplit/blob/master/docs/examples/basic_plotting_example.py
#
# # trajgroup1 = pysplit.make_trajectorygroup(r'C:/trajectories/colgate/raul_marin/*jan*')
# # trajgroup2 = pysplit.make_trajectorygroup(r'C:/trajectories/colgate/monte_tarn/*jan*')
# # trajgroup3 = pysplit.make_trajectorygroup(r'C:/trajectories/colgate/kapuni/*jan*')
# # trajgroup4 = pysplit.make_trajectorygroup(r'C:/trajectories/colgate/campbell_island/*jan*')
#
# trajgroup1 = pysplit.make_trajectorygroup(r'C:/trajectories/colgate_testing/raul_marin/*')
# trajgroup2 = pysplit.make_trajectorygroup(r'C:/trajectories/colgate_testing/monte_tarn/*')
# trajgroup3 = pysplit.make_trajectorygroup(r'C:/trajectories/colgate_testing/kapuni/*')
# trajgroup4 = pysplit.make_trajectorygroup(r'C:/trajectories/colgate_testing/campbell_island/*')
# #
# mapcorners1 =  [-55-80, -60, -55, -30]
# mapcorners2 =  [-55-80, -60, -55, -30]
# mapcorners3 =  [100, -60, 180, -30]
# mapcorners4 =  [100, -60, 180, -30]
# standard_pm = None
#
# tra = [trajgroup1, trajgroup2, trajgroup3, trajgroup4]
# maps = [mapcorners1, mapcorners2, mapcorners3, mapcorners4]
# names = ['RaulMarin','MonteTarn','Kapuni','CampbellIsland']
#
#
# for i in range(0, 4):
#     bmap_params = pysplit.MapDesign(maps[i], standard_pm)
#
#     """
#     Once the ``MapDesign`` is initialized it can be used to draw a map:
#     """
#     bmap = bmap_params.make_basemap()
#
#     """
#     Plotting ``Trajectory`` Paths
#     -----------------------------
#     For this example, we will color-code by initialization (t=0) altitude,
#     (500, 1000, or 1500 m), which can be accessed via ``Trajectory.data.geometry``,
#      a ``GeoSeries`` of Shapely ``Point`` objects.
#     We can store the trajectory color in ``Trajectory.trajcolor`` for convenience.
#     """
#     color_dict = {10 : 'blue'}
#
#     for traj in tra[i]:
#         altitude0 = traj.data.geometry.apply(lambda p: p.z)[0]
#         traj.trajcolor = color_dict[altitude0]
#
#     """
#     For display purposes, let's plot only every fifth ``Trajectory``.  The lats,
#     lons are obtained by unpacking the ``Trajectory.Path``
#     (Shapely ``LineString``) xy coordinates.
#     """
#     # for traj in tra[i][::5]:
#     for traj in tra[i]:
#         bmap.plot(*traj.path.xy, c=traj.trajcolor, latlon=True, zorder=20, alpha=0.1)
#
#     plt.savefig(f'C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/{names[i]}_trajectory.png')