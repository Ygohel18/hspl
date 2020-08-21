import time
from datetime import datetime
from selenium import webdriver

class Hspl(object):
    def __init__(self):
        self.chrome_driver_path = "includes/chromedriver"
        self.browser_profile = webdriver.ChromeOptions()
        self.browser_profile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_IN'})
        self.browser = webdriver.Chrome(self.chrome_driver_path, chrome_options=self.browser_profile)
        self.url = "hostingspell.com"
        # Default wait time
        self.rest = 3

    def check(self):
        self.browser.get('https://google.co.in/search?q=cheap+web+hosting+in+india&num=20')
        time.sleep(self.rest)

        # CITE Element
        url_list = []

        get_list = self.browser.find_elements_by_css_selector('div.r>a')

        for i in get_list:
            url_list.append(i.get_attribute("host"))

        count = 0
        for i in url_list:
            count = count + 1
            if i == self.url:
                return count

    def save_log(self):
        count = self.check()
        ctime = datetime.now()
        stime = ctime.strftime("%d-%b-%Y (%H:%M:%S.%f)")

        add = stime + " : " + str(count)

        with open("hspltrack.txt", "a") as f:
            f.write(add)

    # Close browser it self
    def close_browser(self):
        print('Session end')
        self.browser.quit()

    # Terminate process
    def __exit__(self, exc_type, exc_value, traceback):
        self.close_browser()
