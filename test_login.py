'''
登录测试，分下面几种情况：
(1)用户名、密码正确
(2)用户名正确、密码不正确
(3)用户名正确、密码为空
(4)用户名错误、密码正确
(5)用户名为空、密码正确（还有用户名和密码均为空时与此情况是一样的，这里就不单独测试了）
'''
import unittest
from selenium import webdriver
from time import sleep
import settings
from bs4 import BeautifulSoup

class LoginCase(unittest.TestCase):

# @classmethod
# def setUpClass(cls):  # 这里的cls是当前类的对象
#     pass
# @classmethod
# def tearDownClass(cls):
#     cls._connection.destroy()
#     print("自动化测试执行完毕")

    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()


    # 定义登录方法
    def login(self, username, password):

        self.dr.get(settings.login_url)  # 登录页面
        self.dr.find_element_by_id('txtUserName').send_keys(username)
        self.dr.find_element_by_id('txtUserPwd').send_keys(password)
        self.dr.find_element_by_id('btnLogin').click()

    def test_login_success(self):
        '''用户名、密码正确'''
        self.login('18510808081', 'qq769963636')  # 正确用户名和密码
        sleep(2)

        # self.soup = BeautifulSoup(settings.login_url)
        try:
            assert '控制台 | CDS' in self.dr.title
            print('TEST login success PASS.')
        except Exception as e:
            print('test fail',format(e))
        self.dr.get_screenshot_as_file("E:\logtest\\login_success.png")  # 截图  可自定义截图后的保存位置和图片命名

    def test_login_pwd_error(self):
        '''用户名正确、密码不正确'''
        self.login('18510808081', 'qq7699636361')  # 正确用户名，错误密码
        sleep(2)
        error_message = self.dr.find_element_by_xpath("//span[@class='mage_error']").text
        try:
            self.assertIn('错误', error_message)  # 用assertIn(a,b)方法来断言 a in b  '用户名或密码错误'在error_message里
            print("TEST login pwd error PASS")
        except Exception as e:
            print('test fail',format(e))
        self.dr.get_screenshot_as_file("E:\logtest\\login_pwd_error.png")

    def test_login_pwd_null(self):
        '''用户名正确、密码为空'''
        self.login('18510808081', '')
        sleep(2)# 密码为空
        try:
            error_message = self.dr.find_element_by_xpath("//span[@class='mage_error']").text
            self.assertEqual(error_message, '密码不能为空!')  # 用assertEqual(a,b)方法来断言  a == b  ’密码不能为空!‘等于error_message
            print('TEST login pwd null pass')
        except Exception as e:
            print('test fail',format(e))
        self.dr.get_screenshot_as_file("E:\logtest\\login_pwd_null.png")

    def test_login_user_error(self):
        '''用户名错误、密码正确'''
        self.login('185108080813', 'qq769963636')  # 密码正确，用户名错误
        sleep(2)
        try:
            error_message = self.dr.find_element_by_xpath("//span[@class='mage_error']").text
            self.assertIn('用户名不存在', error_message)  # 用assertIn(a,b)方法来断言 a in b
            print('TEST login user error pass')
        except Exception as e:
            print('test fail',format(e))
        self.dr.get_screenshot_as_file("E:\logtest\\login_user_error.png")

    def test_login_user_null(self):
        '''用户名为空、密码正确'''
        self.login('', 'qq769963636')  # 用户名为空，密码正确
        sleep(2)
        try:
            error_message = self.dr.find_element_by_xpath("//span[@class='mage_error']").text
            self.assertEqual(error_message, '用户名不能为空!')  # 用assertEqual(a,b)方法来断言  a == b
            print("TEST longin user null pass")
        except Exception as e:
            print('test fail',format(e))
        self.dr.get_screenshot_as_file("E:\logtest\\login_user_null.png")

    def tearDown(self):
        self.dr.quit()


if __name__ == '__main__':
    unittest.main()