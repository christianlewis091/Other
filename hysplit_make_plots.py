import pysplit
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import matplotlib.gridspec as gridspec
import numpy as np
import subprocess
import pandas as pd
import shapely
import warnings
from shapely.errors import ShapelyDeprecationWarning
warnings.filterwarnings("ignore", category=ShapelyDeprecationWarning)
from os import listdir
from os.path import isfile, join

"""
6/1/23: version 2 of this file that prepares the Hysplit output for plotting: 
Needs updating to do trajectories for everty site. Old version commented out below
"""
# We're still going to loop through each site using the codenames listed in the previous scripts as well
easy_access = pd.read_excel(r'C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/easy_access2.xlsx')
codenames = easy_access['Codename']

# Read in the sheet that was made from the prvious script (hysplit_prepare_output.py)
means_dataframe = pd.read_excel('C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/means_dataframe.xlsx')

# Read in the sheet that was made from the prvious script (hysplit_prepare_output.py)
points = pd.read_excel('C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/points.xlsx')


# Loop through the codenames
for i in range(0, len(codenames)):

    # here are the POINTS that we'll be plotting
    site_points = points.loc[points['location'] == codenames[i]]

    # here are the means that we'll be plotting:
    site_means = means_dataframe.loc[means_dataframe['Codename'] == codenames[i]]

    # define map boundaries
    mapcorners = [0, -70, 360, -20]
    maxlat = mapcorners[3]
    minlat = mapcorners[1]
    maxlon = mapcorners[2]
    minlon = mapcorners[0]

    # Initialize the Figure
    fig = plt.figure(figsize=(4, 4))
    gs = gridspec.GridSpec(6, 4)
    gs.update(wspace=.25, hspace=0.15)

    # Initialize first subplot
    xtr_subsplot = fig.add_subplot(gs[0:4, 0:4])

    # build the map
    map = Basemap(llcrnrlat=minlat, urcrnrlat=maxlat, llcrnrlon=minlon, urcrnrlon=maxlon, resolution='l', lon_0=-180)
    map.drawmapboundary(fill_color='lightgrey')
    map.fillcontinents(color='darkgrey')
    map.drawcoastlines(linewidth=0.1)

    y, x = map(site_points['y'], site_points['x'])
    y_mean, x_mean = (site_means['y'], site_means['x'])
    map.scatter(x, y, marker='x', color='black', alpha=0.01, label=f'{codenames[i]}')
    map.scatter(x_mean, y_mean, marker='o', color='red', alpha=0.01)
    map.drawparallels(np.arange(-90, 90, 10), labels=[True, False, False, False], linewidth=0.5)
    map.drawmeridians(np.arange(-180, 180, 10), labels=[1, 1, 0, 1], linewidth=0.5)

    xtr_subsplot = fig.add_subplot(gs[4:6, 0:4])
    plt.scatter(site_means['timestep'], site_means['z'])
    plt.show()



#
# for i in range(0, len(groups)):
#
#     # Initialize the Figure
#     fig = plt.figure(figsize=(4, 4))
#     gs = gridspec.GridSpec(6, 4)
#     gs.update(wspace=.25, hspace=0.15)
#     standard_pm = None
#
#     # Initialize first subplot
#     xtr_subsplot = fig.add_subplot(gs[0:4, 0:4])
#
#     # have to plot the trajectories themselves:grab them!
#     trajgroup = groups[i]
#
#     # define map boundaries based on country code in EASY ACCES excel sheet
#     mapcorners = [0, -70, 360, -20]
#     maxlat = mapcorners[3]
#     minlat = mapcorners[1]
#     maxlon = mapcorners[2]
#     minlon = mapcorners[0]
#
#     # build the map
#     map = Basemap(llcrnrlat=minlat, urcrnrlat=maxlat, llcrnrlon=minlon, urcrnrlon=maxlon, resolution='l')
#     map.drawmapboundary(fill_color='lightgrey')
#     map.fillcontinents(color='darkgrey')
#     map.drawcoastlines(linewidth=0.1)
#
#     # add the trajectories
#     color_dict = {10: 'blue', 100: 'black', 200: 'green'}
#     for traj in trajgroup:
#         altitude0 = traj.data.geometry.apply(lambda p: p.z)[0]
#         traj.trajcolor = color_dict[altitude0]
#     for traj in trajgroup:
#         map.plot(*traj.path.xy, c=traj.trajcolor, latlon=True, zorder=20, alpha=0.1)
# #
#     # add the MEANS
#     # y, x = map(this_site_traj_means['y'], this_site_traj_means['x'])
#     # map.scatter(x, y, marker='o', edgecolor='black', facecolors='black', alpha=0.5, label=f'{codenames[i]}')
#     # plt.legend()
#     map.drawparallels(np.arange(-90, 90, 10), labels=[True, False, False, False], linewidth=0.5)
#     map.drawmeridians(np.arange(-180, 180, 10), labels=[1, 1, 0, 1], linewidth=0.5)
#
#     xtr_subsplot = fig.add_subplot(gs[4:6, 0:4])
#     plt.show()









# size1 = 10
# # INITIALIZE FIGURE
# fig = plt.figure(figsize=(12,8))
# gs = gridspec.GridSpec(6, 4)
# gs.update(wspace=.25, hspace=0.15)
#
# # INITIALIZE FIRST SUBPLOT (RAUL MARIN)
# xtr_subsplot = fig.add_subplot(gs[0:2, 0:2])
# trajgroup = pysplit.make_trajectorygroup(r'C:/trajectories/colgate/raul_marin/*')
# mapcorners = [-55-80, -70, -55, -30]
# standard_pm = None
# maxlat = mapcorners[3]
# minlat = mapcorners[1]
# nz_max_lon = mapcorners[2]
# nz_min_lon = mapcorners[0]
# map = Basemap(llcrnrlat=minlat, urcrnrlat=maxlat, llcrnrlon=nz_min_lon, urcrnrlon=nz_max_lon, resolution='l')
# map.drawmapboundary(fill_color='lightgrey')
# map.fillcontinents(color='darkgrey')
# map.drawcoastlines(linewidth=0.1)
# color_dict = {10 : 'blue'}
# for traj in trajgroup:
#     altitude0 = traj.data.geometry.apply(lambda p: p.z)[0]
#     traj.trajcolor = color_dict[altitude0]
# for traj in trajgroup:
#     map.plot(*traj.path.xy, c=traj.trajcolor, latlon=True, zorder=20, alpha=0.1)
# y, x = map(rm['y'], rm['x'])
# map.scatter(x, y, marker='o', edgecolor='black', facecolors='black', alpha=0.5, s=size1, label='Raul Marin')
# plt.legend()
# map.drawparallels(np.arange(-90, 90, 10), labels=[True, False, False, False], linewidth=0.5)
# # map.drawmeridians(np.arange(-180, 180, 10), labels=[1, 1, 0, 1], linewidth=0.5)













#
# # We're still going to loop through each site using the codenames listed in the previous scripts as well
# easy_access = pd.read_excel(r'C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/easy_access2.xlsx')
#
# # Read in the sheet that was made from the prvious script (hysplit_prepare_output.py)
# means_dataframe = pd.read_excel('C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/means_dataframe.xlsx')
#













#
# # # there's an issue with Raul Marin trajectories I need to tackle...I'll remove it for now...
# # easy_access = easy_access.loc[easy_access['Codename'] != 'Raul'].reset_index(drop=True)
# # means_dataframe = means_dataframe.loc[means_dataframe['Codename'] != 'Raul'].reset_index(drop=True)
#
# codenames = easy_access['Codename']
# print(codenames)
# code = easy_access['Code']
# #
# # Read in the sheet that was made from the prvious script (hysplit_prepare_output.py)
# means_dataframe = pd.read_excel('C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/means_dataframe.xlsx')
#
# # testing to make sure I have output for every site:
# print(np.unique(means_dataframe['Codename']))
#
# # iterate through the sites based on their codenames:
# for i in range(0, len(codenames)):
#     print(codenames[i])
#     # locate site information based on the codename
#     easy_access_information = easy_access.loc[easy_access['Codename'] == codenames[i]]
#     easy_access_country_code = code[i]
#
#     this_site_traj_means = means_dataframe.loc[means_dataframe['Codename'] == codenames[i]]
#     print(this_site_traj_means)
#
#     # Initialize the Figure
#     fig = plt.figure(figsize=(4, 4))
#     gs = gridspec.GridSpec(6, 4)
#     gs.update(wspace=.25, hspace=0.15)
#     standard_pm = None
#
#     # Initialize first subplot
#     xtr_subsplot = fig.add_subplot(gs[0:4, 0:4])
#
#     # have to plot the trajectories themselves:grab them!
#     trajgroup = pysplit.make_trajectorygroup(f'C:/trajectories/iteration2/{codenames[i]}/*')
#
#     # define map boundaries based on country code in EASY ACCES excel sheet
#     mapcorners = [0, -70, 360, -20]
#     maxlat = mapcorners[3]
#     minlat = mapcorners[1]
#     maxlon = mapcorners[2]
#     minlon = mapcorners[0]
#
#     # build the map
#     map = Basemap(llcrnrlat=minlat, urcrnrlat=maxlat, llcrnrlon=minlon, urcrnrlon=maxlon, resolution='l')
#     map.drawmapboundary(fill_color='lightgrey')
#     map.fillcontinents(color='darkgrey')
#     map.drawcoastlines(linewidth=0.1)
#
#     # add the trajectories
#     color_dict = {10: 'blue', 100: 'black', 200: 'green'}
#     for traj in trajgroup:
#         altitude0 = traj.data.geometry.apply(lambda p: p.z)[0]
#         traj.trajcolor = color_dict[altitude0]
#     for traj in trajgroup:
#         map.plot(*traj.path.xy, c=traj.trajcolor, latlon=True, zorder=20, alpha=0.1)
# #
#     # add the MEANS
#     y, x = map(this_site_traj_means['y'], this_site_traj_means['x'])
#     map.scatter(x, y, marker='o', edgecolor='black', facecolors='black', alpha=0.5, label=f'{codenames[i]}')
#     plt.legend()
#     map.drawparallels(np.arange(-90, 90, 10), labels=[True, False, False, False], linewidth=0.5)
#     map.drawmeridians(np.arange(-180, 180, 10), labels=[1, 1, 0, 1], linewidth=0.5)
#
#     xtr_subsplot = fig.add_subplot(gs[4:6, 0:4])
# # #
# # #

# #
# #
# #
#














"""
Old version
"""

# # READ IN DATA CREATED BY "hysplit_prepare_output.py"
# rm = pd.read_excel('C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/rm.xlsx')
# mt = pd.read_excel('C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/mt.xlsx')
# kp = pd.read_excel('C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/kp.xlsx')
# ci = pd.read_excel('C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/ci.xlsx')
# bj = pd.read_excel('C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/bj.xlsx')
#
# size1 = 10
# # INITIALIZE FIGURE
# fig = plt.figure(figsize=(12,8))
# gs = gridspec.GridSpec(6, 4)
# gs.update(wspace=.25, hspace=0.15)
#
# # INITIALIZE FIRST SUBPLOT (RAUL MARIN)
# xtr_subsplot = fig.add_subplot(gs[0:2, 0:2])
# trajgroup = pysplit.make_trajectorygroup(r'C:/trajectories/colgate/raul_marin/*')
# mapcorners = [-55-80, -70, -55, -30]
# standard_pm = None
# maxlat = mapcorners[3]
# minlat = mapcorners[1]
# nz_max_lon = mapcorners[2]
# nz_min_lon = mapcorners[0]
# map = Basemap(llcrnrlat=minlat, urcrnrlat=maxlat, llcrnrlon=nz_min_lon, urcrnrlon=nz_max_lon, resolution='l')
# map.drawmapboundary(fill_color='lightgrey')
# map.fillcontinents(color='darkgrey')
# map.drawcoastlines(linewidth=0.1)
# color_dict = {10 : 'blue'}
# for traj in trajgroup:
#     altitude0 = traj.data.geometry.apply(lambda p: p.z)[0]
#     traj.trajcolor = color_dict[altitude0]
# for traj in trajgroup:
#     map.plot(*traj.path.xy, c=traj.trajcolor, latlon=True, zorder=20, alpha=0.1)
# y, x = map(rm['y'], rm['x'])
# map.scatter(x, y, marker='o', edgecolor='black', facecolors='black', alpha=0.5, s=size1, label='Raul Marin')
# plt.legend()
# map.drawparallels(np.arange(-90, 90, 10), labels=[True, False, False, False], linewidth=0.5)
# # map.drawmeridians(np.arange(-180, 180, 10), labels=[1, 1, 0, 1], linewidth=0.5)
#
# xtr_subsplot = fig.add_subplot(gs[2:4, 0:2])
# trajgroup = pysplit.make_trajectorygroup(r'C:/trajectories/colgate/monte_tarn/*')
# mapcorners = [-55-80, -70, -55, -30]
# standard_pm = None
# maxlat = mapcorners[3]
# minlat = mapcorners[1]
# nz_max_lon = mapcorners[2]
# nz_min_lon = mapcorners[0]
# map = Basemap(llcrnrlat=minlat, urcrnrlat=maxlat, llcrnrlon=nz_min_lon, urcrnrlon=nz_max_lon, resolution='l')
# map.drawmapboundary(fill_color='lightgrey')
# map.fillcontinents(color='darkgrey')
# map.drawcoastlines(linewidth=0.1)
# color_dict = {10 : 'blue'}
# for traj in trajgroup:
#     altitude0 = traj.data.geometry.apply(lambda p: p.z)[0]
#     traj.trajcolor = color_dict[altitude0]
# for traj in trajgroup:
#     map.plot(*traj.path.xy, c=traj.trajcolor, latlon=True, zorder=20, alpha=0.1)
# y, x = map(mt['y'], mt['x'])
# map.scatter(x, y, marker='o', edgecolor='black', facecolors='black', alpha=0.5, s=size1, label='Monte Tarn')
# plt.legend()
# map.drawparallels(np.arange(-90, 90, 10), labels=[True, False, False, False], linewidth=0.5)
# # map.drawmeridians(np.arange(-180, 180, 10), labels=[1, 1, 0, 1], linewidth=0.5)
#
# xtr_subsplot = fig.add_subplot(gs[4:6, 0:2])
# trajgroup = pysplit.make_trajectorygroup(r'C:/trajectories/colgate/baja_rosales/*')
# mapcorners = [-55-80, -70, -55, -30]
# standard_pm = None
# maxlat = mapcorners[3]
# minlat = mapcorners[1]
# nz_max_lon = mapcorners[2]
# nz_min_lon = mapcorners[0]
# map = Basemap(llcrnrlat=minlat, urcrnrlat=maxlat, llcrnrlon=nz_min_lon, urcrnrlon=nz_max_lon, resolution='l')
# map.drawmapboundary(fill_color='lightgrey')
# map.fillcontinents(color='darkgrey')
# map.drawcoastlines(linewidth=0.1)
# color_dict = {10 : 'blue'}
# for traj in trajgroup:
#     altitude0 = traj.data.geometry.apply(lambda p: p.z)[0]
#     traj.trajcolor = color_dict[altitude0]
# for traj in trajgroup:
#     map.plot(*traj.path.xy, c=traj.trajcolor, latlon=True, zorder=20, alpha=0.1)
# y, x = map(bj['y'], bj['x'])
# map.scatter(x, y, marker='o', edgecolor='black', facecolors='black', alpha=0.5, s=size1, label='Baja Rosales')
# plt.legend()
# map.drawparallels(np.arange(-90, 90, 10), labels=[True, False, False, False], linewidth=0.5)
# # map.drawmeridians(np.arange(-180, 180, 10), labels=[1, 1, 0, 1], linewidth=0.5)
#
#
# xtr_subsplot = fig.add_subplot(gs[0:2, 2:4])
# trajgroup = pysplit.make_trajectorygroup(r'C:/trajectories/colgate/kapuni/*')
# mapcorners = [80, -70, 180, -20]
# standard_pm = None
# maxlat = mapcorners[3]
# minlat = mapcorners[1]
# nz_max_lon = mapcorners[2]
# nz_min_lon = mapcorners[0]
# map = Basemap(llcrnrlat=minlat, urcrnrlat=maxlat, llcrnrlon=nz_min_lon, urcrnrlon=nz_max_lon, resolution='l')
# map.drawmapboundary(fill_color='lightgrey')
# map.fillcontinents(color='darkgrey')
# map.drawcoastlines(linewidth=0.1)
# color_dict = {10 : 'blue'}
# for traj in trajgroup:
#     altitude0 = traj.data.geometry.apply(lambda p: p.z)[0]
#     traj.trajcolor = color_dict[altitude0]
# for traj in trajgroup:
#     map.plot(*traj.path.xy, c=traj.trajcolor, latlon=True, zorder=20, alpha=0.1)
# y, x = map(kp['y'], kp['x'])
# map.scatter(x, y, marker='o', edgecolor='black', facecolors='black', alpha=0.5, s=size1, label='Kapuni')
# plt.legend()
# map.drawparallels(np.arange(-90, 90, 10), labels=[True, False, False, False], linewidth=0.5)
# # map.drawmeridians(np.arange(-180, 180, 10), labels=[1, 1, 0, 1], linewidth=0.5)
#
#
# xtr_subsplot = fig.add_subplot(gs[2:4, 2:4])
# trajgroup = pysplit.make_trajectorygroup(r'C:/trajectories/colgate/campbell_island/*')
# mapcorners =  [80, -70, 180, -20]
# standard_pm = None
# maxlat = mapcorners[3]
# minlat = mapcorners[1]
# nz_max_lon = mapcorners[2]
# nz_min_lon = mapcorners[0]
# map = Basemap(llcrnrlat=minlat, urcrnrlat=maxlat, llcrnrlon=nz_min_lon, urcrnrlon=nz_max_lon, resolution='l')
# map.drawmapboundary(fill_color='lightgrey')
# map.fillcontinents(color='darkgrey')
# map.drawcoastlines(linewidth=0.1)
# color_dict = {10 : 'blue'}
# for traj in trajgroup:
#     altitude0 = traj.data.geometry.apply(lambda p: p.z)[0]
#     traj.trajcolor = color_dict[altitude0]
# for traj in trajgroup:
#     map.plot(*traj.path.xy, c=traj.trajcolor, latlon=True, zorder=20, alpha=0.1)
# y, x = map(ci['y'], ci['x'])
# map.scatter(x, y, marker='o', edgecolor='black', facecolors='black', alpha=0.5, s=size1, label='Campbell Island')
# plt.legend()
# map.drawparallels(np.arange(-90, 90, 10), labels=[True, False, False, False], linewidth=0.5)
# # map.drawmeridians(np.arange(-180, 180, 10), labels=[1, 1, 0, 1], linewidth=0.5)
#
#
# plt.savefig('C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/summary_plot.png',
#             dpi=300, bbox_inches="tight")






































# # See comments here:
# #https://github.com/mscross/pysplit/blob/master/docs/examples/basic_plotting_example.py
#
# trajgroup1 = pysplit.make_trajectorygroup(r'C:/trajectories/colgate/raul_marin/*')
# trajgroup2 = pysplit.make_trajectorygroup(r'C:/trajectories/colgate/monte_tarn/*')
# trajgroup3 = pysplit.make_trajectorygroup(r'C:/trajectories/colgate/kapuni/*')
# trajgroup4 = pysplit.make_trajectorygroup(r'C:/trajectories/colgate/campbell_island/*')
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

"""
Want to plot just the mean trajectories
"""
# # rm = rm.groupby('timestep').mean().reset_index()
# # mt = rm.groupby('timestep').mean().reset_index()
# # kp = rm.groupby('timestep').mean().reset_index()
# # ci = rm.groupby('timestep').mean().reset_index()
# #
# mapcorners1 =  [-55-80, -60, -55, -30]
# mapcorners2 =  [-55-80, -60, -55, -30]
# mapcorners3 =  [100, -60, 180, -30]
# mapcorners4 =  [100, -60, 180, -30]
#
# # BHD MAP
# plt.close()
# fig = plt.figure(figsize=(16, 4))
# gs = gridspec.GridSpec(4, 4)
# gs.update(wspace=.25, hspace=0.1)
#
# xtr_subsplot = fig.add_subplot(gs[0:2, 0:2])
# # MAP PARAMETERS
# maxlat = mapcorners1[3]
# minlat = mapcorners1[1]
# nz_max_lon = mapcorners1[2]
# nz_min_lon = mapcorners1[0]
# map = Basemap(llcrnrlat=minlat, urcrnrlat=maxlat, llcrnrlon=nz_min_lon, urcrnrlon=nz_max_lon, resolution='l')
# map.drawmapboundary(fill_color='lightgrey')
# map.fillcontinents(color='darkgrey')
# map.drawcoastlines(linewidth=0.1)
#
#
#
# # chile_lat = chile['Lat']
# # chile_lon = chile['new_Lon']
# #
# # z, a = map(chile_lon, chile_lat)
# #
# # map.scatter(z, a, marker='D',color='m', s = size1)
# # THE DATA OF THE MEAN TRAJECTORIES
# y, x = map(rm['y'], rm['x'])
# y2, x2 = map(mt['y'], mt['x'])
# map.scatter(x, y, marker='o', edgecolor='black', facecolors='black', alpha=0.5)
# map.scatter(x2, y2, marker='o', edgecolor='black', facecolors='blue', alpha=0.5)
# plt.legend()
# map.drawparallels(np.arange(-90, 90, 10), labels=[True, False, False, False], linewidth=0.5)
# map.drawmeridians(np.arange(-180, 180, 10), labels=[1, 1, 0, 1], linewidth=0.5)
# plt.show()
#
# #
# # xtr_subsplot = fig.add_subplot(gs[0:2, 0:2])