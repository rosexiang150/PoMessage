import os, sys
sys.path.append(os.getcwd())

import allure
import pytest



from page.sendMessage_page import SendMessagePage
from base.base_driver import BaseDriver
from base.base_yml import yml_data_with_file

class TestAddPerson:

    def setup(self):
        baseDriver = BaseDriver()
        driver = baseDriver.create_driver()
        self.sendMessage = SendMessagePage(driver)
        self.sendMessage.click_add_people()
        self.sendMessage.click_all_button()

    #打电话 allure的pytest
    # @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @pytest.mark.skipif(condition=2 > 1, reason="跳过该函数")
    @allure.step('我是测试步骤001')
    def test_call_person(self):
        self.sendMessage.click_img_button()
        self.sendMessage.click_phone_button()

    # 发短信---pytest
    # @pytest.mark.run(order=2)
    # @pytest.mark.xfail(2 > 1, reason="标注为预期失败")
    # @pytest.mark.parametrize('contents', ['aa', 'bb', 'cc', 'dd'])
    @pytest.mark.parametrize('text', yml_data_with_file()['search_data'])
    def test_send_mes(self):
        self.sendMessage.click_selected_button()
        self.sendMessage.input_text_button('text')
        self.sendMessage.click_send_button()
