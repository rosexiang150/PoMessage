# 导包的快捷键 ctrl+alt+空格
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def click(self,loc):
        self.custom_find_element(loc).click()

    def input(self, loc, text):
        ele = self.custom_find_element(loc)
        ele.click()
        ele.send_keys(text)

    #自定义查找元素的方法
    def custom_find_element(self, loc, time=10, poll=1):
        return WebDriverWait(self.driver, time, poll).until(lambda x:x.find_element(loc[0], loc[1]))


   #通过元素的id和元素的下标，查找并返回该元素,在脚本中需要对元素再操作
    def custom_find_ele_ById_And_index(self, loc, eleIndex):
        list = self.driver.find_elements(By.ID,loc[1])
        return list[eleIndex]

    # 通过元素的id和元素的内容，查找并返回一个元素
    def custom_find_ele_ById_And_content(self, loc, content):
        list = self.driver.find_elements(By.ID,loc[1])
        for i in list:
            if i.get_attribute('text') == content:
                return i