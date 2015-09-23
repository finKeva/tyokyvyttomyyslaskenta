from Laskuri.HashTable import Item as HashTableItem
from Laskuri.HashTable import HashTable as HashTable
import pandas

class Organization:
	'Organisaatioluokka sisältää kaiken datan joka liittyy organisaatioon'
	def __init__(self, name, dataFilePath):
		self.name = name
		self.persons = HashTable(1000)
		self.units = HashTable(50)
		self.serviceRelations = HashTable(1000)
		if bool(dataFilePath) == True:
			self.dataFilePath = dataFilePath 
		else:
			raise NameError("NoData")
	
	def __str__(self):
		return 'instance of Organization, name: ' + self.name
	
	def __repr__(self):
         return "Organization()"
	
	def getName():
		return self.name
	
	def buildSctructure(self):
		import Laskuri.Unit as Unit
		import Laskuri.Person as Person
		import Laskuri.ServiceRelation as ServiceRelation
		
		#open data from csv
		print("Opening data...", end=" ", flush=True)
		self.data = pandas.read_csv(self.dataFilePath, sep=";", encoding="utf-8")
		print("done! (lines: %d)" % len(self.data))
		
		#convert dates into cs format
		print("Converting dates...", end=" ", flush=True)
		self.data['alk'] = pandas.to_datetime(self.data['alk'], format="%d.%m.%Y")
		self.data['paat']= pandas.to_datetime(self.data['paat'], format="%d.%m.%Y")
		print("done!")
		
		#create units
		print("Creating units...", end=" ", flush=True)
		units = pandas.unique(self.data['toimiala'])
		for unitName in units:
			newUnit = Unit(unitName)
			self.units.insert(HashTableItem(unitName, newUnit))
		print("done! (amount: %d)" % self.units.getNumEntries())
		
		print("Creating persons and servicerelations...", end=" ", flush=True)
		for row_index, row in self.data.iterrows():
			newPerson = self.persons.get(str(row['id']))

			if newPerson == None:
				newPerson = Person(str(row['id']))
				self.persons.insert(HashTableItem(newPerson.getId(), newPerson))
			else:
				newPerson = newPerson.value

			#getting persons unit
			personsUnit = self.units.get(str(row['toimiala'])).value
			
			#creating servicerelation
			newServiceRelation = ServiceRelation(newPerson, personsUnit, row['palkkatyyppi'], row['palkka'])
			self.serviceRelations.insert(HashTableItem(newServiceRelation.getId(), newServiceRelation))
			
			#linking servicerelation to person and unit
			personsUnit.addServiceRelation(newServiceRelation)
			newPerson.addServiceRelation(newServiceRelation)
		
			newPerson.addSickLeave(row['alk'], row['paat'])
			
		print("done! (num of persons: %d)" % self.persons.getNumEntries())
		
		#create henkilot
		#persons = pandas.unique(self.data['id'])
		#for personId in persons:
		#	newPerson = Person(str(personId))
		#	self.persons.insert(HashTableItem(newPerson.getId(), newPerson))
		#print("Persons created")
		#print(self.persons.print())
		
		#create palvelusuhteet