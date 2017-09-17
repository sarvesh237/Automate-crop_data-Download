from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


auto_download_excel = webdriver.FirefoxProfile()
auto_download_excel.set_preference("browser.download.folderList", 2)
auto_download_excel.set_preference("browser.download.manager.showWhenStarting", False)
auto_download_excel.set_preference("browser.download.dir", "/home/sarvesh/crop")
auto_download_excel.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/vnd.ms-excel")

def daydate(a,b,c):
	date_final = a+"/"+b+"/"+c
	return date_final
def autom(j,k):
	driver = webdriver.Firefox(firefox_profile = auto_download_excel)
	driver.get("http://agriexchange.apeda.gov.in/ind_prices/ind_prices.aspx")
	crop = Select(driver.find_element_by_id('DdlVariety'))
	crop.select_by_visible_text(j)
	date = driver.find_element_by_id("txt_date")
	date.send_keys(k)
	driver.find_element_by_name('btn_click').click()
	#next page
	driver.implicitly_wait(100) # seconds
	myDynamicElement = driver.find_element_by_id("ImageButton1")

	driver.find_element_by_id('ImageButton1').click()
	driver.close()

k = [u'Onion', u'Cabbage', u'Cauliflower', u'Brinjal', u'Tomato']

year = ["2014","2015","2016","2017"]
month = ["01","02","03","04","05","06","07","08","09","10","11","12"]
day28 = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28"]
day29 = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28" , "29"]
day30 = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28" , "29" , "30"]
day31 = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28" , "29" , "30", "31"]

for a_crop in k:
	for a_year in year:
		for a_month in month:
			name = raw_input("Choosing mm/dd " +a_month+"/"+a_year+ " and crop " + a_crop + ". Press y to continue : ")
			if name == "y" : 
				if ( a_month == "01" or a_month == "03" or a_month == "05" or a_month == "07" or a_month == "08" or a_month == "10" or a_month == "12"):
					for a_day in day31:
						m=daydate(a_day,a_month,a_year)
						autom(a_crop,m)
						print m
				if ( a_month == "04" or a_month == "06" or a_month == "09" or a_month == "11"):
					for a_day in day30:
						m=daydate(a_day,a_month,a_year)
						autom(a_crop,m)
				if ( a_month == "02"):
					if a_year == "16" :
						for a_day in day29:
							m=daydate(a_day,a_month,a_year)
							autom(a_crop,m)
					else:
						for a_day in day28:
							m=daydate(a_day,a_month,a_year)
							autom(a_crop,m)


