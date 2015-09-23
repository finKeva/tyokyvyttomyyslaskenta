class Person:
	'Henkilö'
	personCount = 0
	
	def __init__(self,id):
		import Laskuri.ServiceRelation
		from Laskuri.SickLeave import SickLeavePeriodContainer as SickLeavePeriodContainer
		self.id = id
		self.srs = []
		self.sickLeaves = SickLeavePeriodContainer()
		Person.personCount += 1
	
	def __str__(self):
		#lisää ammattikenttä
		#id:nä voi olla hetu
		return 'instance of Person, id: ' + self.id
	
	def __repr__(self):
         return "Person()"
	
	def getId(self):
		return self.id
	
	def addServiceRelation(self, sr):
		self.srs.append(sr)
	
	def addSickLeave(self, startDate, endDate):
		self.sickLeaves.addSickLeave(startDate, endDate)
		#jotain tänne
	
	def organizeSickLeaves(self):
		self.sickLeaves.organizeSickLeaves()
	
	def getSickLeavesCount(self):
		return self.sickLeaves.getSickLeavesCount()
	
	def getSickLeaves(self):
		return self.sickLeaves.getSickLeaves()
	