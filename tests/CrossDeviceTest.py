import time

from selenium.webdriver.common.by import By
from appium import webdriver


class TestLink:

    def test_android(self):
        caps = {
            "lt:options": {
                "w3c": True,
                "platformName": "android",
                "deviceName": "ASUS ZenFone 8",
                "platformVersion": "13",
                "visual": True,
                "network": True,
                "video": True,
                "console": True
            }
        }
        url = "https://imranbookhive:Jt6VAQUpOLwMMu47LhfIeZ4ihF2KkyRfbrW60cSxSKGwk8Tjl5@hub.lambdatest.com/wd/hub"
        driver = webdriver.Remote(desired_capabilities=caps, command_executor=url)
        self.task(driver)

    def test_ios(self):
        caps = {
            "lt:options": {
                "w3c": True,
                "platformName": "ios",
                "deviceName": "iPhone 14 Pro Max",
                "platformVersion": "16.0",
                "visual": True,
                "network": True,
                "video": True,
                "console": True
            }
        }
        url = "https://imranbookhive:Jt6VAQUpOLwMMu47LhfIeZ4ihF2KkyRfbrW60cSxSKGwk8Tjl5@hub.lambdatest.com/wd/hub"
        driver = webdriver.Remote(desired_capabilities=caps, command_executor=url)
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
