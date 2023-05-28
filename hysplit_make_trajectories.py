import pysplit
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# def generate_bulktraj(basename, hysplit_working, output_dir, meteo_dir, years,
#                       months, hours, altitudes, coordinates, run,
#                       meteoyr_2digits=True, outputyr_2digits=False,
#                       monthslice=slice(0, 32, 1), meteo_bookends=([4, 5], [1]),
#                       get_reverse=False, get_clipped=False,
#                       hysplit="C:\\hysplit4\\exec\\hyts_std"):
# run : int
# Length in hours of simulation.  To calculate back trajectories,
# ``run`` must be negative.

# working_dir = r'C:/hysplit/working'
# storage_dir = r'C:/trajectories/colgate/raul_marin'
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
# location = (-43.79, -72.94)
# runtime = -168 # 1 week
# pysplit.generate_bulktraj(basename, working_dir, storage_dir, meteo_dir,
#                           years, months, hours, altitudes, location, runtime,
#                           monthslice=slice(0, 32, 2), meteo_bookends=([3,4, 5], [1,2]),
#                           get_reverse=True,get_clipped=True, hysplit="C:\hysplit\exec\hyts_std")
#
#
# # # Monte Tarn
# working_dir = r'C:/hysplit/working'
# storage_dir = r'C:/trajectories/colgate/monte_tarn'
# meteo_dir = r'C:/hysplit/met_data'
# basename = 'colgate'
# location = (-53.792, -70.97)
# pysplit.generate_bulktraj(basename, working_dir, storage_dir, meteo_dir,
#                           years, months, hours, altitudes, location, runtime,
#                           monthslice=slice(0, 32, 2), meteo_bookends=([3,4, 5], [1,2]),
#                           get_reverse=True,get_clipped=True, hysplit="C:\hysplit\exec\hyts_std")
# #
# working_dir = r'C:/hysplit/working'
# storage_dir = r'C:/trajectories/colgate/kapuni'
# meteo_dir = r'C:/hysplit/met_data'
# basename = 'colgate'
# location = (-39.483, 174.1343)
# pysplit.generate_bulktraj(basename, working_dir, storage_dir, meteo_dir,
#                           years, months, hours, altitudes, location, runtime,
#                           monthslice=slice(0, 32, 2), meteo_bookends=([3,4, 5], [1,2]),
#                           get_reverse=True,get_clipped=True, hysplit="C:\hysplit\exec\hyts_std")
#
# working_dir = r'C:/hysplit/working'
# storage_dir = r'C:/trajectories/colgate/campbell_island'
# meteo_dir = r'C:/hysplit/met_data'
# basename = 'colgate'
# location = (-52.54, 169.1538)
# pysplit.generate_bulktraj(basename, working_dir, storage_dir, meteo_dir,
#                           years, months, hours, altitudes, location, runtime,
#                           monthslice=slice(0, 32, 2), meteo_bookends=([3,4, 5], [1,2]),
#                           get_reverse=True,get_clipped=True, hysplit="C:\hysplit\exec\hyts_std")

# working_dir = r'C:/hysplit/working'
# storage_dir = r'C:/trajectories/colgate/campbell_island'
# meteo_dir = r'C:/hysplit/met_data'
# basename = 'colgate'
# location = (-52.54, 169.1538)
# pysplit.generate_bulktraj(basename, working_dir, storage_dir, meteo_dir,
#                           years, months, hours, altitudes, location, runtime,
#                           monthslice=slice(0, 32, 2), meteo_bookends=([3,4, 5], [1,2]),
#                           get_reverse=True,get_clipped=True, hysplit="C:\hysplit\exec\hyts_std")


working_dir = r'C:/hysplit/working'
storage_dir = r'C:/trajectories/colgate/baja_rosales'
meteo_dir = r'C:/hysplit/met_data'
basename = 'colgate'
# RAUL MARIN BALMACEDA
# years = [2005, 2007, 2009, 2011, 2015, 2017, 2019, 2021]
# adding extra years begins to throw errors for unknown reasons
years = [2005, 2007, 2009]

months = [1, 2, 12]
hours = [12]
altitudes = [10]
location = (-54.9264, -67.43917)
runtime = -168 # 1 week
pysplit.generate_bulktraj(basename, working_dir, storage_dir, meteo_dir,
                          years, months, hours, altitudes, location, runtime,
                          monthslice=slice(0, 32, 2), meteo_bookends=([3,4, 5], [1,2]),
                          get_reverse=True,get_clipped=True, hysplit="C:\hysplit\exec\hyts_std")
