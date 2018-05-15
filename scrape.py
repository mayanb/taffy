
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import csv
from urls import url_list

# url = 'https://sse18.mapyourshow.com/7_0/alphalist.cfm?endrow=799&alpha=*'
# urls = ["https://sse18.mapyourshow.com/7_0/exhibitor/exhibitor-details.cfm?ExhID=37201", 
# "https://sse18.mapyourshow.com/7_0/exhibitor/exhibitor-details.cfm?ExhID=125766"]
urls = url_list
option = webdriver.ChromeOptions()
option.add_argument(" - incognito")
browser = webdriver.Chrome(executable_path='../../../Downloads/chromedriver', chrome_options=option)
timeout = 20
# browser.get(url)
# try:
#     WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, "mys-table-exhname")))

# except TimeoutException:
#     print("Timed out waiting for page to load")
#     browser.quit()

# titles_element = browser.find_elements_by_class_name("mys-table-exhname")
# titles = [x.text for x in titles_element]
# for title in titles_element:
# 	print title.text
# 	print '"' + title.find_element_by_css_selector('a').get_attribute('href') + '", '


for url in urls:
	browser.get(url)
	try:
	    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, "sc-Exhibitor_PhoneFax")))
	   # WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, "sc-Exhibitor_Address")))

	except TimeoutException:
	    print("Timed out waiting for page to load")
	    browser.quit()

	titles_element = browser.find_elements_by_class_name("sc-Exhibitor_PhoneFax")
	titles = [x.text for x in titles_element]
	for title in titles_element:
		line = title.text
		line = line.strip('\n')
		line = line.strip('\t')
		line = line.replace('\n',' ')
		line = line.replace('\t',' ')
		print line
		# print '"' + title.find_element_by_css_selector('a').get_attribute('href') + '", '


