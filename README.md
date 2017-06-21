# Harmonograph simulators using numpy and matplotlib

Copyright 2017 Alan Richmond @ Python3.codes https://opensource.org/licenses/MIT

There are 2 programs here. The first is a simple bare-bones program that gets a couple of parameters from the user and draws a random harmonograph. The second is a full-fledged GUI with buttons and sliders to allow the creation of user-specified harmonographs, or random ones that can be used as a starting point for user adjustments.

* * *

## random-harmonograph.py

This is a simple harmonograph simulator to generate random-ish harmonographs. It asks for the number of pendulums, and exits if the number is 0\. It also asks for the frequency spread, which means roughly, how far from integer may the frequencies go. The nearer to integer they are, the 'cleaner' looking the harmonographs are, but they tend to be perhaps less interesting. The further from integer they are, the more they're likely to look messy.

If you've seen harmonograph programs before (such as my own on this (see 'Related', below) and other sites) you might expect there to be an outer loop for stepping through the 'time' variable. That's not necessary here because numpy handles it for us, making the program simpler and much faster. The outer loop here is gets user input and generates random parameters for each pendulum's oscillation (i.e. sine wave): amplitude, frequency, and phase. The one inner loop computes, for each pendulum, the whole x and y vectors, at once. That is, numpy notices that 't' is a vector and so knows to compute x and y using faster code than Python (C I believe).

Each picture is drawn in its own window, which remains on screen until the program exits, or you dismiss it. This way, you can compare several pictures and select the best if you want to keep some. To save a picture, click on the floppy disc icon on the window's menu bar.

## gui-harmonograph.py

Based on the previous one, but now with GUI radio buttons for selecting one of the pendulums, sliders for setting pendulum sine wave properties, i.e. amplitude, frequency, and phase. The are also sliders for setting the decay rate, and number of steps. You can also specify thin/thick line width, and create a random harmonograph, which you can then modify with the sliders.

Again, you can save pictures using the floppy-disc save icon.
