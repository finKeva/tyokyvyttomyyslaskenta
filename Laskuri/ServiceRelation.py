import decimal

class ServiceRelation:
	'Palvelussuhde'
	srCount = 0
	
	def __init__(self, person, unit, wageType, wage):
		#import Laskuri.Unit, Laskuri.Person
		
		#if(isinstance(person, Laskuri.Person)):
		self.person = person
		#else:
		#	raise NameError("NoPersonObject")
		
		#if(isinstance(unit, Laskuri.Unit.Unit)):
		self.unit = unit
		#else:
		#	raise NameError("NoUnitObject")
		
		if wageType.upper() == 'T' or wageType.upper() == 'H':
			self.wageType = wageType
		else:
			raise NameError("WrongWageType")
			
		self.wage = decimal.Decimal(wage)
		
		ServiceRelation.srCount += 1
	
	def __str__(self):
		return 'instance of ServiceRelation, personId: ' + self.person.getId() + ', unitId: ' + self.unit.getId()
	
	def __repr__(self):
         return "ServiceRelation()"
	
	def getId(self):
		return self.unit.getId() + '-' + self.wageType + '-' + self.wageType + '-' + self.person.getId()