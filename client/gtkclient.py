#!/usr/bin/env python

import sys, os
import pygtk, gtk, gobject
import socket

from subprocess import Popen

HOST = '127.0.0.1'
PORT = 50007
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

FIFO = "/tmp/fifo%d" % time.time()
STDOUT = "/tmp/out%d" % time.time()
STDERR = "/dev/null"
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
		#self.button.connect("clicked", self.start_stop)
		hbox.pack_start(self.button, False)
		self.button2 = gtk.Button("Quit")
		self.button2.connect("clicked", self.exit)
		hbox.pack_start(self.button2, False)
		self.button3 = gtk.Button("-")
		#self.button3.connect("clicked", self.exit)
		hbox.pack_start(self.button3, False)
		self.button4 = gtk.Button("Right")
		self.button4.connect("clicked", self.move_right)
		self.button4.connect("pressed", self.move_right)
		hbox.pack_start(self.button4, False)
		self.button5 = gtk.Button("Forward")
		self.button5.connect("clicked", self.move_forward)
		self.button5.connect("pressed", self.move_forward)
		hbox.pack_start(self.button5, False)
		self.button6 = gtk.Button("Left")
		self.button6.connect("clicked", self.move_left)
		self.button6.connect("pressed", self.move_left)
		hbox.pack_start(self.button6, False)
		
		hbox.add(gtk.Label())

		window.show_all()

        if os.path.exists(FIFO):
            os.unlink(FIFO)

        if os.path.exists(DUMP):
            os.unlink(DUMP)

        os.mkfifo(FIFO)

        command = MPLAYER_CMD  % (self.movie_window.window.xid)
        commandList = command.split()
        Popen(commandList, stdout=open(STDOUT,"w+b"), stderr=open(STDOUT,"r+b"))

        self.mplayerClient = open(FIFO,"w")

	def exit(self, widget, data=None):
		s.send('Q')
        mplayerClient.write('quit')
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
