"""
Configuration file for Fugai Overlay (part of the Nettomo project).

NOTE: It is strongly recommended that values are provided for all these variables. 
Not defining variables could cause a fatal error. Those notated as REQUIRED VALUE will
cause definietly a fatal error if left undefined.

    NameError: name 'variable' is not defined

^ an example of a warning you might see if a variable is left undefined

***

2020 (c) aidswidjaja and other contributors.
https://github.com/nettomo/fugai
https://aidswidjaja.github.io

This program is free software: you can redistribute it and/or modify
it under the terms of the MIT License as originally published by
the Massachusetts Institute of Technology and currently maintained by
the Open Source Initiative.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
MIT License for more details.

You should have received a copy of the MIT License
along with this program.  If not, see <https://opensource.org/licenses/MIT>.
"""
# Change the background image. 
# Image must be a Qt supported format. https://doc.qt.io/qt-5/qtimageformats-index.html
# Default value = "overlay/src/res/default.png"
# REQUIRED VALUE
background_image = "overlay/src/res/default.png"

# Change the background colour. Colour value must be a hex code. 
# Default value = "#002040"
# REQUIRED VALUE
background_colour = "#002040"

# Change the opacity of the background.
# 0.0 –-> 1.0 (greater value = less transparency) 
# Default value = 0.8
# REQUIRED VALUE
opacity = 0.8

# Change the font used in clockView.
# Defualt value = 'Helvetica'
# REQUIRED VALUE
clock_font = 'Helvetica'

# Change the font size used in clockView.
# Default value = '80'
# REQUIRED VALUE
clock_font_size = 80

# Change the font colour used in clockView.
# Default value = "white"
# REQUIRED VALUE
clock_font_colour = "white"