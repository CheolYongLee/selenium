from selenium import webdriver


browser = webdriver.Edge('C:/Users/Administrator/selenium/edgedriver/msedgedriver.exe') # 다운받은 웹 드라이버 경로 지정

browser.get("http://www.naver.com") # 사이트 주소를 입력하여 웹 페이지 접속

search_input = browser.find_element_by_xpath('//*[@id="query"]').send_keys('facebook') # xpath를 이용하여 네이버 홉의 검색창에 겁색어 입력

search_btn = browser.find_element_by_class_name("btn_submit").click() # class name을 이용하여 네이버 홉의 검색 버튼 클릭
