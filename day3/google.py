from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl")
elem = driver.find_element_by_name("q")#특정 요소를 찾는 코드x`
elem.send_keys("방탄소년단 지민") # 키보드 입력값 전송
elem.send_keys(Keys.RETURN) #엔터키 전송

SCROLL_PAUSE_TIME = 1
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click() #결과 더보기 클릭
        except:
            break
    last_height = new_height


images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd") #한개 선택은 element 여러개 선택 elements 작은이미지 클릭해서 큰이미지 띄움
count = 1
for image in images:
    try:
        image.click() 
        time.sleep(3) #브라우저를 클릭하고 동작하는데 시간이 걸리므로 중간에 지연시키는 dummy코드가 필요함.
        imgURL = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")  # 큰이미지의 src 주소값 가져옴
        urllib.request.urlretrieve(imgURL, "test"+str(count)+".jpg")
        count +=1
    except:
        pass

driver.close()


# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
