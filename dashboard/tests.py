from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class DeviceAdminTest(LiveServerTestCase):

    fixtures = ['admin_user.json']

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def _login(self):
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('ben')
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('icbiatwt2')
        password_field.send_keys(Keys.RETURN)


    def test_can_access_admin_site(self):
        # Gertrude opens her web browser, and goes to the admin page
        self.browser.get(self.live_server_url + '/admin/')
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)
        self._login()
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Site administration', body.text)

    def test_we_can_add_a_device(self):
        self.browser.get(self.live_server_url + '/admin/')
        self._login()
        devices_links = self.browser.find_elements_by_link_text('Devices')

        # First link is a breadcrumb link
        devices_links[1].click()
        new_device_link = self.browser.find_element_by_link_text('Add device')
        new_device_link.click()
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Name:', body.text)
        self.assertIn('Registered at:', body.text)

        # Add Device
        name_field = self.browser.find_element_by_name('name')
        name_field.send_keys("Room G01")
        date_field = self.browser.find_element_by_name('registered_at_0')
        date_field.send_keys('01/01/12')
        time_field = self.browser.find_element_by_name('registered_at_1')
        time_field.send_keys('00:00')

        # Save Device
        save_button = self.browser.find_element_by_css_selector("input[value='Save']")
        save_button.click()