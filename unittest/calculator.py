class Calculator:

	def __init__(self, last_value = None):
		self.last_value = last_value


	def add(self, number1, number2):
		answer = number1+number2
		print(str(answer))
		self.last_value = answer
		return self.last_value

	def subtract(self, number1, number2):
		answer = number1-number2
		print(str(answer))
		self.last_value = answer
		return self.last_value

	def multiply(self, number1, number2):
		answer = number1*number2
		print(str(answer))
		self.last_value = answer
		return self.last_value

	def division(self, number1, number2):
		answer = number1/number2
		print(str(answer))
		self.last_value = answer
		return self.last_value
