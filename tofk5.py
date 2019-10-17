import numpy as np
from astropy.coordinates import SkyCoord
from astropy import units as u

contin = np.loadtxt('output_coremass.txt',usecols=(0,2,4),dtype={'names': ('source','l','b'), 'formats': ('|S5',np.float,np.float)})
f = open('coreid_fk5.dat','w')


for i in np.arange(len(contin['source'])):
    c = SkyCoord(contin['l'][i], contin['b'][i], frame='galactic',unit=(u.deg, u.deg))
    ra = c.fk5.ra.degree
    dec = c.fk5.dec.degree 
    print >> f, contin['source'][i],ra,dec
    
    
f.close()