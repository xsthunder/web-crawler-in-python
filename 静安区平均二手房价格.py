#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://sh.lianjia.com/ershoufang/jingan/")


ret = []
while(True):
    price_eles = driver.find_elements_by_class_name('totalPrice')
    for ele in price_eles:
        ret.append(ele.text)
    try:
        nxt = driver.find_element_by_link_text('下一页')
        nxt.click()
    except:
        breake
        # NoSuchElementException                    
        

driver.close()


nxt_ret = []
for x in ret:
    nxt_ret.append(float(x[:-1]))


print(sum(nxt_ret)/len(nxt_ret))

