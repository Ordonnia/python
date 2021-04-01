class Credentials():
	def __init__(self):
		pass

	@classmethod
	def assign(cls, **kwargs):
		for key, value in kwargs.items():
			try:
				if cls.credentials != None:
					cls.credentials[key] = value
			except:
				cls.credentials = {}
				cls.credentials[key] = value

	@classmethod
	def clear(cls):
		del cls.Credentials
		return "Credentials have been cleared."