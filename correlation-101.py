import numpy

def correlation(x,y):
	temp = numpy.correlate(x,y,'full')
	result = temp[:temp.size/2 + 1]
	return result

hora = numpy.arange(0,24,1)

temp = [18.2,18.1,18,17.7,17.5,16.8,17.3,17.9,18.2,18.4,18.9,19,19.2,19.5,19.3,18.8,18.4,17.8,17.5,17.6,17.2,17.3,17.2,17.2]
lux = [10,10,10,100,200,500,850,1020,1200,1430,1900,1857,1500,1200,930,800,650,446,220,100,20,10,10,10]

r = numpy.corrcoef(temp,lux)
covar = numpy.cov(temp, lux)
cross_corr = correlation(temp,lux)
auto_corr_temp = correlation(temp,temp)
auto_corr_lux = correlation(lux,lux)
print "Correlation" 
print r
print "Covariance"
print covar
print "Cross Correlation"
print cross_corr
print "Temperature Auto Correlation"
print auto_corr_temp
print "Luminosity Auto Correlation"
print auto_corr_lux
exit()


