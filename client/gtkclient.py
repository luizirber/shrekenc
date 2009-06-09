#!/usr/bin/env python

import sys, os
import pygtk, gtk, gobject

from subprocess import Popen

MPLAYER_CMD="mplayer -vo x11 -fps 15 -wid %i -slave -idle -noconsolecontrols sdp://n800.sdp"  

class GTK_Main:
	def __init__(self):
		window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		window.set_title("Webcam-Viewer")
		window.set_default_size(500, 400)
		window.connect("destroy", gtk.main_quit, "WM destroy")
		vbox = gtk.VBox()
		window.add(vbox)
		self.movie_window = gtk.DrawingArea()
		vbox.add(self.movie_window)
		hbox = gtk.HBox()
		vbox.pack_start(hbox, False)

		hbox.set_border_width(10)
		hbox.pack_start(gtk.Label())
		self.button = gtk.Button("Start")
		self.button.connect("clicked", self.start_stop)
		hbox.pack_start(self.button, False)
		self.button2 = gtk.Button("Quit")
		self.button2.connect("clicked", self.exit)
		hbox.pack_start(self.button2, False)
		hbox.add(gtk.Label())

		window.show_all()

		command = MPLAYER_CMD  % (self.movie_window.window.xid)
		commandList = command.split()
		Popen(commandList)

	def exit(self, widget, data=None):
		gtk.main_quit()

GTK_Main()
gtk.gdk.threads_init()
gtk.main()
