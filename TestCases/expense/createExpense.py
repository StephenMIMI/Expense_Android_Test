# coding:utf-8

# 必须导入的内容
import sys

curDir = sys.path[0]
print curDir
sys.path.append(curDir + '\\TestCases\\common')
sys.path.append(curDir + '/TestCases/common')
import Initialize
import ScreenShot
import InitLogin
import traceback

import unittest


class createExpense(unittest.TestCase):
    def __init__(self, methodName):
        unittest.TestCase.__init__(self, methodName)
        print '************************** login test **************************'

    # 初始化操作
    def setUp(self):
        Initialize.setUp(self)

    # 测试用例执行完成后的操作
    def tearDown(self):
        Initialize.tearDown(self)

    '''用户登陆：
    1、打开简单报销，假如还未登录就登录
    2、进入费用管理界面
    3、点击添加费用
    '''

    def test_createExpense(self):
        print 'start create expense test ...  '
        InitLogin.init_login(self,'xiangyu@qq.com','admin')
        try:

            self.driver.find_element_by_id('com.cloudpense:id/btn_expense').click()  #费用管理
            self.driver.find_element_by_id('com.cloudpense:id/exp_add').click()#添加费用


        except Exception, e:
            print traceback.format_exc()
            # 内部获取类名sys._getframe().f_code.co_name
            ScreenShot.screenShot(self, sys._getframe().f_code.co_name)


def suite(self):
    suite = unittest.TestSuite()
    suite.addTest(createExpense('test_createExpense'))

    runner = unittest.TextTestRunner()
    runner.run(suite)
