##############################################################
#Script written by Evangelia Tremou(E.T.)					 #
#for calculating the synchrotron lifetime of a galaxy 		 #
#Synchrotron age is depending on Magnetic Field strength,	 #
#redshift, radio frequency and  the equivalent magnetic field#
#of the microwave background. More info can be found in      #
#van der Laan & Perola (1969), Parma et al. 1999, 			 #
#Murgia et al.1999			 								 #
##############################################################

import math

print '******************************************************************************************************'
print 'Welcome!'
print ''
print 'Find out the synchrotron lifetime in a galaxy'
print ''
print 'Script written by E.T.'
print ''
print 'Facing issues, having suggestions for impovement?'
print ''
print 'Please do not hesitate to contact me : ***etremou@gmail.com***'
print '******************************************************************************************************'

redshift = float(raw_input('Please type the redshift of the galaxy :'))
print ''
print 'Your galaxy is at redshift z =', redshift ,'!!!'
print ''

#Define the function of the equivalent magnetic field
def equiv_magn_field(redshift):
	b_r = 3.25*((1.0+redshift)**2)
	return b_r
	
emf=equiv_magn_field(redshift)
print 'The strength of the equivalent magnetic field is: B_r =', emf ,'uGauss!'
print ''

freq = float(raw_input('Please type the observed frequency in GigaHertz :'))
print ''
print 'Your observed frequency is  nu =', freq ,'GHz!!!'
print ''

Hzfreq=freq*10**9


flux_dens = float(raw_input('Please type the flux density in Jansky at the above observed frequency:'))
print ''
print 'Your flux density is  S_(nu) =', flux_dens ,'Jy!!!'
print ''

print '******************************************************************************************************'
print '*******************************************FYI*******************************************************'
print '******************************************************************************************************'
print 'Assuming cylindrical symmetry we can obtain the path length through the source in the line of sight'
print 'equal to the width of the source in the plane of the sky.'
print '******************************************************************************************************'
print '************************************More details at  Miley et al. 1980********************************' 
print '******************************************************************************************************'
print '' 

theta_x = float(raw_input('Please type the semimajor axis of the observing beam in arcseconds at the above observed frequency :'))
print ''
print 'The width of the source in x axis is theta_x =', theta_x ,'arcsec!!!'
print ''

theta_y = float(raw_input('Please type the semiminor axis of the observing beam in arcseconds at the above observed frequency :'))
print ''
print 'The width of the source in y axis is theta_y =', theta_y ,'arcsec!!!'
print ''

rkpc = float(raw_input('Please type the path length through the source in kpc : '))
print ''
print 'The path length through your source is = ', rkpc, 'kpc!!!'
print ''


#Define the function of the magnetic field strength	
def magnfield(redshift,flux_dens,rkpc,theta_x,theta_y,freq):
	magn = (1.4*(10.0**(4.0)))*((1+redshift)**(1.1))*(freq**(0.22))*(flux_dens/(theta_x*theta_y*rkpc))**(2.0/7.0)
	return magn
	
magn_field = magnfield(redshift,flux_dens,rkpc,theta_x,theta_y,freq)

print ''
print 'The strength of the magnetic field is: B =', magn_field*(10**(-6)) ,'uGauss!'
print ''
	
	
nu_break = float(raw_input('Please type the break frequency in GigaHertz  : '))
print ''
print 'The break frequency is = ', nu_break, 'GHz!!!'
print ''

	
#Define the function of the synchrotron lifetime	
def synch_age(nu_break,redshift,magn_field,emf):
	tsynch = ((1.61*(10.0**(3.0)))*(magn_field**(0.5))/(magn_field**(2.0))+(emf**(2.0)))*(((1.0+redshift)*nu_break)**(-1.0/2.0))
	return tsynch
	
t_synch	= synch_age(nu_break,redshift,magn_field,emf)
	
print ''
print 'The synchrotron lifetime is: t_synchrotron =', t_synch ,'Myrs!'
print ''

print 'Thank you for using the script!'
print 'If you enjoyed it please do not forget to acknowledge us at https://github.com/tremou'
