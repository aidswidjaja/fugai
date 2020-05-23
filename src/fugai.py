"""
Configuration file for Fugai Overlay (part of the Nettomo project).

NOTE: It is strongly recommended that values are provided for these variables. 
Not defining variables could cause a fatal error. Those notated as REQUIRED VALUE will
cause a fatal error if left undefined.

(c) 2020 Adrian Widjaja
https://github.com/nettomo/fugai
License information available in LICENSE.md
"""
# Change the background image. 
# Image must be a Qt supported format. https://doc.qt.io/qt-5/qtimageformats-index.html
# Default value = "overlay/src/res/default.png"
# REQUIRED VALUE
background_image = "overlay/src/res/default.png"

# Change the background colour. Colour value must be a hex code. 
# Default value = "#002040"
background_colour = "#002040"

# Change the opacity of the background.
# 0.0 –-> 1.0 (greater value = less transparency) 
# Default value = 0.8
opacity = 0.8

# Change the font used throughout Fugai. 
# Defualt value = 'Helvetica'
global_font = 'Helvetica'

# Change the font size used in clockView.
# Default value = '80'
clock_font_size = 80