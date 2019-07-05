
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

driver = webdriver.Firefox()
driver.get("https://sh.lianjia.com/ershoufang/jingan/")


ret = []
while(True):
    price_eles = driver.find_elements_by_class_name('houseInfo')
    for ele in price_eles:
        res = re.search('([\d\.]+)平米', ele.text)
        if res is not None:
             ret.append(res[1])
    try:
        nxt = driver.find_element_by_link_text('下一页')
        nxt.click()
    except:
        break
        # NoSuchElementException                    
        

driver.close()


nxt_ret = []
for x in ret:
    nxt_ret.append(float(x))


print(sum(nxt_ret)/len(nxt_ret))
