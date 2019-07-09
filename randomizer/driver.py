from selenium import webdriver

LOG_PATH = '/Users/noahvito'
LOGIN_URL = 'https://{}.slack.com/signin'
GIPHY_URL = 'https://{}.slack.com/services/417362304373'


class giphy_war_machine(object):
    def __init__(self, workspace='staydomio', email='noah.vito@staydomio.com', password=None):
        self.driver = self.init_webdriver()
        self.workspace = workspace
        self.email = email
        self.password = password
        self.login_url = LOGIN_URL.format(workspace)
        self.giphy_url = GIPHY_URL.format(workspace)

    def init_webdriver(self):
        options = webdriver.firefox.options.Options()
        # options.add_argument('--headless')
        # Did not work with headless on the server.
        # Instead I used pyvirtualdisplay and removed this option
        return webdriver.Firefox(
            firefox_options=options
            #log_path='{}/geckodriver.log'.format(LOG_PATH)
        )

    def run(self):
        self.login()
        self.disable_giphy_previews()
        self.driver.quit()
        print 'DONE!'

    def login(self):
        print 'logging in...'
        self.driver.get(self.login_url)
        email_field = self.driver.find_element_by_id('email')
        email_field.send_keys(self.email)
        password_field = self.driver.find_element_by_id('password')
        password_field.send_keys(self.password)

        continue_button = self.driver.find_element_by_id('signin_btn')
        continue_button.click()

    def disable_giphy_previews(self):
        print 'checking if previews are disabled...'
        self.driver.get(self.giphy_url)
        previews_checkbox = self.driver.find_element_by_name('previews_enabled')
        save_button = self.driver.find_element_by_id('add_integration')
        if previews_checkbox.is_selected():
            previews_checkbox.click()
            print 'previews are now disabled!'
        else:
            print 'previews already disabled!'
        save_button.click()
