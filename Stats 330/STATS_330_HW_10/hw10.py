import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from pylab import *

f = open( 'p1.txt', 'r' )
lines = f.readlines();
f.close()

data = []
for i in range( len( lines ) ):
	data.append( [float(x) for x in lines[i].split()] )

data = [sorted(list(x)) for x in zip( *data )]


means = []
for i, column in enumerate(data):
	means.append( sum(column) / len(column) )
	print( "Mean %d: %f" %( i + 1, means[i] ) )

print( '' )

medians = []
for i, column in enumerate(data):
	medians.append( ( column[len(column)/2] + column[len(column)/2 + 1] ) / 2)
	print( "Median %d: %f" %( i + 1, medians[i] ) )

print( '' )

stdev = []
for i, column in enumerate(data):
	x = 0
	for num in column:
		x += (num-means[i]) **2
	x /= len( column ) -1
	stdev.append( x ** 0.5 )

	print( "Stdev %d: %f" %( i + 1, stdev[i] ) )

print( '' ) 

lq = []
for i, column in enumerate(data):
	low_mid = int( round( ( len( column) + 1) / 4.0 ) - 1)
	lq.append( column[low_mid])

	print( "Lower Quartile %d: %f" %( i + 1, lq[i] ) )

print( ' ' )

uq = []
for i, column in enumerate(data):
	upper_mid = int( round( ( len( column) + 1) * 0.75 ) - 1 )
	uq.append( column[upper_mid] )
	print( "Upper Quartile %d: %f" %( i + 1, uq[i] ) )

plt.rcParams.update({'font.size': 22})

plt.boxplot( data )
plt.savefig( './Figures/Boxplot' )
plt.close()


colors = ['red', 'blue', 'yellow' ]
for i, column in enumerate(data):
	plt.hist( column, 40, color = colors[i] )

plt.savefig( './Figures/Histogram', bbox_inches = 'tight' )
plt.close()

strings = []
with open( 'p2.txt', 'r' ) as f:
	strings = f.readlines()

x, y = [], []
for string in strings:
	split = string.split()
	x.append( int( split[0] ) )
	y.append( float( split[1] ) )

scatter( x, y )
axis( 	[1780, 2020, 0, 350 ] )
xlabel( 'Year' )
ylabel( 'Population in Millions' )
title( 'US Population vs Time')
savefig( './Figures/Timeplot' )





