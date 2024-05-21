import time

from selenium.webdriver.common.by import By
from selenium import webdriver


class TestLink:

    def test_chrome(self):
        selenium_endpoint = "http://imranbookhive:Jt6VAQUpOLwMMu47LhfIeZ4ihF2KkyRfbrW60cSxSKGwk8Tjl5@hub.lambdatest.com/wd/hub"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        option = {
            "single_test": {
                "browserName": "Chrome",
                "browserVersion": "114.0",
                "LT:Options": {
                    "username": "imranbookhive",
                    "accessKey": "Jt6VAQUpOLwMMu47LhfIeZ4ihF2KkyRfbrW60cSxSKGwk8Tjl5",
                    "platformName": "Windows 10",
                    "project": "Chrome",
                    "w3c": True,
                    "plugin": "python-pytest"
                }
            }
        }
        chrome_options.set_capability("LT:Options", option)
        driver = webdriver.Remote(
            command_executor=selenium_endpoint,
            options=chrome_options
        )

        self.task(driver)

    def test_firefox(self):
        selenium_endpoint = "http://imranbookhive:Jt6VAQUpOLwMMu47LhfIeZ4ihF2KkyRfbrW60cSxSKGwk8Tjl5@hub.lambdatest.com/wd/hub"
        firefox_option = webdriver.FirefoxOptions()
        firefox_option.add_argument('--disable-blink-features=AutomationControlled')
        configure_option = {
            "single_test": {
                "browserName": "Firefox",
                "browserVersion": "114.0",
                "LT:Options": {
                    "username": "imranbookhive",
                    "accessKey": "Jt6VAQUpOLwMMu47LhfIeZ4ihF2KkyRfbrW60cSxSKGwk8Tjl5",
                    "platformName": "Windows 10",
                    "project": "Firefox",
                    "w3c": True,
                    "plugin": "python-pytest"
                }
            }
        }
        firefox_option.set_capability("LT:Options", configure_option)
        driver = webdriver.Remote(
            command_executor=selenium_endpoint,
            options=firefox_option
        )

        self.task(driver)

    def test_safari(self):
        selenium_endpoint = "http://imranbookhive:Jt6VAQUpOLwMMu47LhfIeZ4ihF2KkyRfbrW60cSxSKGwk8Tjl5@hub.lambdatest.com/wd/hub"
        safari_option = webdriver.SafariOptions()
        safari_option.add_argument('--disable-blink-features=AutomationControlled')
        configure_option = {
            "single_test": {
                "browserName": "Safari",
                "browserVersion": "16.0",
                "LT:Options": {
                    "username": "imranbookhive",
                    "accessKey": "Jt6VAQUpOLwMMu47LhfIeZ4ihF2KkyRfbrW60cSxSKGwk8Tjl5",
                    "platformName": "MacOS Ventura",
                    "project": "Safari",
                    "w3c": True,
                    "plugin": "python-pytest"
                }
            }
        }
        safari_option.set_capability("LT:Options", configure_option)
        driver = webdriver.Remote(
            command_executor=selenium_endpoint,
            options=safari_option)

        self.task(driver)

    def task(self, driver):
        driver.get("https://dev.bookhive.me/login")
        assert "Bookhive - Online Reading Platform" in driver.title
        print("Successfully open the Bookhive - Online Reading Platform website")
        time.sleep(10)
        google_sign_in_account = driver.find_element(By.XPATH,
                                                     "//iframe[contains(@title,'Sign in with Google Button')]")
        google_sign_in_account.click()

        window_before = driver.window_handles[0]
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        time.sleep(10)

        # Sign in with the Google account
        username_input = driver.find_element(By.XPATH, "//input[contains(@type,'email')]")
        username_input.send_keys("qaengineer553@gmail.com")
        next_button = driver.find_element(By.XPATH, "//span[contains(text(),'Next')]")
        next_button.click()
        time.sleep(10)
        password_input = driver.find_element(By.XPATH, "//input[contains(@type,'password')]")
        password_input.send_keys("qatest@1234")
        next_button = driver.find_element(By.XPATH, "//span[contains(text(),'Next')]")
        next_button.click()
        print("Authentication of the Gmail account has been successful")

        driver.switch_to.window(window_before)
        time.sleep(10)
        create_button = driver.find_element(By.XPATH, "//div[@id='app']//span[text()=' Create reading ']")
        create_button.click()
        time.sleep(10)

        # Search for the book
        driver.find_element(By.XPATH, "(//div[@id='app']//input)[2]").send_keys("0143126563")
        time.sleep(10)
        search_book = driver.find_element(By.XPATH, "//div[contains(@class,'v-list-item')]//span[text()='0143126563']")
        search_book.click()
        time.sleep(5)
        driver.quit()
