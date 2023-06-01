"""
5/31/2023: In the second iteration of this script, we're going to make trajectories for ALL our tree-ring sampling sites,
and we're going to do a few atmospheric layers (10, 100, 200m), and we're going to expand the time period. I had a few
issues previously using data from 2005-07, and after that there were errors thrown. Because we're going to do more trajectories,
I'll have to implement a loop.
"""

import pysplit
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pandas as pd

# the following bit of code will create data to read into the for-loops for easier understanding.
# READ IN TREE RING DATA (sent from my work PC to personal PC)
# df = pd.read_excel(r'C:/OPEN_ACCESS_DATA3.xlsx', sheet_name='Final_results')
# df = df[['Site','NewLat','NewLon']].drop_duplicates()
# df.to_excel(r'C:/Users/lewis/test.xlsx')

# after adding "codenames" to each site, which i'll use to write absolute file paths, I reimport it here:
# I'm also going to make a new folder in C for each site "codename"
df = pd.read_excel(r'C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/easy_access2.xlsx')
codenames = df['Codename']
lats = df['NewLat']
lons = df['ChileFixLon']
sitename = df['Site']

# we're going to iterate and make trajectories for all of our sites
for i in range(0, len(codenames)):
    working_dir = r'C:/hysplit/working'
    storage_dir = f'C:/trajectories/iteration2/{codenames[i]}'
    meteo_dir = r'C:/hysplit/met_data'
    basename = 'iteration2'

    years = [2005]
    months = [12]
    hours = [12]
    altitudes = [10, 100, 200]
    location = (lats[i], lons[i])
    print(location)
    runtime = -168  # 1 week
    pysplit.generate_bulktraj(basename, working_dir, storage_dir, meteo_dir,
                              years, months, hours, altitudes, location, runtime,
                              monthslice=slice(0, 32, 2), meteo_bookends=([3,4,5], [1,2]),
                              get_reverse=True,get_clipped=True, hysplit="C:\hysplit\exec\hyts_std")











"""
OLD VERSION BELOW
"""

# # def generate_bulktraj(basename, hysplit_working, output_dir, meteo_dir, years,
# #                       months, hours, altitudes, coordinates, run,
# #                       meteoyr_2digits=True, outputyr_2digits=False,
# #                       monthslice=slice(0, 32, 1), meteo_bookends=([4, 5], [1]),
# #                       get_reverse=False, get_clipped=False,
# #                       hysplit="C:\\hysplit4\\exec\\hyts_std"):
# # run : int
# # Length in hours of simulation.  To calculate back trajectories,
# # ``run`` must be negative.
#
# # working_dir = r'C:/hysplit/working'
# # storage_dir = r'C:/trajectories/colgate/raul_marin'
# # meteo_dir = r'C:/hysplit/met_data'
# # basename = 'colgate'
# # # RAUL MARIN BALMACEDA
# # # years = [2005, 2007, 2009, 2011, 2015, 2017, 2019, 2021]
# # # adding extra years begins to throw errors for unknown reasons
# # years = [2005, 2007, 2009]
# #
# # months = [1, 2, 12]
# # hours = [12]
# # altitudes = [10]
# # location = (-43.79, -72.94)
# # runtime = -168 # 1 week
# # pysplit.generate_bulktraj(basename, working_dir, storage_dir, meteo_dir,
# #                           years, months, hours, altitudes, location, runtime,
# #                           monthslice=slice(0, 32, 2), meteo_bookends=([3,4, 5], [1,2]),
# #                           get_reverse=True,get_clipped=True, hysplit="C:\hysplit\exec\hyts_std")
# #
# #
# # # # Monte Tarn
# # working_dir = r'C:/hysplit/working'
# # storage_dir = r'C:/trajectories/colgate/monte_tarn'
# # meteo_dir = r'C:/hysplit/met_data'
# # basename = 'colgate'
# # location = (-53.792, -70.97)
# # pysplit.generate_bulktraj(basename, working_dir, storage_dir, meteo_dir,
# #                           years, months, hours, altitudes, location, runtime,
# #                           monthslice=slice(0, 32, 2), meteo_bookends=([3,4, 5], [1,2]),
# #                           get_reverse=True,get_clipped=True, hysplit="C:\hysplit\exec\hyts_std")
# # #
# # working_dir = r'C:/hysplit/working'
# # storage_dir = r'C:/trajectories/colgate/kapuni'
# # meteo_dir = r'C:/hysplit/met_data'
# # basename = 'colgate'
# # location = (-39.483, 174.1343)
# # pysplit.generate_bulktraj(basename, working_dir, storage_dir, meteo_dir,
# #                           years, months, hours, altitudes, location, runtime,
# #                           monthslice=slice(0, 32, 2), meteo_bookends=([3,4, 5], [1,2]),
# #                           get_reverse=True,get_clipped=True, hysplit="C:\hysplit\exec\hyts_std")
# #
# # working_dir = r'C:/hysplit/working'
# # storage_dir = r'C:/trajectories/colgate/campbell_island'
# # meteo_dir = r'C:/hysplit/met_data'
# # basename = 'colgate'
# # location = (-52.54, 169.1538)
# # pysplit.generate_bulktraj(basename, working_dir, storage_dir, meteo_dir,
# #                           years, months, hours, altitudes, location, runtime,
# #                           monthslice=slice(0, 32, 2), meteo_bookends=([3,4, 5], [1,2]),
# #                           get_reverse=True,get_clipped=True, hysplit="C:\hysplit\exec\hyts_std")
#
# # working_dir = r'C:/hysplit/working'
# # storage_dir = r'C:/trajectories/colgate/campbell_island'
# # meteo_dir = r'C:/hysplit/met_data'
# # basename = 'colgate'
# # location = (-52.54, 169.1538)
# # pysplit.generate_bulktraj(basename, working_dir, storage_dir, meteo_dir,
# #                           years, months, hours, altitudes, location, runtime,
# #                           monthslice=slice(0, 32, 2), meteo_bookends=([3,4, 5], [1,2]),
# #                           get_reverse=True,get_clipped=True, hysplit="C:\hysplit\exec\hyts_std")
#
#
# working_dir = r'C:/hysplit/working'
# storage_dir = r'C:/trajectories/colgate/baja_rosales'
# meteo_dir = r'C:/hysplit/met_data'
# basename = 'colgate'
# # RAUL MARIN BALMACEDA
# # years = [2005, 2007, 2009, 2011, 2015, 2017, 2019, 2021]
# # adding extra years begins to throw errors for unknown reasons
# years = [2005, 2007, 2009]
#
# months = [1, 2, 12]
# hours = [12]
# altitudes = [10]
# location = (-54.9264, -67.43917)
# runtime = -168 # 1 week
# pysplit.generate_bulktraj(basename, working_dir, storage_dir, meteo_dir,
#                           years, months, hours, altitudes, location, runtime,
#                           monthslice=slice(0, 32, 2), meteo_bookends=([3,4, 5], [1,2]),
#                           get_reverse=True,get_clipped=True, hysplit="C:\hysplit\exec\hyts_std")
