class FirstClass:
	"""docstring for ClassName"""
	zalupa = "konya"
	def changezalupa(self,newzalupa):
	 		self.zalupa = newzalupa

class Two:
	"""docstring for ClassName"""
	zalupa1 = "umer muzhik"
	


n = FirstClass.changezalupa(Two.zalupa1)
print("What is zalupa? {1}".format(n.zalupa))