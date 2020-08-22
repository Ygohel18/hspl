import time
import json
from selenium import webdriver


class Hspl(object):
    def __init__(self):
        self.chrome_driver_path = "includes/chromedriver"
        self.browser_profile = webdriver.ChromeOptions()
        self.browser_profile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_IN'})
        self.browser_profile.add_argument('headless')
        self.browser_profile.add_argument('--no-sandbox')
        self.browser = webdriver.Chrome(self.chrome_driver_path, chrome_options=self.browser_profile)
        # Default wait time
        self.rest = 3

    def check(self, search_query, url):
        search_num = 20
        search = "https://google.co.in/search?q=" + search_query + "&num=" + str(search_num)
        self.browser.get(search)
        time.sleep(self.rest)

        url_list = []
        url_title_list = []
        data_ary = []

        get_list = self.browser.find_elements_by_css_selector('div.r>a')
        get_list_title = self.browser.find_elements_by_css_selector('div.r>a>h3')

        for i in get_list:
            url_list.append(i.get_attribute("host"))

        for t in get_list_title:
            url_title_list.append(t.get_attribute("textContent"))

        count = 0
        rank = 0
        for i in url_list:
            count = count + 1
            if i == url:
                rank = count

        c = 0

        data = {
            "your_rank": int(rank),
            "your_url": str(url),
            "your_keyword": str(search_query)
        }

        data_ary.append(data)

        for i in url_list:
            data = {
                "rank": int(c + 1),
                "link": (str(i)),
                "text": str(url_title_list[c])
            }

            data_ary.append(data)
            c = c + 1

        res = json.dumps(data_ary)

        return res

    # Close browser it self
    def close_browser(self):
        print('Session end')
        self.browser.quit()

    # Terminate process
    def __exit__(self, exc_type, exc_value, traceback):
        self.close_browser()
