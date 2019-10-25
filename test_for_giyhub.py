import unittest
from nose.tools import assert_equal, assert_true
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SampleTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.set_page_load_timeout(30)