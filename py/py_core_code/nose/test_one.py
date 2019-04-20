import unittest

class Widget(object):
    def __init__(self, size = (40, 40)):
        self._size = size
    def getSize(self):
        return self._size
    def resize(self, width, height):
        if width < 0 or height < 0:
            raise ValueError  #, "illegal size"
        self._size = (width, height)
    def dispose(self):
        pass

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget()
    def tearDown(self):
        self.widget.dispose()
        self.widget = None
    def testSize(self):
        self.assertEqual(self.widget.getSize(), (40, 40))
    def testResize(self):
        self.widget.resize(100, 100)
        self.assertEqual(self.widget.getSize(), (100, 100))

#def runtest():
    # 添加测试集 (1)、(2)、(3)
    
    #(1) 测试集一个个添加测试用例
    #suite = unittest.TestSuite()
    #suite.addTest(WidgetTestCase("testSize"))
    #suite.addTest(WidgetTestCase("testResize"))
    
    #(2) 派生unittest.TestSuite的子类添加测试用例
    #tests = ['testSize', 'testResize']             
    #suite = unittest.TestSuite(map(WidgetTestCase, tests))
    
    #(3) 若测试方法都是以test开头，自己构造测试集
    #suite = unittest.makeSuite(WidgetTestCase, "test")

    # 执行测试
    #runner = unittest.TextTestRunner()
    #runner.run(suite)

    #	事实上，TestSuite除了可以包含TestCase外，也可以包含TestSuite，从而可以构成一个更加庞大的测试用例集：
    #	suite1 = mysuite1.TheTestSuite()
    #	suite2 = mysuite2.TheTestSuite()
    #	alltests = unittest.TestSuite((suite1, suite2))    
		
if __name__ == "__main__":
    #runtest()        	
    unittest.main(verbosity=2)   #推荐用这种，那么就不需要runtest()启用测试集，但是测试方法必须以test开头，自动检测测试方法




