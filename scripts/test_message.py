import os, sys
sys.path.append(os.getcwd())

from page.sendMessage_page import SendMessagePage
from base.base_driver import BaseDriver

class TestAddPerson:



    def setup(self):
        baseDriver = BaseDriver()
        driver = baseDriver.create_driver()
        self.sendMessage = SendMessagePage(driver)
        self.sendMessage.click_add_people()
        self.sendMessage.click_all_button()


    #发短信
    def test_send_mes(self):
        self.sendMessage.click_selected_button()
        self.sendMessage.input_text_button('hellodoyoudddddd')
        self.sendMessage.click_send_button()

    #打电话
    def test_call_person(self):
        self.sendMessage.click_img_button()
        self.sendMessage.click_phone_button()




