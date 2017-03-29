import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5, 6, 7 ,8 ,9, 10, 11, 12 ,13]
y = [936,1080,641,1056,1009,590,744,489,1030,648,513,780,612]
labels = ['Bill Gates', 'CNN', 'Jimmy Fallon', 'NASA', 'Donald Trump', 'alex', 'Ellen Degeneres', 'Justin Bieber', 'Neil Patrick Harris', 'Kim Kardashian', 'Cristiano Ronaldo', 'Barack Obama', 'Taylor Swift']

plt.plot(x, y, 'ro')
# You can specify a rotation for the tick labels in degrees or with keywords.
plt.xticks(x, labels, rotation='vertical')
# Pad margins so that markers don't get clipped by the axes
plt.margins(0.2)
# Tweak spacing to prevent clipping of tick-labels
plt.subplots_adjust(bottom=0.15)
plt.show()