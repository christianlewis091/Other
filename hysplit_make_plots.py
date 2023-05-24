import pysplit
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# See comments here:
#https://github.com/mscross/pysplit/blob/master/docs/examples/basic_plotting_example.py


trajgroup1 = pysplit.make_trajectorygroup(r'C:/trajectories/colgate/raul_marin_jan/*jan*')
trajgroup2 = pysplit.make_trajectorygroup(r'C:/trajectories/colgate/monte_tarn_jan/*jan*')
trajgroup3 = pysplit.make_trajectorygroup(r'C:/trajectories/colgate/kapuni_jan/*jan*')
trajgroup4 = pysplit.make_trajectorygroup(r'C:/trajectories/colgate/campbell_island_jan/*jan*')
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
    color_dict = {500.0 : 'blue',
                  1000.0 : 'orange',
                  1500.0 : 'black'}

    for traj in tra[i]:
        altitude0 = traj.data.geometry.apply(lambda p: p.z)[0]
        traj.trajcolor = color_dict[altitude0]

    """
    For display purposes, let's plot only every fifth ``Trajectory``.  The lats,
    lons are obtained by unpacking the ``Trajectory.Path``
    (Shapely ``LineString``) xy coordinates.
    """
    for traj in tra[i][::5]:
        bmap.plot(*traj.path.xy, c=traj.trajcolor, latlon=True, zorder=20)

    plt.savefig(f'C:/Users/lewis/venv/python310/python-masterclass-remaster-shared/{names[i]}_trajectory.png')