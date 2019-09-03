#!/usr/bin/env python
# coding: utf-8

# 华理研究生抢体育课脚本
# dependency 
## selenium https://selenium-python.readthedocs.io/installation.html#introduction
## firefox selenium驱动
## firefox >= 68
## python >= 3.7

# TODO
# 检查是否体育课已选

# 附送windows cmd循环脚本
# :loop
# timeout 5
# python tiyu.py
# goto loop


# 选课系统账号密码
USERNAME=
PASSWORD=

# In[1]:


url = 'http://59.78.108.52/webui/' # 登陆页面获取session


# In[2]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get(url)


# In[3]:


username = driver.find_element_by_id('username')
username.send_keys(USERNAME)


# In[4]:


password = driver.find_element_by_id('password')
password.send_keys(PASSWORD)


# In[5]:


btnlogin = driver.find_element_by_id('btnlogin')
btnlogin.click()


# In[6]:


driver.get('http://59.78.108.52/webui/Student/SelectClass.aspx?kkbh=28403&kind=4317&dept=18&id=3&bx=0&xwk=0') # 体育学院-健康体育-选课页面


# In[7]:


links = driver.find_elements_by_link_text('选择')


# In[8]:


import random
link = random.choice(links) # 任意选择一门课，因为第一门课经常不能选


# In[9]:

try: # 确保浏览器能关闭
	link.click()
	driver.close()
except Exception:
	print('wrong click')
	driver.close()
