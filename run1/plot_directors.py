import sys
from pyMCDS import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# load cell and microenvironment data
#mcds = pyMCDS('output00000017.xml', 'Archive')
fname = "output%08d.xml" % int(sys.argv[1])
mcds = pyMCDS(fname)

tval = int(mcds.get_time())

cell_df = mcds.get_cell_df()
#xx, yy = mcds.get_2D_mesh()

# get unique cell types and radii
cell_df['radius'] = (cell_df['total_volume'].values * 3 / (4 * np.pi))**(1/3)
types = cell_df['cell_type'].unique()  # array([3., 1., 0.])
dir_type = np.array([3])

# static int worker_ID = 0;
# static int cargo_ID = 1;
# static int linker_ID = 2;    # not used
# static int director_ID = 3;
colors = ['green','blue', 'red']

fig, ax = plt.subplots(figsize=(6, 6))

# Add cells layer
for i, ct in enumerate(dir_type):
    plot_df = cell_df[cell_df['cell_type'] == ct]
    for j in plot_df.index:
        if (j==0):
            print('radius = ',plot_df.loc[j,'radius'])  # 8.412710547954228
        circ = Circle((plot_df.loc[j, 'position_x'], plot_df.loc[j, 'position_y']),
                       color=colors[i], radius=plot_df.loc[j,'radius']*2, alpha=1.0, ec='none')
        ax.add_artist(circ)

ax.axis('equal')
ax.set_xlabel('x [micron]')
ax.set_ylabel('y [micron]')
rbox = 1010
plt.xlim(-rbox,rbox)
plt.ylim(-rbox,rbox)
#fig.colorbar(cs, ax=ax)
title_str = str(tval) + ' mins' 
#ax.set_title(fname + ':  min=' + str(mcds.get_time()) )
#ax.set_title(title_str)
ax.set_title('Director cells (fixed in time)')

plt.show()

#plt.savefig('vector.png')
