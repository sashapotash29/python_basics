# The Values will be in an array.
# The Hash() function will return the index where the value is stored.


class HashTable:

	def __init__(self,name="HashMap"):
		self.name = name
		self.size = 64
		self.list = [None] * self.size


	def get_hash(self, key):
		hsh = 0
		for character in str(key):
			hsh += ord(character)
		return hsh % self.size

	def show_hash_table(self):
		print("")
		print(str(self.name))
		for item in self.list:
			if item is not None:
				print(str(item))

	def add(self, key, value):
		hash_index = self.get_hash(key)
		hash_value = [key,value]

		if self.list[hash_index] == None:
			self.list[hash_index] = list([hash_value])
			print("Key (" + str(key) + ") and Value (" + str(value) + ") have been added.")
		else:
			for item in self.list[hash_index]:
				if item[0] == key:
					item[1] = value
					print("Updated Key (" + str(key) + ") to new Value (" + str(value) +").")
					return
			self.list[hash_index].append(hash_value)
			print("Key " + str(key) + " and Value " + str(value) + " have been added.")
			return
			
		

	def get(self, key):
		hash_index = self.get_hash(key)
		if self.list[hash_index] != None:
			for item in self.list[hash_index]:
				if item[0] == key:
					print("For Key (" + str(item[0]) + "), there is a value (" + str(item[1])+").")
				else:
					pass
		elif self.list[hash_index] == None:
			raise KeyError('No Key Found for parameter: ' + str(key))
		else:
			print("Generic Error")


	def delete(self,key):
		hash_index = self.get_hash(key)
		if self.list[hash_index] != None:
			for item in self.list[hash_index]:
				if item[0] == key:
					self.list[hash_index].pop(item)
				else:
					pass
		elif self.list[hash_index]==None:
			raise KeyError('No Key Found for parameter: ' + str(key))
		else:
			print("Generic Error")


hashTable = HashTable("My HashMap")
hashTable.add("key", "value")
hashTable.add(1, "one")
hashTable.add(3, "three")
hashTable.show_hash_table()
print("")
hashTable.get("key")
hashTable.get(1)
hashTable.get("blah")



		


