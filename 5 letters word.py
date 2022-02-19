from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


s = Service('C:/Users/USER/Downloads/chromedriver.exe')
driver = webdriver.Chrome(service = s)
driver.get('https://www.bestwordlist.com/5letterwords.htm')

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'mot'))
)
words = driver.find_elements('class name', 'mot')
words2 = driver.find_elements('class name', 'mot2')
list = []

def flatten(x, list):
    x = x.split(' ')
    for l in x:
        list.append(l)
    return list

for word in words:
    flatten(word.text,list)
for word in words2:
    flatten(word.text,list)


#蒐集後面14頁的內容
for i in range(2,16):
    driver.get(f'https://www.bestwordlist.com/5letterwordspage{i}.htm')
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'mot'))
    )
    words = driver.find_elements('class name', 'mot')
    words2 = driver.find_elements('class name', 'mot2')

    for word in words:
        flatten(word.text, list)
    for word in words2:
        flatten(word.text, list)
print(list)
