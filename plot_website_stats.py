"""
Plot the evolution of website access as obtained from google analytics
"""

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

###############################################################################
stats = pd.read_csv(
    'Analytics scikit-learn.sourceforge.net Audience Overview 20110101-20220430.csv',
    skiprows=[0, 1, 2, 3, 4],
    thousands=',')

# Drop last row which is an aggregate
stats = stats[:-1]

year = np.arange(len(stats['Month Index']))
year = year / 12. + 2011

###############################################################################
# Plot in white bg
plt.figure(figsize=(3.5, 2))

plt.plot(year, stats['Users'], linewidth=2, color='C1')
plt.ylim(0, )
plt.xticks([2010, 2012, 2014, 2016, 2018, 2020, 2022], size=12)
plt.xlim(xmax=year.max())

plt.yticks([2e5, 4e5, 6e5, 8e5, 1e6],
           ["200k", "400k", "600k", "800k", "1M"])
ax = plt.gca()
ax.yaxis.tick_right()
plt.grid(axis='y', color='.5')
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.tight_layout(pad=.1)

plt.savefig('sklearn_website_stats.pdf', facecolor='none',
            edgecolor='none')
plt.savefig('sklearn_website_stats.svg', facecolor='none',
            edgecolor='none')
plt.savefig('sklearn_website_stats.png', facecolor='none',
            edgecolor='none', dpi=200)

###############################################################################
# Plot in white bg
import black_fig
black_fig.black_fig()

plt.figure(figsize=(3.5, 2))

plt.plot(year, stats['Users'], linewidth=2, color='C1')
plt.ylim(0, )
plt.xticks([2010, 2012, 2014, 2016, 2018, 2020, 2022], size=12)
plt.xlim(xmax=year.max())
plt.yticks([2e5, 4e5, 6e5, 8e5, 1e6],
           ["200k", "400k", "600k", "800k", "1M"])
ax = plt.gca()
ax.yaxis.tick_right()
plt.grid(axis='y', color='.2')
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.tight_layout(pad=.1)

plt.savefig('sklearn_website_stats_black.pdf', facecolor='none',
            edgecolor='none')
plt.savefig('sklearn_website_stats_black.svg', facecolor='none',
            edgecolor='none')
plt.savefig('sklearn_website_stats_black.png', facecolor='none',
            edgecolor='none', dpi=200)
