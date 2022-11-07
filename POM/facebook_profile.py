import re
import time

from library.exel_lib import ReadExcel
from library.config import Config


class Facebookprofile:
    read_xl = ReadExcel()
    Profile_locators = read_xl.read_locators(Config.PROFILE_LOCATOR_SHEET)

    def __init__(self, driver):
        self.driver = driver



    def user_name(self, username):
        if isinstance(username, float):
            username = int(username)
        locator = self.Profile_locators["enter_username"]
        self.driver.find_element(*locator).send_keys(username)

    def pass_word(self, pwd):
        locator = self.Profile_locators["enter_password"]
        self.driver.find_element(*locator).send_keys(pwd)

    def login(self):
        locator = self.Profile_locators["login"]
        self.driver.find_element(*locator).click()

    def profile_icon(self):
        locator = self.Profile_locators["profile_icon"]
        self.driver.find_element(*locator).click()
        time.sleep(7)

    def Add_to_Story(self):
        locator = self.Profile_locators["Add_to_Story"]
        self.driver.find_element(*locator).click()

    def create_text_story(self):
        locator = self.Profile_locators["create_text_story"]
        self.driver.find_element(*locator).click()
        time.sleep(7)

    def start_typing(self, status):
        locator = self.Profile_locators["start_typing"]
        self.driver.find_element(*locator).send_keys(status)
        time.sleep(3)

    def discard(self):
        locator = self.Profile_locators["discard"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def confirm_discard(self):
        locator = self.Profile_locators["confirm_discard"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def back_button(self):
        locator = self.Profile_locators["back_button"]
        self.driver.find_element(*locator).click()

    def edit_profile(self):
        locator = self.Profile_locators["edit_profile"]
        self.driver.find_element(*locator).click()


    def add_bio(self):
        locator = self.Profile_locators["add_bio"]
        self.driver.find_element(*locator).click()
        time.sleep(3)


    def discribe(self, note):
        locator = self.Profile_locators["discribe"]
        self.driver.find_element(*locator).send_keys(note)
        time.sleep(3)

    def save(self):
        locator = self.Profile_locators["save"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def back_to_profile(self):
        locator = self.Profile_locators["back_to_profile"]
        self.driver.find_element(*locator).click()
        time.sleep(7)

    def about(self):
        locator = self.Profile_locators["about"]
        self.driver.find_element(*locator).click()
        time.sleep(7)

    def contact_and_basic(self):
        locator = self.Profile_locators["contact_and_basic"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def address(self):
        locator = self.Profile_locators["address"]
        self.driver.find_element(*locator).click()
        time.sleep(3)

    def add_address(self, home):
        locator = self.Profile_locators["add_address"]
        self.driver.find_element(*locator).send_keys(home)
        time.sleep(3)


    def save_address(self):
        locator = self.Profile_locators["save_address"]
        self.driver.find_element(*locator).click()
        time.sleep(3)