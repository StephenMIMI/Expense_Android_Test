#coding:utf-8

import unittest
import sys
import os

curDir = sys.path[0]

#windows下的写法
sys.path.append(curDir + '\\TestCases\\login')
#mac下的写法
sys.path.append(curDir + '/TestCases/login')


import ExpenseLogin



ExpenseLogin.suite(0)