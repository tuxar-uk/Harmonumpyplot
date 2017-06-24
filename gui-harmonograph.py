"""	Multi-pendulum Harmonograph simulator with GUI, using numpy and matplotlib

	You can specify any number of pendulums npend > 0; this number also sets
	the number of frequencies available. The sine wave parameters are 
	a: amplitude, a random float in the range 0 to 1;
	f: frequency, a random near-integer in the range 1 to npend
	p: phase, a random float in the range 0 to 2pi

	Copyright 2017 Alan Richmond @ Python3.codes
	The MIT License	https://opensource.org/licenses/MIT
"""
from numpy import arange, sin, pi
import random as r
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons, Button

plt.rcParams["figure.figsize"] = 12.8, 9.6	# size of plot in inches
mf = npend = 4			# # of pendulums & maximum frequency
sigma = 0.005			# frequency spread (from integer)
step = 0.01				# step size
steps = 50000				# # of steps
linew = 1				# line width
delta = 0.0005				# frequency fine tuning with arrows
print("Arrow keys for frequency fine tuning: x = left/right, y = up/down")

t = arange(steps)*step			# time vector
d = 1 - 0.5* arange(steps)/steps	# decay vector
ax = [0.0 for i in range(npend)]	# x amplitude
fx = [i+1 for i in range(npend)]	# x frequency
px = [0.0 for i in range(npend)]	# x phase
ay = [0.0 for i in range(npend)]	# y amplitude
fy = [i+1 for i in range(npend)]	# y frequency
py = [pi/2 for i in range(npend)]	# y phase
ax[0] = 1.0
ay[0] = 1.0
x = y = 0
for i in range(npend):			# initial plot
	x += d * ax[i] * sin(t * fx[i] + px[i])
	y += d * ay[i] * sin(t * fy[i] + py[i])

# PLOT area for harmonogram
f1 = plt.figure(1, facecolor = 'white')
f1.canvas.set_window_title('Harmonograph')
ax1 = f1.add_subplot(111)
plt.axis('off')
plt.subplots_adjust(left=0.1, right=0.9, top=0.95, bottom=0.05)
l, = plt.plot(x, y, 'k', lw=linew)

# CONTROLS

plt.rcParams["figure.figsize"] = 16,2
f2 = plt.figure(2)
f2.canvas.set_window_title('Harmonograph Controls')
ax2 = f2.add_subplot(111)
plt.axis('off')
plt.subplots_adjust(left=0.0, right=1.0, top=1.0, bottom=0.0)

def xprint(name, value):	# convenience function to print params.
	print(name+' '.join(['%.4f' % x for x in value]))

# Radio buttons for pendulum selector
pend = plt.axes([0.0, 0.0, 0.1, 0.8])
radio = RadioButtons(pend, ('1', '2', '3', '4'))

p = 0
update = True
def pensel(label):		# Pendulum selector callback
	global p, update
	pendict = {'1': 0, '2': 1, '3': 2, '4': 3}
	p = pendict[label]
	update = False
	Xsa.set_val(ax[p])
	Xsf.set_val(fx[p])
	Xsp.set_val(px[p])
	Ysa.set_val(ay[p])
	Ysf.set_val(fy[p])
	Ysp.set_val(py[p])
	update = True

radio.on_clicked(pensel)

# Width toggle
def Wupdate(val):		# Width toggle callback
	global l, linew
	linew = 3 - linew		# toggles between 1 & 2
	plt.setp(l, lw=linew)
	f1.canvas.draw_idle()

# Button for Width toggle button
width = plt.axes([0.0, 0.8, 0.1, 0.1])
Width = Button(width, ('Thin/Thick'))
Width.on_clicked(Wupdate)

# 'Random' callback
def Rupdate(val):		# Random button
	global l, update, ax, fx, px, ay, fy, py
	update = False
	for i in range(npend):
		ax[i] = r.uniform(0, 1)
		ay[i] = r.uniform(0, 1)
		px[i] = r.uniform(0, 2*pi)
		py[i] = r.uniform(0, 2*pi)
		fx[i] = r.randint(1, mf) + r.gauss(0, sigma)
		fy[i] = r.randint(1, mf) + r.gauss(0, sigma)
		Xsa.set_val(ax[i])
		Xsf.set_val(fx[i])
		Xsp.set_val(px[i])
		Ysa.set_val(ay[i])
		Ysf.set_val(fy[i])
		Ysp.set_val(py[i])
#	kludge: above has set display of sines to last one computed;
#	need to repeat for current pendulum to get correct values...
	Xsa.set_val(ax[p])
	Xsf.set_val(fx[p])
	Xsp.set_val(px[p])
	Ysa.set_val(ay[p])
	Ysf.set_val(fy[p])
	Ysp.set_val(py[p])
	update = True
#	print('Rupdate')
#	xprint('ax = ', ax); xprint('fx = ', fx); xprint('px = ', px)
#	xprint('ay = ', ay); xprint('fy = ', fy); xprint('py = ', py)
	x = y = 0
	for i in range(npend):
		x += d * (ax[i] * sin(t * fx[i] + px[i]))
		y += d * (ay[i] * sin(t * fy[i] + py[i]))
	l.set_xdata(x)
	l.set_ydata(y)
	ax1.relim()
	ax1.autoscale_view(True,True,True)
	f1.canvas.draw_idle()

# Random button
rand = plt.axes([0.0, 0.9, 0.1, 0.1])
Rand = Button(rand, ('Random'))
Rand.on_clicked(Rupdate)

# Steps controller
def Supdate(val):		# Steps slider callback
	global l, d, steps, t
	steps = Stps.val
	d = 1 - arange(steps)*Dec.val/steps	# decay vector
	t = arange(steps)*step			# time vector
	x = y = 0
	for i in range(npend):
	    x += d * ax[i] * sin(t * fx[i] + px[i])
	    y += d * ay[i] * sin(t * fy[i] + py[i])
	l.set_xdata(x)
	l.set_ydata(y)
	ax1.relim()
	ax1.autoscale_view(True,True,True)
	f1.canvas.draw_idle()

# Slider for line length (steps)
stps = plt.axes([0.2, 0.02, 0.73, 0.1])
Stps = Slider(stps, 'Steps (all)', 0.0, 200000, valinit=steps)
Stps.on_changed(Supdate)

# Decay controller
def Dupdate(val):		# Decay slider callback
	global l, d
	d = 1 - arange(steps)*Dec.val/steps		# decay vector
	x = 0 
	y = 0
	for i in range(npend):
	    x += d * ax[i] * sin(t * fx[i] + px[i])
	    y += d * ay[i] * sin(t * fy[i] + py[i])
	l.set_xdata(x)
	l.set_ydata(y)
	ax1.relim()
	ax1.autoscale_view(True,True,True)
	f1.canvas.draw_idle()

# Slider for decay rate
dec = plt.axes([0.2, 1/8+.02, 0.73, 0.1])
Dec = Slider(dec, 'Decay (all)', 0.0, 1.0, valinit=0.5)
Dec.on_changed(Dupdate)

# X parameters amplitude, frequency, phase
def Xupdate(val):		# X sliders
	global l, ax, fx, px
	if not update: return
	ax[p] = Xsa.val
	fx[p] = Xsf.val
	px[p] = Xsp.val
	x = 0 
	for i in range(npend):
	    x += d * ax[i] * sin(t * fx[i] + px[i])
	l.set_xdata(x)
	ax1.relim()
	ax1.autoscale_view(True,True,True)
	f1.canvas.draw_idle()

def Yupdate(val):		# Y sliders
	global l, ay, fy, py
	if not update: return
	ay[p] = Ysa.val
	fy[p] = Ysf.val
	py[p] = Ysp.val
	y = 0
	for i in range(npend):
	    y += d * ay[i] * sin(t * fy[i] + py[i])
	l.set_ydata(y)
	ax1.relim()
	ax1.autoscale_view(True,True,True)
	f1.canvas.draw_idle()

def getkey(event):
	global fx, fy
	if event.key == 'left':
		fx[p] -= delta
	elif event.key == 'right':
		fx[p] += delta
	elif event.key == 'up':
		fy[p] += delta
	elif event.key == 'down':
		fy[p] -= delta
	else:	return
	xprint('fx = ', fx); xprint('fy = ', fy) 
	update = False
	Xsf.set_val(fx[p])
	Ysf.set_val(fy[p])
	update = True
	x = 0 
	y = 0
	for i in range(npend):
		x += d * ax[i] * sin(t * fx[i] + px[i])
		y += d * ay[i] * sin(t * fy[i] + py[i])
	l.set_xdata(x)
	l.set_ydata(y)
	ax1.relim()
	ax1.autoscale_view(True,True,True)
	f1.canvas.draw_idle()

plt.connect('key_press_event', getkey)

# Sliders for sine wave parameters (amplitude etc), for x & y
axa = plt.axes([0.2, 2/8+.02, 0.73, 0.1])
axf = plt.axes([0.2, 3/8+.02, 0.73, 0.1])
axp = plt.axes([0.2, 4/8+.02, 0.73, 0.1])
Xsa = Slider(axa, 'X Amplitude', 0.0, 1.0, valinit=ax[p])
Xsf = Slider(axf, 'X Frequency', 0.0, mf, valinit=fx[p])
Xsp = Slider(axp, 'X Phase    ', 0.0, 2*pi, valinit=px[p])

aya = plt.axes([0.2, 5/8+.02, 0.73, 0.1])
ayf = plt.axes([0.2, 6/8+.02, 0.73, 0.1])
ayp = plt.axes([0.2, 7/8+.02, 0.73, 0.1])
Ysa = Slider(aya, 'Y Amplitude', 0.0, 1.0, valinit=ay[p])
Ysf = Slider(ayf, 'Y Frequency', 0.0, mf, valinit=fy[p])
Ysp = Slider(ayp, 'Y Phase    ', 0.0, 2*pi, valinit=py[p])

Xsf.on_changed(Xupdate)
Xsa.on_changed(Xupdate)
Xsp.on_changed(Xupdate)

Ysf.on_changed(Yupdate)
Ysa.on_changed(Yupdate)
Ysp.on_changed(Yupdate)

plt.show()
