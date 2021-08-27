from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
import os


class Doc88Book:
    def __init__(self,driver_path=r"D:\edgedriver\msedgedriver.exe"):
        self.driver_path = driver_path


    def set_up(self,doc_url,implicitly_wait_time=20):
        driver = webdriver.Edge(executable_path=self.driver_path)
        driver.implicitly_wait(implicitly_wait_time)
        driver.get(doc_url)
        return driver

    def close_driver(self,driver):
        driver.close()

    def tear_down(self,driver):
        print("Will quit in 3 seconds")
        time.sleep(3)
        driver.quit()

    def view_check(self,driver,view_x_path='//*[@id="doc-view"]',full_screen_path='//*[@id="pptModelButton"]'):
        # try:
        doc_view = driver.find_element_by_xpath(view_x_path)
        ActionChains(driver).move_to_element(doc_view).perform()
        # 点击全屏ppt模式
        full_screen = driver.find_element_by_xpath(full_screen_path)
        full_screen.click()
        # except exceptions.NoSuchElementException:
        #     print('模式显示按钮不存在')
        #     return False




    def save_img(self,driver,screen_path,page_num):
        try:
            time.sleep(2)
            for i in range(1, page_num + 1):
                time.sleep(2)
                if os.path.exists(screen_path + '/' + str(i) + '.png'):
                    print(f"第{i}页文件已存在，删除")
                    os.remove(screen_path + '/' + str(i) + '.png')
                # 截图
                driver.save_screenshot(screen_path + '/' + str(i) + '.png')
                # 点击键盘向右
                ActionChains(driver).send_keys(Keys.RIGHT).perform()
                time.sleep(2)
                print("第{}页截图完成".format(str(i)))

        except Exception as ee:
            return ee



# if __name__ == "__main__":
#     doc_url = 'https://www.doc88.com/p-10359441830592.html'
#     page_num = 568
#     screen_path = 'D:\\screenshots\\django project'
#
#     doc_to_do = Doc88Book()
#     retry_times = 0
#
#     while retry_times <= 3:
#         driver = doc_to_do.set_up(doc_url, 10)
#         driver.maximize_window()
#         time.sleep(2)
#         driver.refresh()
#         time.sleep(4)
#         try:
#             doc_to_do.view_check(driver)
#             break
#         except Exception as ee:
#             print(ee)
#             print(f'幻灯片按钮不存在，重试,已重试次数{retry_times}')
#             driver.close()
#             retry_times +=1
#             continue
#     # 顺序保存图片
#     time.sleep(3)
#     doc_to_do.save_img(driver,screen_path,page_num)
#     doc_to_do.tear_down(driver)
