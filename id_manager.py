import csv

class IDManager():
	
	def __init__(self):
		self.master_IDs = set()
		self.scanned_IDs = set()

		self.path = None

		self.initialized = False

	def set_path(self, path):
		with open(path, newline = '') as file:
			ID_reader = csv.reader(file)
			for row in ID_reader:
				self.master_IDs.add(row[1])

		self.initialized = True

	def add_scanned_ID(self, ID):
		self.scanned_IDs.add(ID)

	def get_missing_IDs(self):
		return self.master_IDs - self.scanned_IDs if self.initialized else None

	def get_unexpected_IDs(self):
		return self.scanned_IDs - self.master_IDs if self.initialized else None