#coding:utf-8

#必须导入的内容
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


class ExpenseLogin(unittest.TestCase):
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
    1、打开简单报销，假如已经登录就注销
    2、进入用户登录界面
    3、点击忘记密码
    4、什么都不做，返回到用户登陆界面
    5、什么都不输入，点击登陆
    6、输入任意账号，点击登陆
    7、输入任意账号，和任意密码，点击登陆
    8、输入正确账号和错误密码，点击登陆
    9、输入正确账号和正确密码点击登陆，进入到首页
    10、退出登陆，回到首页'''

    def test_Mobilelogin(self):
        print 'start login test ...  '
        InitLogin.init_logout(self)
        try:
            userName = self.driver.find_element_by_id('com.cloudpense:id/et_userName')
            passWd = self.driver.find_element_by_id('com.cloudpense:id/et_passWord')
            loginBtn = self.driver.find_element_by_id('com.cloudpense:id/btn_login')

            self.driver.find_element_by_id('com.cloudpense:id/btn_forget_password').click()#忘记密码
            self.driver.find_element_by_id('com.cloudpense:id/btn_back').click()

            userName.send_keys('')
            loginBtn.click()
            ensureBtn = self.driver.find_element_by_id('com.cloudpense:id/btn_ensure')
            ensureBtn.click()
            
            userName.send_keys('1111@qq.com')
            loginBtn.click()
            ensureBtn.click()

            userName.send_keys('1111@qq.com')
            passWd.send_keys('1111')
            loginBtn.click()
            ensureBtn.click()

            userName.send_keys('xiangyu@qq.com')
            passWd.send_keys('1111')
            loginBtn.click()
            ensureBtn.click()

            userName.send_keys('xiangyu@qq.com')
            passWd.send_keys('admin')
            loginBtn.click()
        except Exception, e:
            print traceback.format_exc()
            #内部获取类名sys._getframe().f_code.co_name
            ScreenShot.screenShot(self, sys._getframe().f_code.co_name)


def suite(self):
    suite = unittest.TestSuite()
    suite.addTest(ExpenseLogin('test_Mobilelogin'))

    runner = unittest.TextTestRunner()
    runner.run(suite)
