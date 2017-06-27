#coding: utf-8

def getDensity(elasticityModulus, throughTime,  temperature = 25, distance = 0.15, objectLength = 0.05):
	elasticityModulus = elasticityModulus
	throughTime = throughTime
	temperature = 25

	#temperature compensation
	cAir = 332 + 0.607 * temperature

	dAir = dsitance - objectLength
	
	tAir = dAir / float(cAir)

	tObject = throughTime - tAir
	
	cObject = objectLength / float(tObject)

	#c = 1 / math.sqrt(elasticityModulus * density)
	density = 1 / float(pow(cObject, 2) * elasticityModulus)

	return density
