import pysplit
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import matplotlib.gridspec as gridspec
import numpy as np
import subprocess
import pandas as pd
from os import listdir
from os.path import isfile, join

"""
6/1/23: version 2 of this file that prepares the Hysplit output for plotting: 
Needs updating to do trajectories for everty site. Old version commented out below
"""

df = pd.read_excel(r'C:/easy_access.xlsx')
codenames = df['Codename']

# Location of your tdump file
points = []

for j in range(0, len(codenames)):
    tdump_file = f'C:/trajectories/iteration2/{codenames[j]}'

    onlyfiles = [f for f in listdir(tdump_file) if isfile(join(tdump_file, f))]
    # Store the points in this object

    # Open the file for reading
    print("Reading trajectory information")

    for i in range(0, len(onlyfiles)):
        with open(f'C:/trajectories/iteration2/{codenames[j]}/{onlyfiles[i]}', "r") as handle:
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
                print(codenames[j])
                # Now we can read points from the trajectory
                points.append({
                    "location": codenames[j],
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
# points.to_excel('C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/points.xlsx')
#

means_dataframe = pd.DataFrame()
for k in range(0, len(codenames)):
    x = points.loc[points['location'] == codenames[k]]


    mean_x = x.groupby('timestep').mean().reset_index()
    print(mean_x)
    means_x = pd.DataFrame(mean_x)
    # add the codename back in for later
    mean_x['Codename'] = codenames[k]
    means_dataframe = pd.concat([means_dataframe, mean_x])

means_dataframe.to_excel('C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/means_dataframe.xlsx')


#
# """
# Version 1 below
# """
#
# names = ['raul_marin','monte_tarn','kapuni','campbell_island', 'baja_rosales']
# # Location of your tdump file
# points = []
#
# for j in range(0, len(names)):
#     tdump_file = f'C:/trajectories/colgate/{names[j]}/'
#
#     onlyfiles = [f for f in listdir(tdump_file) if isfile(join(tdump_file, f))]
#     # Store the points in this object
#
#
#     # Open the file for reading
#     print("Reading trajectory information")
#
#     for i in range(0, len(onlyfiles)):
#         with open(f'C:/trajectories/colgate/{names[j]}/{onlyfiles[i]}', "r") as handle:
#             # split the file into lines
#             lines = handle.read().split("\n")
#             # Track the number of files
#             trajectory_file_count = None
#             # Track the number of starting points
#             starting_point_count = None
#             # Flag to skip the output type line
#             skip_output_type = True
#             # loop through lines
#             for line in lines:
#                 # Split the line based on spaces and remove empty ones
#                 data = list(filter(lambda x: not x == "", line.split(" ")))
#
#                 # Skip blank lines
#                 if len(data) == 0:
#                     continue
#
#                 # The first line we encounter is the trajectory file count
#                 if trajectory_file_count is None:
#                     trajectory_file_count = int(data[0])
#                     continue
#                 # Then we skip lines equal to the trajectory file count
#                 if trajectory_file_count > 0:
#                     trajectory_file_count -= 1
#                     continue
#
#                 # Repeat for trajectory points
#                 if starting_point_count is None:
#                     starting_point_count = int(data[0])
#                     continue
#
#                 if starting_point_count > 0:
#                     starting_point_count -= 1
#                     continue
#
#                 # Skip the output flag line if not already done
#                 if skip_output_type:
#                     skip_output_type = False
#                     continue
#                 runtime = 2
#                 print(names[j])
#                 # Now we can read points from the trajectory
#                 points.append({
#                     "location": names[j],
#                     "start_point": int(data[0]),
#                     "grid": int(data[1]),
#                     "year": int(data[2]),
#                     "month": int(data[3]),
#                     "day": int(data[4]),
#                     "hour": int(data[5]),
#                     "minute": int(data[6]),
#                     "forecast": int(data[7]),
#                     "timestep": float(data[8]),
#                     "y": float(data[9]),
#                     "x": float(data[10]),
#                     "z": float(data[11]),
#                     "p": float(data[12]),
#                 })
#         print("{} points found".format(len(points)))
#
# points = pd.DataFrame(points)
# points.to_excel('C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/points.xlsx')
# rm = points.loc[points['location'] == 'raul_marin']
# mt = points.loc[points['location'] == 'monte_tarn']
# kp = points.loc[points['location'] == 'kapuni']
# ci = points.loc[points['location'] == 'campbell_island']
# bj = points.loc[points['location'] == 'baja_rosales']
#
# rm = rm.groupby('timestep').mean().reset_index()
# mt = mt.groupby('timestep').mean().reset_index()
# kp = kp.groupby('timestep').mean().reset_index()
# ci = ci.groupby('timestep').mean().reset_index()
# bj = bj.groupby('timestep').mean().reset_index()
#
# rm.to_excel('C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/rm.xlsx')
# mt.to_excel('C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/mt.xlsx')
# kp.to_excel('C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/kp.xlsx')
# ci.to_excel('C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/ci.xlsx')
# bj.to_excel('C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/bj.xlsx')
