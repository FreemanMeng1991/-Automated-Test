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

	#unittest.defaultTestLoader实际上是一个TestLoader实例
	loader = unittest.defaultTestLoader
	#getTestCaseNames()方法获取一个TastCase实例中所有测试用例的名称
	test_cases = loader.getTestCaseNames(TestStringMethods())
	print(test_cases)

	results    = unittest.TestResult()
	case_names = ["testonly.test.TestStringMethods.test_split",
	              "testonly.test.TestStringMethods.test_upper",
	              "testonly.test.TestStringMethods.test_isupper"]

	#loadTestsFromNames()方法用于向TestLoader实例中批量添加测试用例，
	#所有待添加的用例名称都存储在一个列表中，用例名称用上述点分路径表示
	#注意：
	#使用loadTestsFromName(s)，要求将被测代码当做一个模块来处理，因此需将其
	#放到python解释器可以搜索到模块存放路径中，这里将模块testonly放置于site-packages中
	#模块内文件： ../testonly/__init__.py   ../testonly/test.py  
	test_suite = loader.loadTestsFromNames(case_names) #返回TestSuite对象
	test_suite.run(results)
	
	#loadTestsFromName()向TestLoader实例中添加单个测试用例
	loader.loadTestsFromName("testonly.test.TestStringMethods.test_split").run(results)
	
	#loadTestsFromTestCase()向TestLoader实例中加载某个TestCase实例中的所有测试用例
	#并返回一个TestSuite实例
	loader.loadTestsFromTestCase(TestStringMethods).run(results)
	
	#loadTestsFromModule()向TestLoader实例中加载某个模块(这里是testonly.test)中所有
	#继承自TestCase类的实例，并将其中的测试用例添加至TestLoader实例中
	#注意：
	#传递给loadTestsFromModule()方法的参数所指向的模块中，若实现了load_tests()，则只会
	#向TestLoader中加载load_tests()方法中指定的测试用例，而不是该模块中包含的所有测试用例。
	loader.loadTestsFromModule(testonly.test).run(results)
	print(results)
	for a,b in results.errors:
		print("---"*20,"\n",a,"\n",b)
	
'''
******************Points*****************************
TestLoader类
unittest.defaultTestLoader
getTestCaseNames()     loadTestsFromName()
loadTestsFromNames()   loadTestsFromTestCase()
loadTestsFromModule()
'''
	



