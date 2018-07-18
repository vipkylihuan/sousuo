import unittest
from selenium import webdriver
import settings

class test_sousuo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(settings.url)

    def test_main(self):
        pass

    def tearDown(self):
        self.driver.quit()