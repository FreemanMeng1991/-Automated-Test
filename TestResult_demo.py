import unittest,testonly
import math

class ForTestResult(unittest.TestCase):

	def test_errors(self):
		print("Run test_errors")
		1/0 #故意制造错误，在测试过程中产生意外的异常情况
		self.assertEqual(math.sqrt(4),2.0)

	def test_failures(self):
		print("Run test_failures")
		self.assertEqual(math.sqrt(4),3.0)

	@unittest.skip("Do nothing")
	def test_skip():
		pass

	@unittest.expectedFailure
	def test_expected_failure(self):
		#期望出现失败，若测试结果为失败则证明测试成功
		print("Run test_expected_failure")
		self.assertEqual(math.sqrt(4),3.0)


def suite_for_TestResult():
	suite = unittest.TestSuite()
	tests = [ForTestResult('test_errors'),
	         ForTestResult('test_failures'),
	         ForTestResult('test_skip'),
	         ForTestResult('test_expected_failure')
	        ]
	suite.addTests(tests) 
	return suite



if __name__ == '__main__':
	results = unittest.TestResult()
	test_suite = suite_for_TestResult()
	test_suite.run(results)
	print(results)
	print("Run",results.testsRun,"tests in total\n")
	print("*",results.errors)
	print("**",results.failures)
	print("***",results.skipped)
	print("****",results.expectedFailures)
	
'''
******************Points*****************************
TestResult类
testsRun()  errors()  failures()
skipped()   expectedFailures()
'''




