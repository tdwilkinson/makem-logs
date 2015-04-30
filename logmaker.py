import numpy as np
import matplotlib.pyplot as plt
import pyfits 
import numpy.ma as ma
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

#   attempt one: 
# read in file
#star_files = [f for f in listdir(".") if isfile(join(".",f))]
# to specify specific files add something like =>    and f[0] == "d"
#print star_files  #test
#for filename in star_files:
#
#	star_list = fits.open(filename) 
#	star = star_list[0]   #to specify this HDU (object)
#	
#	namefile = star.header['filename']
#	name = star.header['OBJNAME']
#	airmass = star.header['airmass']
#	exptime = star.header['exptime']
#	objtype = star.header['imagetyp']
#	a = np.array(namefile,name,airmass,exptime,objtype)
#	newfile.write(a)

newfile.close()



###################################################
#load fits file
#hdulist_b = pyfits.open('e_copy_objb.r.fits')
#open primary HDU 
#hdu_b = hdulist_b[0]
#obtain flux from fits file
#bdata = hdu_b.data[0][0]
#print max(cdata)
#to mask the values of 0.0 to an average of the nearby numbers
#b = ma.masked_equal(bdata,0.0) 
#replaceb = (b[-1]+b[1])/2.0
#newb = b.filled(replaceb)
########  ISNAN: 
#print np.count_nonzero(~np.isnan(bdata))
#print np.count_nonzero(np.isnan(cdata))
#### without ~ this gives elements missing in array.  0
#### with ~ it gives the number of non-missing elements in array. 2048
# make the array in the header match what is done above
#hdulist_b[0].data[0][0] = newb
																											#to save the file
#hdulist_b.writeto('e_updated_objb.b.fits')
##################################################
#test portion:
#x = np.array([1.0,2.0,3.0,0.0,4.0,5.0])
#m = ma.masked_equal(x,0.0)
#replacem = (m[-1]+m[1])/2.0
#newm = m.filled(replacem) 
#x = newm
#print x    #huzzah!



