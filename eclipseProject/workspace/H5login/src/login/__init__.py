# -*- coding: UTF-8 -*-
from selenium import webdriver
driver = webdriver.Chrome()
driver.get(r'http://www.126.com/')
ele = driver.find_element_by_xpath
ele('//*[@id="auto-id-1533179611133"]').send_keys('123')