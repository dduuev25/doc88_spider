from  get_screenshot import Doc88Book
from pic_refactor.pic_refac import PicRefactor
import time
from settings import settings001


doc_url = settings001.doc_url
page_num = settings001.page_num
screen_path = settings001.screen_path

doc_to_do = Doc88Book()
retry_times = 0

while retry_times <= 3:
    driver = doc_to_do.set_up(doc_url, 10)
    driver.maximize_window()
    time.sleep(2)
    driver.refresh()
    time.sleep(4)
    try:
        doc_to_do.view_check(driver)
        time.sleep(3)
        doc_to_do.save_img(driver, screen_path, page_num)
        doc_to_do.tear_down(driver)
        print("Job done!!!")
        break
    except Exception as ee:
        print(ee)
        print(f'幻灯片按钮不存在，重试,已重试次数{retry_times}')
        doc_to_do.close_driver(driver)
        retry_times +=1
        continue
    # 顺序保存图片

