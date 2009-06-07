#!/bin/sh
VPORT=5434
APORT=5432
HOST=${1:-192.168.1.106}
gst-launch-0.10 gconfv4l2src ! video/x-raw-yuv,width=176,height=144,framerate=\(fraction\)15/1 ! hantro4200enc stream-type=1 profile-and-level=1001 ! video/x-h263,framerate=\(fraction\)15/1 ! rtph263ppay mtu=1438 ! udpsink host=$HOST port=$VPORT dsppcmsrc ! queue ! audio/x-raw-int,channels=1,rate=8000 ! mulawenc ! rtppcmupay mtu=1438 ! udpsink host=$HOST port=$APORT
