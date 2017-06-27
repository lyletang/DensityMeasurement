#coding: utf-8

def getElasticityModulus(material):
	materialDic = {1: 2.0,\
		       2: 1.0,\
		       3: 0.1,\
		       4: 0.01\
		       }

	return materialDic[material]
