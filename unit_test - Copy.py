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

	#unittest.main提供命令行接口，命令格式：python test_code.py [-v]
	#.表示通过，s表示跳过，E表示出现错误（异常）
	#main()运行TestCase对象中的每个测试用例，实际是每次调用TestCase.run()方法
	#可选参数： verbosity = 0,1,2 数字越大，信息越详细，大于2时与2作用相同
	# unittest.main()
	
	#TestCase类中的run()方法：
	#一个TestCase类中可以有一个或多个测试用例，每个测试用例就是一个方法
	#实例化一个TestCase类后，若构造函数的参数缺省，run()会默认调用runTest()方法，
	#若该方法未实现则会报错。
	# result = TestStringMethods().run()
	# print(result)
	
	#若TestCase中有多个测试用例，在构造参数中指定该测试用例的方法名后，run()会调用
	#该方法而不是默认的runTest()方法
	#注意：这里   不强制要求   方法名必须以test开头
	# result = TestStringMethods("another_test_split").run()
	# print(result)
	
	#TestSuite类中的的run()方法：
	#不同于TestCase类，这里的run()方法需要一个TestResult对象作为参数来
	#记录测试结果，因此在使用TestSuite.run()之前，确保创建一个TestResult对象
	# result = unittest.TestResult()
	# suite = suite()   #创建一个TestSuite实例
	# suite.run(result) 

	#debug()方法执行TestSuite对象中的所有测试用例，但测试结果不会保存，
	#且测试用例中的异常会传递到主调函数
	# suite = suite()   #创建一个TestSuite实例
	# suite.debug() 
	# print(suite.countTestCases()) #获取TestSuite中的测试用例数量
	# print("#####",result.skipped)
	
	#TextTestRunner类中的run():
	#这里的run()方法接受一个TestSuite对象或TestCase对象为参数
	#并测试TestSuite对象中的所有测试用例和TestCase对象中的某一测试用例
	#测试结果将输出到某一输出流中(默认值为std.__err__, 交互式编译器的输出流)
	
	#输出到文件test.log文件
	# fp = open("test.log","w")
	# runner = unittest.TextTestRunner(stream=fp)
	
	#输出到默认输出流std.__err__
	# runner = unittest.TextTestRunner()
	
	# runner.run(suite())
	# runner.run(TestStringMethods())
	# runner.run(TestStringMethods("test_split"))
	
	#unittest.defaultTestLoader实际上是一个TestLoader实例
	# loader = unittest.defaultTestLoader
	#getTestCaseNames()方法获取一个TastCase实例中所有测试用例的名称
	# test_cases = loader.getTestCaseNames(TestStringMethods())
	# results    = unittest.TestResult()
	# case_names = ["testonly.test.TestStringMethods.test_split",
	              # "testonly.test.TestStringMethods.test_upper",
	              # "testonly.test.TestStringMethods.test_isupper"]

	#loadTestsFromNames()方法用于向TestLoader实例中批量添加测试用例，
	#所有待添加的用例名称都存储在一个列表中，用例名称用上述点分路径表示
	#注意：
	#使用loadTestsFromName(s)，要求将被测代码当做一个模块来处理，因此需将其
	#放到python解释器可以搜索到模块存放路径中，这里将模块testonly放置于site-packages中
	#模块内文件： ../testonly/__init__.py   ../testonly/test.py  
	# test_suite = loader.loadTestsFromNames(case_names) #返回TestSuite对象
	# test_suite.run(results)
	#loadTestsFromName()向TestLoader实例中添加单个测试用例
	# loader.loadTestsFromName("testonly.test.TestStringMethods.test_split").run(results)
	
	#loadTestsFromTestCase()向TestLoader实例中加载某个TestCase实例中的所有测试用例
	#并返回一个TestSuite实例
	# loader.loadTestsFromTestCase(TestStringMethods).run(results)
	
	#loadTestsFromModule()向TestLoader实例中加载某个模块(这里是testonly.test)中所有
	#继承自TestCase类的实例，并将其中的测试用例添加至TestLoader实例中
	#注意：
	#传递给loadTestsFromModule()方法的参数所指向的模块中，若实现了load_tests()，则只会
	#向TestLoader中加载load_tests()方法中指定的测试用例，而不是该模块中包含的所有测试用例。
	# loader.loadTestsFromModule(testonly.test).run(results)
	# print(results)
	# for a,b in results.errors:
	# 	print("---"*20,"\n",a,"\n",b)
	# results = unittest.TestResult()
	# test_suite = suite_for_TestResult()
	# test_suite.run(results)
	# print(results)
	# print("Run",results.testsRun,"tests in total\n")
	# print(results.errors)
	# print(results.failures)
	# print(results.skipped)
	# print(results.expectedFailures)
	

	test_runner = unittest.TextTestRunner().run(TestStringMethods())
	test_runner = unittest.TextTestRunner().run(suite())



