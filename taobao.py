# -*- coding:utf8 -*-

import os, time

def test_all_select(driver):
    allCheckBox = driver.find_element_by_id('allCheckBox')
    allCheckBox.click()
    cartCheckBoxs = driver.find_elements_by_name('cartCheckBox')
    k = 0
    for i, cartCheckBox in enumerate(cartCheckBoxs):
        if cartCheckBox.get_attribute('checked') == allCheckBox.get_attribute('checked'):
            print str(i) + '' + 'is ok!'
        else:
            k = 1
            print str(i) + '' + 'is a bug!'
    try:
        k == 0
    except Error as e:
        print 'except:', e
    else:
        print 'test_all_select is ok!'


def delete_single(driver):
    n = len(driver.find_elements_by_class_name('shopInfo'))
    driver.find_element_by_class_name('cart_td_8').click()
    ns = len(driver.find_elements_by_class_name('shopInfo'))
    if n == ns + 1:
        print 'ok'
    else:
        raise NameError('lose')
        

def delete_select(driver):
    n = len(driver.find_elements_by_class_name('shopInfo'))
    driver.find_element_by_class_name('cart_td_1').click()
    time.sleep(5)
    driver.find_element_by_class_name('delete').click()
    ns = len(driver.find_elements_by_class_name('shopInfo'))
    if n == ns + 1:
        print 'ok'
    else:
        raise NameError('lose')


def change_num(driver):
    tds = driver.find_elements_by_class_name('cart_td_6') 
    for i, td in enumerate(tds):
        value = int(td.find_element_by_tag_name('input').get_attribute('value'))
        if value == 1:
            td.find_element_by_name('m').click()
            try:
                alert = driver.switch_to_alert()
                alert.accept()
            except Error as e:
                print 'except:', e
        else:
            td.find_element_by_name('m').click()
            value_new = int(td.find_element_by_tag_name('input').get_attribute('value'))
            if value_new == value - 1:print str(i) + '' + 'm is ok'
            else:print str(i) + '' + 'm is a bug'
        value_1 = int(td.find_element_by_tag_name('input').get_attribute('value'))
        td.find_element_by_name('a').click()
        value_new_1 = int(td.find_element_by_tag_name('input').get_attribute('value'))
        if value_new_1 == value_1 + 1:
            print str(i) + '' + 'a is ok'
        else:
            print str(i) + '' + 'a is a bug'


def test_main():
    from selenium import webdriver
    driver = webdriver.Chrome()
    file_path = 'file:///' + os.path.abspath('demo.html')
    driver.get(file_path)
    driver.maximize_window()
    test_all_select(driver)
    change_num(driver)
    delete_single(driver)
    delete_select(driver)


if __name__ == '__main__':
    test_main()
