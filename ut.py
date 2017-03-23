# coding = utf-8
import os, time
import unittest
from selenium import webdriver

class TestTaoBao(unittest.TestCase):
    def setUp(self):
        print('test start')
        file_path = 'file:///' + os.path.abspath('demo.html')
        self.driver = webdriver.Chrome()
        self.driver.get(file_path)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
        print('test end')

    def test_all_select(self):
        allCheckBox = self.driver.find_element_by_id('allCheckBox')
        allCheckBox.click()
        cartCheckBoxs = self.driver.find_elements_by_name('cartCheckBox')
        for cartCheckBox in cartCheckBoxs:
            self.assertEqual(allCheckBox.get_attribute('checked'),
                cartCheckBox.get_attribute('checked'))


if __name__ == '__main__':
    unittest.main()
