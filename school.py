class School:
	def __init__(self, name=None,  roster={}):
		self.name = name
		self.roster = roster
        
	def add_student(self, full_name, grade):
		self.roster.setdefault(grade, []).append(full_name)
        
	def grade(self, grade):
		return self.roster[grade]
    
	def sort_roster(self):
		new_dict = self.roster
		for key in new_dict:
			new_dict[key].sort()
		return new_dict
