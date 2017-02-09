# coding:utf-8

from time import sleep

def init_login(self, account, passwd):
    sleep(5)
    # 处理未登陆的情况
    try:
        self.driver.find_element_by_id('com.cloudpense:id/et_userName').send_keys(account)
        self.driver.find_element_by_id('com.cloudpense:id/et_passWord').send_keys(passwd)
        self.driver.find_element_by_id('com.cloudpense:id/btn_login').click()  # 点击登陆
        sleep(5)
    except:
        pass


def init_logout(self):
    # 处理已登录需要退出登录情况
    sleep(5)
    try:
        self.driver.find_element_by_id('com.cloudpense:id/btn_me').click()
        self.driver.find_element_by_id('com.cloudpense:id/settings_column').click()  # 点击设置
        self.driver.find_element_by_id('com.cloudpense:id/Cancellation_column').click()  # 点击注销
        self.driver.find_element_by_id('com.cloudpense:id/btn_ensure').click()  # 点击退出登录
        sleep(2)
    except:
        pass