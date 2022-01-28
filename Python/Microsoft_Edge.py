from selenium import webdriver


driver = webdriver.Edge('C:/Users/Administrator/selenium/edgedriver/msedgedriver.exe') # 다운받은 웹 드라이버 경로 지정

driver.get("http://www.naver.com") # 사이트 주소를 입력하여 웹 페이지 접속

# 인터넷 창 크기 변경
driver.maximize_window() # 최대화
# driver.minimize_window() # 최소화
# driver.set_window_size(1920, 1280) # 지정 사이즈로 변경

# xpath를 이용한 검색어 입력
def X_path_input(X_path, key):  # X_path는 입력 창 경로, key는 입력할 input 값
    driver.find_element_by_xpath(X_path).send_keys(key)

# class name을 이용한 버튼 클릭
def class_btn_click(class_name):  # 클릭하고자 하는 대상의 class name 입력
    driver.find_element_by_class_name(class_name).click()

# input 초기화
def X_path_clear(X_path):  # 초기화 하고자 하는 text box의 xpath 입력
    driver.find_element_by_xpath(X_path).clear()

X_path_input('//*[@id="query"]', 'facebook') # xpath를 이용하여 네이버 홉의 검색창에 겁색어 입력
class_btn_click('btn_submit') # class name을 이용하여 네이버 홉의 검색 버튼 클릭

# 검색 후 다른내용 재검색
X_path_clear('//*[@id="nx_query"]') # 네이버 검색 창 초기화
X_path_input('//*[@id="nx_query"]', 'instagram') # 홈 페이지가 아닌 검색 실행한 페이지에서 instagram 검색
class_btn_click('bt_search') # 검색 버튼 클릭
