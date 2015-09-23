from Laskuri.HashTable import Item as HashTableItem
from Laskuri.HashTable import HashTable as HashTable

class Unit:
	'Organisaation yksikkö'
	unitCount = 0
	
	def __init__(self,id):
		import Laskuri.ServiceRelation
		self.id = id
		self.srs = HashTable(1000)
		Unit.unitCount += 1
		
	def __str__(self):
		return 'instance of Unit, id: ' + self.id
	
	def __repr__(self):
         return "Unit()"
	
	def getId(self):
		return self.id
	
	def addServiceRelation(self, sr):
		self.srs.insert(HashTableItem(sr.getId(), sr))