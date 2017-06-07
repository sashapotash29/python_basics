#TESTING


### Why do it?

- Testing is essential because it allows us to ensure the functionality of certain features as we continue to enhance/modify our system.
- In terms of web applications, if we were to add another feature that allows users to favorite messages from other users, we would like to hope that the part of the application that allows for message transfer remains functional.
- Hope no longer because we can do said checking with Testing

### Manual vs Automated

- Manual Testing is the process of physically testing each portion of code or function of an application one by one thus requiring physical man power and presence. 

- Automated Testing is the process of developing code that will run and/or ping different parts of your applications sytem to test its ability to work.

- Automated Testing is favored due to its ease to implement in the long run. (Press a button and watch it go)


### Good Testing Practices

- Know the Type and Scope of your Tests
	- Pay attention to where your test is running and what variables it needs access to.
	- Use a test framewokr that fits the situation.
- A single test should focus on a single thing.
	- If there is a test aims to verify a function that interprets the databases data and returns a result. Design a test for that specific function rather than the multiple processes that are required for the data to come from the database to the webpage (frontend).
- Write clear step by step procedures	
	- Before coding, think about what parts of the system you need to touch and what is the logic of your test. 1. Go to database and read data, 2. import Pandas library, 3. convert to dataframe, 4. etc.
	- The idea is to take a step back and think about how the process is unfolding on a basic level.
- Leave no trace.
	- Tests should run without modifying or changing the existing system. Meaning if a test was built to see if the database could be written to by some process, be sure that the data is then removed afterwards being it is most likely dummy data and/or redundant.

### UnitTest

- Python Testing Framework
- Unittest provides a 'TestCase' subclass that allows you to:
	- setUp, tearDown, assertion methods, 'test_' methods
- Positives and Negatives:
	- +: Easy to use for quick unit tests (i.e. a function)
	- -: Forces class inheritance.
	- -: Does not support parameterized test cases.

#### unittest Directory Layout
```
- root Directory
	- product packages
	- tests
		- __init__.py
		- test_<name>.py
	- README.md
```
#### unittest Example

##### calculator.py
```
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

```

##### unit_test.py

- First we import the unittest Module and our Calculator class from calculator.py
- Using Classical Inheritance, we create a calculator class that inherits 'unittest.TestCase'.
- Remember that this allows are custom class to utilize the functionality and properties of the 'unittest.testcase' class.

- General Procedure:
	- *Create setUp(self)* method which will create environment variable or in our case instantiate our Calculator class.
	- *Create 'test_<nameOfMethod>'(self)* methods for the methods you would like to test.
	- *NOTE* I have created the variables within the scope of each 'test_' method but this can be declared within the setUp() as a self.<propertyOfYourChoice> = data.
		- This may be critical if your testing value (or answer you would like to assert) is complex and needs to be generated through complex procedures.

```
from calculator import Calculator
import unittest

class CalculatorTest(unittest.TestCase):

	def setUp(self):
		self.calc = Calculator()

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



<!-- # INSTANTIATE THE TEST CLASS
# RUN setUp() method
# run 'test_' methods
# NOTE this can be ran from the command line as well!!!

# ct = CalculatorTest()

# ct.setUp()

# ct.test_add()

# ct.test_subtract() -->



if __name__ == '__main__':
	import xmlrunner
	unittest.main(
			testRunner = xmlrunner.XMLTestRunner(output='test-reports'),
			failfast = False,
			buffer = False,
			catchbreak = False
			)

```

- At the bottom of the code snippet, we import "xmlrunner" which allows us to run our tests and generate a report in XML format.
- The first parameter is the directory you would like to save the .xml file to. The other parameters were practices from another individual.


### 
