from appium import webdriver

class BaseDriver:

    def create_driver(self):
        desired_caps = {}
        # 设备信息
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        # app的信息 com.android.contacts
        desired_caps['appPackage'] = 'com.android.messaging'
        desired_caps['appActivity'] = '.ui.conversationlist.ConversationListActivity'
        # 解决输入中文
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        # 声明我们的driver对象
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        return driver
