# coding:utf-8

from appium import webdriver
# 测试用例的初始化操作

def setUp(self):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.4'
    desired_caps['deviceName'] = 'Android Emulator'
    desired_caps['appPackage'] = 'com.cloudpense'
    desired_caps['appActivity'] = 'com.cloudpense.activity.LoginActivity'
    self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


def tearDown(self):
    self.driver.quit()
    print 'end'
