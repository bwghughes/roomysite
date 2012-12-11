from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class DevicesAdminFunctionalTest(LiveServerTestCase):

    fixtures = ['admin_user.json', 'admin_devices.json']

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)
        self._login()

    def tearDown(self):
        self.browser.quit()

    def _login(self):
        self.browser.get(self.live_server_url + '/admin/')
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('ben')
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('icbiatwt2')
        password_field.send_keys(Keys.RETURN)


    def test_we_can_add_a_device(self):
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
        version_field = self.browser.find_element_by_name('software_version')
        version_field.send_keys('0.1')

        # Save Device
        save_button = self.browser.find_element_by_css_selector("input[value='Save']")
        save_button.click()

        # Check successful save
        saved_message = self.browser.find_element_by_css_selector("li[class='info']")
        self.assertIn("was added successfully.", saved_message.text)

    def test_we_can_add_a_space(self):
        self.browser.get(self.live_server_url + '/admin/')
        self._login()
        spaces_links = self.browser.find_elements_by_link_text('Spaces')

        # First link is a breadcrumb link
        spaces_links[1].click()
        new_space_link = self.browser.find_element_by_link_text('Add space')
        new_space_link.click()
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Name:', body.text)
        self.assertIn('Area:', body.text)
        self.assertIn('Device:', body.text)

        # Add Space
        name_field = self.browser.find_element_by_name('name')
        name_field.send_keys("Room G01")
        area_field = self.browser.find_element_by_name('area')
        date_field.send_keys('21.25')


        # Save Space
        save_button = self.browser.find_element_by_css_selector("input[value='Save']")
        save_button.click()

        # Check successful save message
        saved_message = self.browser.find_element_by_css_selector("li[class='info']")
        self.assertIn("was added successfully.", saved_message.text)


