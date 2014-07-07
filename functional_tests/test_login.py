from selenium.webdriver.support.ui import WebDriverWait
from .base import FunctionalTest
import time

class LoginTest(FunctionalTest):

    def test_login_with_persona(self):
        #Arlo goes to the awesome treemap site and notices a "Sign in" link for the first time.
        self.browser.get(self.server_url + "/treemap")
        self.browser.find_element_by_id('id_login').click()

        # A Persona Login box appears
        self.switch_to_new_window('Mozilla Persona')

        # Edith logs in with her email address
        # Use mockmyid.com for test email
        self.browser.find_element_by_id(
            'authentication_email'
        ).send_keys('arlo@mockmyid.com')
        self.browser.find_element_by_tag_name('button').click()

        #The Persona window closes
        self.switch_to_new_window('Toronto Tree Map')

        #He can see that he is logged in
        self.wait_for_element_with_id('id_logout')
        navbar = self.browser.find_element_by_css_selector('.navbar-nav')
        self.assertIn('arlo@mockmyid.com', navbar.text)

    def switch_to_new_window(self, text_in_title):
        retries = 60
        while retries >0:
            for handle in self.browser.window_handles:
                self.browser.switch_to_window(handle)
                if text_in_title in self.browser.title:
                    return
            retries -= 1
            time.sleep(0.5)
        self.fail('could not find window')

    def wait_for_element_with_id(self, element_id):
        WebDriverWait(self.browser, timeout=3).until(
            lambda b: b.find_element_by_id(element_id)
            )