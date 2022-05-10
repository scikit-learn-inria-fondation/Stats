import numpy as np

from matplotlib import pyplot as plt
from cycler import cycler
from matplotlib import colors

def black_fig():
    plt.rcParams['savefig.edgecolor'] = 'k'
    plt.rcParams['savefig.facecolor'] = 'k'
    plt.rcParams['figure.facecolor'] = 'k'
    plt.rcParams['figure.edgecolor'] = 'k'
    plt.rcParams['axes.facecolor'] = 'k'
    plt.rcParams['axes.edgecolor'] = '.7'
    plt.rcParams['axes.labelcolor'] = 'w'
    plt.rcParams['legend.edgecolor'] = 'w'
    plt.rcParams['ytick.color'] = 'w'
    plt.rcParams['xtick.color'] = 'w'
    plt.rcParams['text.color'] = 'w'
    plt.rcParams['boxplot.boxprops.color'] = 'w'

    color_cycle = list(plt.rcParamsDefault['axes.prop_cycle'])
    color_cycle = [.8 * np.array(colors.to_rgb(c['color'])) + .2
                   for c in color_cycle]

    plt.rcParams['axes.prop_cycle'] = cycler(color=color_cycle)
