import time
import os
import unittest
from selenium import webdriver
from common.read_conf_ini import ReadConf
from selenium.webdriver.common.by import By
from common import login
current = os.path.dirname(__file__)
config_path = os.path.join(current,'../../conf/conf.ini')
report_path = os.path.join(current,'../report')
class LoginCase(unittest.TestCase):
    def setUp(self):
        conf = ReadConf(config_path)
        self.url = conf.read_conf_url()
        self.username = conf.read_conf_username()
        self.password = conf.read_conf_password()
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.url)
        login.login(self.driver,self.username,self.password)
        # self.driver.find_element(By.XPATH, '//input[@id="account"]').send_keys(self.username)
        # self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(self.password)
        # self.driver.find_element(By.XPATH, '//button[@id="submit"]').click()

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    def test_create_bug(self):
        '''新增bug测试'''
        time.sleep(1)
        self.driver.find_element(By.XPATH,'//li[@data-id="qa"]').click()
        self.driver.find_element(By.XPATH, '//li[@data-id="bug"]').click()
        self.driver.find_element(By.XPATH, '//a[@href="/zentao/bug-create-1-0-moduleID=0.html"]').click()
        self.driver.find_element(By.XPATH,'//div[@id="module_chosen"]').click()
        self.driver.find_element(By.XPATH,'//li[@title="/测试1"]').click()
        self.driver.find_element(By.XPATH, '//div[@id="project_chosen"]').click()
        self.driver.find_element(By.XPATH, '//li[@title="学生管理迭代1.1"]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//div[@id="openedBuild_chosen"]').click()
        self.driver.find_element(By.XPATH, '//li[@title="主干"]').click()
        self.driver.find_element(By.XPATH, '//div[@id="assignedTo_chosen"]').click()
        self.driver.find_element(By.XPATH, '//li[@title="A:admin"]').click()
        self.driver.find_element(By.XPATH, '//input[@id="deadline"]').send_keys('2021-06-30')
        self.driver.find_element(By.XPATH, '//div[@id="type_chosen"]').click()
        self.driver.find_element(By.XPATH, '//li[@title="配置相关"]').click()
        self.driver.find_element(By.XPATH, '//div[@id="os_chosen"]').click()
        self.driver.find_element(By.XPATH, '//li[@title="Windows 8"]').click()
        self.driver.find_element(By.XPATH, '//div[@id="browser_chosen"]').click()
        self.driver.find_element(By.XPATH, '//li[@title="IE11"]').click()
        self.driver.find_element(By.XPATH, '//input[@id="title"]').send_keys('密码规则不符合')
        time.sleep(1)
        #self.driver.find_element(By.XPATH,'//*[@id="submit"]').click()
if __name__=='__main__':
    unittest.main()