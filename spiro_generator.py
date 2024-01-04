#!/usr/local/bin/python3
import numpy as np
from math import cos, sin, pi

centerX = -118.28544531620815
centerY = 34.020555041445604

R = 36
r = 9
a = 30
N = 30000
nRevs = 24

f = open("spiro.kml", 'w')
f.write("<?xml version='1.0' encoding='UTF-8'?>\n")
f.write("<kml xmlns='http://www.opengis.net/kml/2.2'>\n")
f.write("<Folder>\n")
f.write("<Style id='z1'>\n")
f.write("<IconStyle><Icon><href>http://www.google.com/intl/en_us/mapfiles/ms/micons/blue-dot.png</href></Icon></IconStyle>\n")
f.write("</Style>\n")
f.write("<Placemark>\n")
f.write("<styleUrl>#z1</styleUrl><Point><coordinates>-118.28551117649391,34.02073082963444</coordinates></Point>\n")
f.write("</Placemark>\n")
f.write("<Placemark>\n")
f.write("<LineString>\n")
f.write("<visibility>1</visibility>\n")
f.write("<extrude>1</extrude>\n")
f.write("<tessellate>1</tessellate>\n")
f.write("<coordinates>\n")

for t in np.arange(0.0, pi * nRevs, 0.02):
    x = ((R + r) * cos((r / R) * t) - a * cos((1 + r / R) * t)) / N + centerX
    y = ((R + r) * sin((r / R) * t) - a * sin((1 + r / R) * t)) / N + centerY

    f.write(str(x) + "," + str(y) + ",0.0" + "\n")

f.write("</coordinates>\n")
f.write("</LineString>\n")
f.write("</Placemark>\n")
f.write("</Folder>\n")
f.write("</kml>\n")

f.close()
