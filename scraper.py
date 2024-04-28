from selenium import webdriver 
from bs4 import BeautifulSoup 
 
# Set up the browser 
driver = webdriver.Chrome() 
driver.get("https://www.bbc.co.uk/news/business") 
 
# Get the page source after the JavaScript has executed 
page_source = driver.page_source 
 
# Use BeautifulSoup to parse the HTML 
soup = BeautifulSoup(page_source, 'html.parser') 

def filter_headlines(p_class):
	if p_class.attrs['class'][1] == "exn3ah96":
		return True
	else:
		return False

p_classes = filter(filter_headlines, soup.find_all('p'))

for p_class in p_classes:  
	print(p_class.text)
 
# Close the browser 
driver.quit()
