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

if __name__ == '__main__':

	#TestCase类中的run()方法：
	#一个TestCase类中可以有一个或多个测试用例，每个测试用例就是一个方法(以test开头)
	#实例化一个TestCase类时，若构造函数的参数缺省，run()会默认调用runTest()方法，
	#若该方法未实现则会报错。
	result = TestStringMethods().run()
	print(result)
	
	#若TestCase中有多个测试用例，在构造参数中指定该测试用例的方法名后，run()会调用
	#该方法而不是默认的runTest()方法
	#注意：这里   不强制要求   方法名必须以test开头
	result = TestStringMethods("another_test_split").run()
	print("*",result)
	result = TestStringMethods("test_split").run()
	print("**",result)

	#unittest.main提供命令行接口，命令格式：
	#python test_code.py [-v] [test_case_name]
	#Examples: 
	#python test_code.py -v TestStringMethods.test_isupper  #单个用例
	#python test_code.py -v [testcase1,testcase2,testcase3] #多个用例
	#
	#若命令行参数中不指定测试用例的名称,main()方法执行被测模块(.py文件)中的
	#所有测试用例，这些测试用例可能包含中多个TestCase实例中,例如本文件中的
	#ForTestResult、TestStringMethods类中的共7个测试用例。
	#
	#测试结果：  .表示通过，s表示跳过，E表示出现错误（异常），F表示失败(Failure)
	#           x表示出现期望的异常
	#           
	#main()默认运行TestCase实例中的每个测试用例，实际是每次调用TestCase.run()方法
	#调用main()函数返回一个TestProgram实例，见main.py中 main = TestProgram
	#可选参数： verbosity = 0,1,2 数字越大，信息越详细，大于2时与2作用相同
	#
	#！！main()函数执行后，整个程序就会退出，若main()函数后还有语句，则不会被执行！！
	unittest.main() 
	print("Should not execute to here")

'''
******************Points*****************************
unittest
unittest.main()

TestCase类
setUp()    tearDown()  doCleanups()
run()      runTest()   subTest()
test_xxx() assertXXX()

装饰器
@unittest.skip   @unittest.skipIf  @unittest.skipUnless 
@unittest.expectedFailure  @unittest.skipTest
'''
	
	
	



