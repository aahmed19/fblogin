from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

class LoginTest:

    def __init__(self):
        return

    def setUp(self):
        binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
        self.driver = webdriver.Firefox(firefox_binary=binary)
        self.driver.get("http://www.facebook.com")

    def test_Login(self):
        driver = self.driver
        facebookUsername = "MY_USERNAME"
        facebookPassword = "MY_PASSWORD"
        emailFieldID = 'email'
        passwordFieldID = 'pass'
        loginButtonXpath = "//input[@value='Log In']"
        fbLogoXpath = "(//a[contains(@href, 'logo')])[1]"

        emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(emailFieldID))
        passFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passwordFieldID))
        loginButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(loginButtonXpath))

        emailFieldElement.clear()
        emailFieldElement.send_keys(facebookUsername)
        passFieldElement.clear()
        passFieldElement.send_keys(facebookPassword)
        loginButtonElement.click()

        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(fbLogoXpath))

    def tearDown(self):
        self.driver.quit()

fblogin = LoginTest()
fblogin.setUp()
fblogin.test_Login()
fblogin.tearDown()
