#!/usr/bin/env python

import sys, os
import pygtk, gtk, gobject
import socket

HOST = '127.0.0.1'
PORT = 50008
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

class GTK_Main:
	def __init__(self):
		window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		window.set_title("Webcam-Viewer")
		window.set_default_size(80, 80)
		window.connect("destroy", gtk.main_quit, "WM destroy")

		hbox = gtk.HBox()
		window.add(hbox)

		hbox.set_border_width(10)
		hbox.pack_start(gtk.Label())
		self.button4 = gtk.Button("Right")
		self.button4.connect("clicked", self.move_right)
		hbox.pack_start(self.button4, False)
		self.button5 = gtk.Button("Forward")
		self.button5.connect("clicked", self.move_forward)
		hbox.pack_start(self.button5, False)
		self.button6 = gtk.Button("Left")
		self.button6.connect("clicked", self.move_left)
		hbox.pack_start(self.button6, False)
		
		hbox.add(gtk.Label())

		window.show_all()

	def exit(self, widget, data=None):
		s.send('Q')
		gtk.main_quit()

	def move_right(self, widget, data=None):
		s.send('R')

	def move_left(self, widget, data=None):
		s.send('L')

	def move_forward(self, widget, data=None):
		s.send('F')

GTK_Main()
gtk.gdk.threads_init()
gtk.main()
