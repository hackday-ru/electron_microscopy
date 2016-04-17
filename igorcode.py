import copy

import matplotlib.pyplot as plt
import numpy as np
#import plotly.plotly as py
#import matplotlib.mlab as mlab
import matplotlib.cm as cm
import matplotlib.colors as clrs
from mpl_toolkits.axes_grid1 import make_axes_locatable


def research(squaresArr, perimetersArr):
    path = 'images/'  # WHERE ALL HISTOGRAMS, PLOTS AND PIES ARE SAVED

# INPUT FOR SQUARE------------------------------------------------------------
    # HIST AND PIE
    #squaresArr = [1, 2,2, 3,3,3, 4,4,4,4, 5,5,5,5,5, 10,10,10,10,10,10,10,10,10,10,10]
    #summBackgroundSquare = 2
    summBackgroundSquare = copy.deepcopy(squaresArr[len(squaresArr)-1])
    squaresArr.remove(squaresArr[len(squaresArr)-1])

    # DON'T TOUCH
    summObjectSquare = 0
    for objectSquare in squaresArr:
        summObjectSquare += objectSquare
#---------------------------------------------------------------------------------


# INPUT FOR PERIMETER--------------------------------------------------------------
    # HIST
    print perimetersArr
    #perimetersArr = [1, 2,2, 3,3,3, 4,4,4,4, 5,5,5,5,5, 10,10,10,10,10,10,10,10,10,10,10]
#--------------------------------------------------------------------------------



# SQUARE PIE
    myValueArr=[summObjectSquare, summBackgroundSquare]
    myLabelsArr=['Objects', 'Backround']
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
    plt.figure(num = 1, figsize = (6,6) )
    plt.title('Relative squares', size = 24)
    explode = (0.08, 0)
    plt.pie(myValueArr, labels = myLabelsArr, colors = colors, shadow = True, explode = explode)
    plt.savefig(path + 'squarepie.png', format = 'png')
    plt.close('all')


# SQUARE COLORED HIST
    fig, ax = plt.subplots()
    ax.set_title('Squares', size = 24)
    plt.xlabel('Square')
    plt.ylabel('Number')
    Ntotal = 1000
# N, bins, patches = ax.hist(np.random.rand(Ntotal), 20)
    N, bins, patches = ax.hist(squaresArr)

    fracs = N.astype(float)/N.max()
    norm = clrs.Normalize(fracs.min(), fracs.max())

    for thisfrac, thispatch in zip(fracs, patches):
        color = cm.jet(norm(thisfrac))
        thispatch.set_facecolor(color)

    plt.savefig(path + 'squarecoloredhist.png', format = 'png')
    plt.close('all')


# PERIMETERS COLORED HIST
    fig, ax = plt.subplots()
    ax.set_title('Perimeters', size = 24)
    plt.xlabel('Perimeter')
    plt.ylabel('Number')
    Ntotal = 1000
# N, bins, patches = ax.hist(np.random.rand(Ntotal), 20)
    perimN, perimBins, perimPatches = ax.hist(perimetersArr)

    fracs = perimN.astype(float)/perimN.max()
    norm = clrs.Normalize(fracs.min(), fracs.max())

    for thisfrac, thispatch in zip(fracs, perimPatches):
        color = cm.jet(norm(thisfrac))
        thispatch.set_facecolor(color)

    plt.savefig(path + 'perimetercoloredhist.png', format = 'png')
    plt.close('all')

'''
# SQUARE VS PERIMETER SCATTER
    x = squaresArr
    y = perimetersArr

    plt.close('all')

    plt.title('Square vs Perimeter', size = 24)
    plt.xlabel('Square')
    plt.ylabel('Perimeter')
    N = 50

#x = np.random.rand(N)
#y = np.random.rand(N)
#colors = np.random.rand(N)


    colors2 = np.random.rand(len(squaresArr))
    area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radiuses


#plt.scatter(x, y, s=area, c=colors2, alpha=0.5)
    plt.scatter(x, y, c=colors2, alpha=0.5)

    plt.savefig(path + 'sqrPerScatter.png', format = 'png')
    plt.close('all')
'''

