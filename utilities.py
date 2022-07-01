"""

Partner Group: Raees Ahmad and Dave Thaker

"""

import matplotlib.pyplot as plt
import numpy as np


# Bar Graph of Lebron James Game for Cleveland
labels = ['CLE elo_pre', 'GSW elo_pre', 'CLE elo_post', 'GSW elo_post']
elo_rating = [1592.28, 1729.05, 1576.58, 1744.76]
x = np.arange(len(labels))
width = 0.15

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, elo_rating, width)

# Labels for the Lebron James Final Game in Cleveland Bar Graph
ax.set_ylabel('Elo Rating')
ax.set_xlabel('Team Elo')
ax.set_title('Lebron Final Game for CLE on 06/08/2018')
ax.set_xticks(x)
ax.set_xticklabels(labels)

ax.bar_label(rects1, padding=3)
fig.tight_layout()


plt.show()