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

if __name__ == '__main__':

	#TestSuite类中的的run()方法：
	#不同于TestCase类，这里的run()方法需要一个TestResult对象作为参数来
	#记录测试结果，因此在使用TestSuite.run()之前，确保创建一个TestResult对象
	result = unittest.TestResult()
	suite = suite()   #创建一个TestSuite实例
	suite.run(result) 
	print("Ran count:",suite.countTestCases()) #获取TestSuite中的测试用例数量
	print("Skipped:",result.skipped)

	#debug()方法执行TestSuite对象中的所有测试用例，但测试结果不会保存，
	#且测试用例中的异常会传递到主调函数
	#!!! debug()执行完毕后会退出程序，后面的语句不会执行 !!!
	suite.debug() 
	print("Should not execute to here.")


'''
******************Points*****************************
TestSuite类
addTest()  addTests()  run()
debug()    countTestCases()
'''
	
	




