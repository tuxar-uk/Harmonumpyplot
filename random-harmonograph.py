"""	Multi-pendulum random Harmonograph simulator using numpy and matplotlib

	You can specify any number of pendulums npend > 0; this number also sets
	the number of frequencies available. The sine wave parameters are 
	a: amplitude, a random float in the range 0 to 1;
	f: frequency, a random near-integer in the range 1 to npend
	p: phase, a random float in the range 0 to 2pi

	Copyright 2017 Alan Richmond @ Python3.codes
	The MIT License	https://opensource.org/licenses/MIT
"""
import random as r
import matplotlib.pyplot as plt
from numpy import arange, sin, cos, exp, pi
plt.rcParams["figure.figsize"] = 8,6	# size of plot in inches

mf = npend = 4			# # of pendulums & maximum frequency
sigma = 0.005			# frequency spread (from integer)
step = 0.01			# step size
steps = 40000			# # of steps
linew = 2			# line width
def xprint(name, value):	# convenience function to print params.
	print(name+' '.join(['%.4f' % x for x in value]))

t = arange(steps)*step		# time axis
d = 1 - arange(steps)/steps	# decay vector
while True:
	n = input("Number of pendulums (%d)(0=exit): "%npend)
	if n != '': npend = int(n)
	if npend == 0: break
	n = input("Deviation from integer freq.(%f): "%sigma)
	if n != '': sigma = float(n)
	ax = [r.uniform(0, 1) for i in range(npend)]
	ay = [r.uniform(0, 1) for i in range(npend)]
	px = [r.uniform(0, 2*pi) for i in range(npend)]
	py = [r.uniform(0, 2*pi) for i in range(npend)]
	fx = [r.randint(1, mf) + r.gauss(0, sigma) for i in range(npend)]
	fy = [r.randint(1, mf) + r.gauss(0, sigma) for i in range(npend)]
	xprint('ax = ', ax); xprint('fx = ', fx); xprint('px = ', px)
	xprint('ay = ', ay); xprint('fy = ', fy); xprint('py = ', py)
	x = y = 0
	for i in range(npend):
		x += d * (ax[i] * sin(t * fx[i] + px[i]))
		y += d * (ay[i] * sin(t * fy[i] + py[i]))
	plt.figure(facecolor = 'white')
	plt.plot(x, y, 'k', linewidth=1.5)
	plt.axis('off')
	plt.subplots_adjust(left=0.0, right=1.0, top=1.0, bottom=0.0)
	plt.show(block=False)
