import os, sys
sys.path.append(os.getcwd())

from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class SendMessagePage(BaseAction):

    add_people_button = By.ID, 'com.android.messaging:id/start_new_conversation_button'
    all_button = By.XPATH, '//*[@text="所有联系人"]'
    selected_button = By.ID, 'com.android.messaging:id/contact_name'
    text_button = By.ID, 'com.android.messaging:id/compose_message_text'
    send_mes_button = By.ID, 'com.android.messaging:id/self_send_icon'



    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    def click_add_people(self):
        self.click(self.add_people_button)

    def click_all_button(self):
        self.click(self.all_button)

    def click_selected_button(self):
        #self.click(self.selected_button)
        ele = self.custom_find_ele_ById_And_index(self.selected_button,1)
        ele.click()

    def input_text_button(self, text):
        self.input(self.text_button, text)

    def click_send_button(self):
        self.click(self.send_mes_button)

