#!/usr/bin/env python3

import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

CHROMEDRIVER = "/usr/local/bin/chromedriver" #
CHROME_BINARY = "/Applications/Chromium.app/Contents/MacOS/Chromium" # /usr/bin/chromium

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.binary_location = CHROME_BINARY

driver = webdriver.Chrome(executable_path=os.path.abspath(CHROMEDRIVER),   chrome_options=chrome_options)
driver.set_page_load_timeout(60) # 60 seconds
time.sleep(1)

driver.get("http://howdy.tamu.edu")

print(driver.current_url)

title = driver.find_element_by_css_selector("#splash-cell-inner > p:nth-child(3) > i")
print(title.text)

driver.close()
