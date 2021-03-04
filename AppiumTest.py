import unittest
from appium import webdriver
from time import sleep

class AppiumTest(unittest.TestCase):
    dc = {}
    driver = None

    def setUp(self):

        self.dc['platformName'] = 'Android'
        self.dc['deviceName'] = 'DeviceR'
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.dc)

    def testFirstAutomation(self):
        self.driver.find_element_by_xpath("//*[@text='Play Store']").click()
        sleep(7)
        self.driver.find_element_by_xpath("//*[@text='Search for apps & games']").click()
        self.driver.find_element_by_xpath("//*[@text='Search for apps & games']").send_keys("astra")
        self.driver.press_keycode(66)
        self.driver.find_element_by_xpath('//android.view.View[contains(@content-desc,"Astra - Travel Social Network")]').click()
        self.driver.find_element_by_xpath("//*[@text='Install']").click()
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()