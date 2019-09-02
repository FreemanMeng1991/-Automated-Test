import unittest,testonly
import math


class TestStringMethods(unittest.TestCase):
	#实例化一个TestCase类，该实例用来存放测试用例
	#执行单元测试时的函数调用顺序：
	#run()->setUp()->test_xxx()->tearDown()->doCleanups()
	# def setUp(self):
	# 	print("Set up")

	# def tearDown(self):
	# 	print("Tear down")	

	# def doCleanups(send_keys):
	# 	print("Run doCleanups")

    #装饰器(以@开头)，启用该装饰器后跳过这个测试用例
    #相关装饰器：skip skipIf skipUnless expectedFailure skipTest
	@unittest.skip("Too easy")  
	#测试用例默认以test开头，这是由loader.py中testMethodPrefix = 'test' 所致
	def test_upper(self):
		print("Run test_upper")
		self.assertEqual('foo'.upper(), 'FOO')

	def test_isupper(self):
		print("Run test_isupper")
		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())

	def test_split(self):
		print("Run test_split")
		s = 'hello world'
		self.assertEqual(s.split(), ['hello', 'world'])
		# check that s.split fails when the separator is not a string
		with self.assertRaises(TypeError):
			s.split(2)

	def another_test_split(self):
		print("Run another_test_split")
		s = 'hello world'
		self.assertEqual(s.split(), ['hello', 'world'])
		# check that s.split fails when the separator is not a string
		with self.assertRaises(TypeError):
			s.split(2)

	def runTest(self):
		print("Run runTest")
		self.assertEqual('foo'.upper(), 'FOO')

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




		
		


def suite():
	#TestSuite对象：将所有或部分测试用例按一定的顺序和结构组织起来，成为一个测试集
	suite = unittest.TestSuite()
	#addTest()：向测试集中添加单个测试用例
	# suite.addTest(TestStringMethods('test_upper')) 
	# suite.addTest(TestStringMethods('test_split'))
	# suite.addTest(TestStringMethods('test_isupper'))
	
	#addTests()：向测试集中一并加载位于某一容器中的所有测试用例
	tests = [TestStringMethods('test_split'),TestStringMethods('test_upper')]
	suite.addTests(tests) 
	return suite

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
	
	#TextTestRunner类中的run():
	#这里的run()方法接受一个TestSuite对象或TestCase对象为参数
	#并测试TestSuite对象中的所有测试用例和TestCase对象中的某一测试用例
	#测试结果将输出到某一输出流中(默认值为std.__err__, 交互式编译器的输出流)
	
	#输出到文件test.log文件
	# fp = open("test.log","w")
	# runner = unittest.TextTestRunner(stream=fp)
	
	#输出到默认输出流std.__err__
	runner = unittest.TextTestRunner()
	
	runner.run(suite())             #运行TestSuit对象中的所有测试用例
	runner.run(TestStringMethods()) #默认运行TestStringMethods对象中的runTest用例
	runner.run(TestStringMethods("test_split")) #运行TestStringMethods对象中的test_split用例
	





