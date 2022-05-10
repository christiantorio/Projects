from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Main Function
if __name__ == '__main__':
    
    #options list
	options = webdriver.ChromeOptions()
	options.add_argument("--start-maximized")
	options.add_argument("--log-level=3")

	# Provide the path of chromedriver present on your system.
	driver = webdriver.Chrome(executable_path="chromedriver", options=options)
    
	driver.set_window_size(1920,1080)

	# Send a get request to the url
	print("Going to python website...")
	driver.get("https://www.python.org")
	print("This is the title of the website: " + driver.title)
	print(".....")
	print("assert test...")
	assert "Google" in driver.title

    
	print("Looking for something in search bar...")
	element = driver.find_element_by_id("id-search-field")
	element.send_keys("flask", Keys.ENTER)
	time.sleep(10)
   
	driver.back()
    
    #using option to leave open
	time.sleep(10)
 
    #close window
	driver.quit()
 
    # just showing terminal its done
	print("Done.......")