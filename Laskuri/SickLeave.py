class SickLeavePeriodContainer:
	'Yksittäinen sairauspoissaolo'
	
	def __init__(self):
		self.sickLeaves = []
		self.sickLeavesCount = 0
	
	def addSickLeave(self, startDate, endDate):
		self.sickLeaves.append([startDate, endDate])
		self.sickLeavesCount += 1
	
	def getSickLeavesCount(self):
		return self.sickLeavesCount
	
	def getSickLeaves(self):
		return self.sickLeaves
	
	def organizeSickLeaves(self):
		False
		
class SickLeavePeriod:
	'Yksittäinen sairauspoissaolo'
	slpCount = 0;
	
	def __init__(self, startDate, endDate):
		self.startDate = startDate
		self.endDate = endDate
		SickLeave.slCount += 1

class SickLeave:
	'Yksittäinen sairauspoissaolo'
	slCount = 0;
	
	def __init__(self, startDate, endDate):
		self.startDate = startDate
		self.endDate = endDate
		SickLeave.slCount += 1