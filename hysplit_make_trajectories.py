import pysplit
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

working_dir = r'C:/hysplit/working'
storage_dir = r'C:/trajectories/colgate/raul_marin_jan'
meteo_dir = r'C:/hysplit/met_data'
basename = 'colgate'

# RAUL MARIN BALMACEDA
years = [2006, 2008, 2010]
months = [1]
hours = [12]
altitudes = [500]
location = (-43.79, -72.94)
runtime = -120
#
pysplit.generate_bulktraj(basename, working_dir, storage_dir, meteo_dir,
                          years, months, hours, altitudes, location, runtime,
                          monthslice=slice(0, 32, 2), meteo_bookends=([3,4, 5], [1,2]),
                          get_reverse=True,get_clipped=True, hysplit="C:\hysplit\exec\hyts_std")


working_dir = r'C:/hysplit/working'
storage_dir = r'C:/trajectories/colgate/monte_tarn_jan'
meteo_dir = r'C:/hysplit/met_data'
basename = 'colgate'

# Monte Tarn
years = [2006, 2008, 2010]
months = [1]
hours = [12]
altitudes = [500]
location = (-53.792, -70.97)
runtime = -120
#
pysplit.generate_bulktraj(basename, working_dir, storage_dir, meteo_dir,
                          years, months, hours, altitudes, location, runtime,
                          monthslice=slice(0, 32, 2), meteo_bookends=([3,4, 5], [1,2]),
                          get_reverse=True,get_clipped=True, hysplit="C:\hysplit\exec\hyts_std")

working_dir = r'C:/hysplit/working'
storage_dir = r'C:/trajectories/colgate/kapuni_jan'
meteo_dir = r'C:/hysplit/met_data'
basename = 'colgate'

# Kapuni
years = [2006, 2008, 2010]
months = [1]
hours = [12]
altitudes = [500]
location = (-39.483, 174.1343)
runtime = -120
#
pysplit.generate_bulktraj(basename, working_dir, storage_dir, meteo_dir,
                          years, months, hours, altitudes, location, runtime,
                          monthslice=slice(0, 32, 2), meteo_bookends=([3,4, 5], [1,2]),
                          get_reverse=True,get_clipped=True, hysplit="C:\hysplit\exec\hyts_std")

working_dir = r'C:/hysplit/working'
storage_dir = r'C:/trajectories/colgate/campbell_island_jan'
meteo_dir = r'C:/hysplit/met_data'
basename = 'colgate'

# Kapuni
years = [2006, 2008, 2010]
months = [1]
hours = [12]
altitudes = [500]
location = (-52.54, 169.1538)
runtime = -120
#
pysplit.generate_bulktraj(basename, working_dir, storage_dir, meteo_dir,
                          years, months, hours, altitudes, location, runtime,
                          monthslice=slice(0, 32, 2), meteo_bookends=([3,4, 5], [1,2]),
                          get_reverse=True,get_clipped=True, hysplit="C:\hysplit\exec\hyts_std")

