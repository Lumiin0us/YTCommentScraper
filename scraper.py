from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import traceback
import time

try:
    URL = 'https://www.youtube.com/watch?v=EtQwJeec2Ls'
    DELAY = 10

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.get(URL)
    time.sleep(10)
    driver.execute_script('window.scrollTo(0, 500)')
    time.sleep(3)
    try:
        comment = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'comments')))
        # comment_id = driver.find_element(By.ID, 'count')
        time.sleep(5)
        sections = comment.find_element(By.ID, 'sections')
        contents = sections.find_element(By.ID, 'contents')
        count = contents.find_elements(By.TAG_NAME, 'ytd-comment-thread-renderer')

        # for text in count:
        #     comm = text.find_element(By.ID, 'comment')
        #     body = comm.find_element(By.ID, 'body')
        #     main = body.find_element(By.ID, 'main')
        #     comment_content = main.find_element(By.ID, 'comment-content')
        #     expander = comment_content.find_element(By.ID, 'expander')
        #     content = expander.find_element(By.ID, 'content')
        #     content_text = content.find_element(By.ID, 'content_text')
        #     print(content_text.text)








        # print(count.text)
        # //*[@id="contents"]/ytd-comment-thread-renderer[1]
        # //*[@id="contents"]/ytd-comment-thread-renderer[2]
        # 
        print(count)
        # print(count.text)
        # print(comment.get_attribute('innerHTML'))
        print('Page is ready')


    except TimeoutException:
        print('Loading took too much time...')
    time.sleep(5)
    # driver.quit()
except Exception as e:
    print("[EXCEPTION]", e)
    traceback.print_exc()


