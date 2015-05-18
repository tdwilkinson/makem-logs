import numpy as np
import matplotlib.pyplot as plt
import pyfits 
import pyfits 
from astropy.io import fits
from os import listdir  # will get files in directory
from os.path import isfile,join
import glob

#open file
newfile = open('obsnotes_140520.txt','w')

#write UT Date     \n =new line
newfile.write('UT140520\n')
#write observatory name , instrument
newfile.write('APO 3.5m DIS-High \n \n')

#make column labels:
newfile.write( "#FileName		ObjectName	Airmass		Exptime	Imagetype \n \n")

a = []

for fitsName in glob.glob('*.fits'):
	hdulist = pyfits.open(fitsName)
	namefile = hdulist[0].header['filename']
	name = hdulist[0].header['OBJNAME']
	airmass = hdulist[0].header['airmass']
	exptime = hdulist[0].header['exptime']
	objtype = hdulist[0].header['imagetyp']
	a.append([namefile,name,airmass,exptime,objtype])
	hdulist.close()

a = np.array(a).T

# it printed lists with the above forloop so need them to be grouped together
for i in range(len(a[0])):
	if (namefile[0] == 'b' or 'f'):
		newfile.write(str(a[0][i]) + '\t \t' + str(a[1][i])  + '\t' + str(a[2][i])  + '\t' + str(a[3][i]) + '\t'+ str(a[4][i]) + '\n')
	else:
		newfile.write(str(a[0][i]) + '\t'+ str(a[1][i])  + '\t' + str(a[2][i])  + '\t' + str(a[3][i]) + '\t'+ str(a[4][i]) + '\n')
newfile.close()
