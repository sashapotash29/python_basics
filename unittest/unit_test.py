from calculator import Calculator
import unittest


x = 5
y = 4


class CalculatorTest(unittest.TestCase):

	def setUp(self):
		self.calc = Calculator()
		number1 = 5
		number2 = 3

	def test_add(self):
		number1 = 5
		number2 = 3
		value = self.calc.add(number1, number2)
		self.assertEquals(value, 9, 'FAILURE')

	def test_subtract(self):
		number1 = 5
		number2 = 3
		value = self.calc.subtract(number1, number2)
		self.assertEquals(value, 1, 'FAILURE')



# INSTANTIATE THE TEST CLASS
# RUN setUp() method
# run 'test_' methods
# NOTE this can be ran from the command line as well!!!

# ct = CalculatorTest()

# ct.setUp()

# ct.test_add()

# ct.test_subtract()



if __name__ == '__main__':
	import xmlrunner
	unittest.main(
			testRunner = xmlrunner.XMLTestRunner(output='test-reports'),
			failfast = False,
			buffer = False,
			catchbreak = False
			)


	