
The program: logmaker.py

This program looks in a given directory with fits files.
It writes a new textfile with header information from the fits files. 
The first lines can be edited, and currently list the UT date and Telescope Information.
It will list in column format:
  -Fits file name
  -Object Name
  -Airmass
  -Exposure time
  -Image type

BUG: Currently, the columns get misaligned with wierd spacings. tbf
