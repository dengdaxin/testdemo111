import time
import os
import unittest
from selenium import webdriver
from common.read_conf_ini import ReadConf
from selenium.webdriver.common.by import By
from common import login
current = os.path.dirname(__file__)
config_path = os.path.join(current,'../conf/conf.ini')

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

    def tearDown(self):
        time.sleep(1)
        self.driver.quit()

    def test_login_pass(self):
        '''登录成功测试'''
        login.login(self.driver,self.username,self.password)
        username = self.driver.find_element(By.XPATH,'//span[@class="user-name"]').text
        self.assertEqual(username,self.username,'test_login_pass测试失败')

if __name__=='__main__':
    unittest.main()