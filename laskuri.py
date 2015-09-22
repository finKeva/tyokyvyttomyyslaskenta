from Laskuri.Organization import *
from Laskuri.Unit import *
from Laskuri.Person import *
from Laskuri.ServiceRelation import *
from Laskuri.SickLeave import *

import csv 
import numpy
import pandas

#HUOM! datan pitää olla UTF-8 without BOM koodattu!
test_org = Organization("esim", "esimdata.csv")
#print(test_org)

test_org.buildSctructure()

temp = pandas.read_csv("esimdata.csv", sep=";", encoding="utf-8")
#temp['alk'] = pandas.to_datetime(temp['alk'])
#temp['paat']= pandas.to_datetime(temp['paat'])




#for row_index, row in temp.iterrows():
#	if(row_index>3):
#		break
#	print('%s\n%s' % (row_index, row))
#	print(row['id'])
	
#print(temp.dtypes)
#print(temp.head())
#id;alk;paat;palkallisuus;toimiala;palkkatyyppi;palkka
