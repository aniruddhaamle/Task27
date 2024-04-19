import Data.Data
from Data import Data
from Locators import Locators
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from datetime import date
from datetime import datetime
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 30, poll_frequency=1)

    def boot(self):
        self.driver.get(Data.webData().url)
        self.driver.maximize_window()
        #self.wait.until(ec.url_to_be(Data.webData().url))
        self.wait.until(ec.presence_of_element_located((By.XPATH, Locators.WebLocators().userNameLocator)))

    def quit(self):
        self.driver.quit()

    def enterText(self, locator, textValue):
        element = self.driver.find_element(by=By.XPATH, value=locator)
        element.clear()
        element.send_keys(textValue)

    def clickButton(self, locator):
        self.driver.find_element(by=By.XPATH, value=locator).click()

    def login(self):
        try:
            self.boot()
            for row in range(2, Data.webData().rowcount() + 1):
                username = Data.webData().readData(row, 2)
                password = Data.webData().readData(row, 3)
                self.wait.until(ec.presence_of_element_located((By.XPATH, Locators.WebLocators().userNameLocator)))
                self.enterText(Locators.WebLocators().userNameLocator, username)
                self.enterText(Locators.WebLocators().passwordLocator, password)
                self.clickButton(Locators.WebLocators().loginButtonLocator)
                #self.wait.until(ec.url_to_be(Data.webData().dashboardUrl))

                if self.driver.current_url == Data.webData().dashboardUrl:
                    print("Successfully Loggedin")
                    Data.webData().writeData(row, 7, "PASSED")
                    currentDate = date.today()
                    Data.webData().writeData(row, 4, currentDate)
                    now = datetime.now()
                    currentTime = now.time()
                    Data.webData().writeData(row, 5, currentTime)
                    NameOfTester = os.getlogin()
                    Data.webData().writeData(row, 6, NameOfTester)

                    #self.clickButton(Locators.WebLocators().profileIconLocator)
                    self.wait.until(ec.presence_of_element_located((By.XPATH, Locators.WebLocators().profileIconLocator))).click()
                    #self.clickButton(Locators.WebLocators().logoutLocator)
                    self.wait.until(
                        ec.presence_of_element_located((By.XPATH, Locators.WebLocators().logoutLocator))).click()


                else:
                    print("Login unsuccessfull")
                    Data.webData().writeData(row, 7, "FAILED")
                    currentDate = date.today()
                    Data.webData().writeData(row, 4, currentDate)
                    now = datetime.now()
                    currentTime = now.time()
                    Data.webData().writeData(row, 5, currentTime)
                    NameOfTester = os.getlogin()
                    Data.webData().writeData(row, 6, NameOfTester)

        except NoSuchElementException as e:
            print(e)
        finally:
            self.quit()


obj = LoginPage()
obj.login()
