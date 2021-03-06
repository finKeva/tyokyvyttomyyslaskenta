#!/usr/bin/env python
 
import sys
 
class Item:
	key   = ""
	value = 0
 
	def __init__(self,key,value):
		self.key = key
		self.value = value
 
	def print(self):
		print("  '" + self.key + "' / " + str(self.value) )
	 
 
class HashTable:
	'Common base class for a hash table'
	tableSize	= 0
	entriesCount = 0
	alphabetSize = 2*26
	hashTable	= []
	 
 
	def __init__(self, size):
		self.tableSize = size
		self.hashTable = [[] for i in range(size)]
 
	def char2int(self,char):
		if char == 'ä' or char == 'å' or char == ' ' or char == '-' or char == '_' or char == '.' or char == ',':
			char = 'a'
		elif char == 'Ä' or char == 'Å':
			char = 'A'
		elif char == 'ö':
			char = 'o'
		elif char == 'Ö':
			char = 'O'
		
		if char >= '0' and char <= '9':
			return ord(char)-48
		if char >= 'A' and char <= 'Z':
			return ord(char)-65
		elif char >= 'a' and char <= 'z':
			return ord(char)-65-7
		else:
			raise NameError('Invalid character in key! Alphabet is [a-z][A-Z] ('+char+')')
		 
	def hashing(self,key):
		hash = 0
		for i,c in enumerate ( key ):
			hash += pow(self.alphabetSize, len(key)-i-1) * self.char2int(c)
		return hash % self.tableSize
 
	def insert(self,item):
		hash = self.hashing(item.key)
		# print(hash)
		for i,it in enumerate(self.hashTable[hash]):
			if it.key == item.key:
				del self.hashTable[hash][i]
				self.entriesCount -= 1
		self.hashTable[hash].append(item)
		self.entriesCount += 1		   
 
	def get(self,key):
		#print ("Getting item(s) with key '" + key + "'")
		hash = self.hashing(key)
		for i,it in enumerate(self.hashTable[hash]):
			if it.key == key:
				return it #self.hashTable[hash]
		#print (" NOT IN TABLE!")			
		return None
 
	def getAll(self):
		forReturn = []
		for i in range(0,self.tableSize-1):
			forReturn.extend(self.hashTable[i])
		return forReturn
 
	def delete(self,key):
		#print ("Deleting item with key '" + key + "'")
		hash = self.hashing(key)
		for i,it in enumerate(self.hashTable[hash]):
			if it.key == key:
				del self.hashTable[hash][i]
				self.entriesCount -= 1
				return
		#print (" NOT IN TABLE!")			
			 
	def print(self):
		print ( ">>>>> CURRENT TABLE BEGIN >>>>" )
		print ( str(self.getNumEntries()) + " entries in table" )
		for i in range(self.tableSize):
			print ( " [" + str(i) + "]: " )
			for j in range(len(self.hashTable[i])):
				self.hashTable[i][j].print()
		print ( "<<<<< CURRENT TABLE END <<<<<" )
 
	def getNumEntries(self):
		return self.entriesCount
 
 
if __name__ == "__main__":
	hs = HashTable(11)
 
	item = Item("one",1)
	hs.insert(item)
	hs.print()
	hs.insert(item)
	hs.print()
 
	item = Item("two",2)
	hs.insert(item)
 
	item = Item("three",3)
	hs.insert(item)
	hs.print()
 
	item = Item("one",4);
	hs.insert(item);
 
	items = hs.get("one");
	if items != None:
		for j in range(len(items)):
			items[j].print()
	 
	item = Item("PheewThisIsALongOne",12345)
	hs.insert(item)
	hs.print()
 
	items = hs.get("PheewThisIsALongOne")
	if items != None:
		for j in range(len(items)):
			items[j].print()
		 
	items = hs.get("PheewThisIsOne")
	if items != None:
		for j in range(len(items)):
			items[j].print()
		 
	hs.delete("PheewThisIsALongOne")
	hs.print()
 
	hs.delete("PheewThisIsTheOne")
	hs.print()
 
	hs.delete("one")
	hs.print()
 
	# This one leads to an exception as '!' is not part of the allowed alphabet
	# item = Item("!", 5)
	# hs.insert(item)