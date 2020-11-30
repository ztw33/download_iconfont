from selenium import webdriver
import time

# 首页地址
URL = "https://www.iconfont.cn/collections/index?spm=a313x.7781069.1998910419.4"

# 打开Chrome
opt = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=opt)
driver.implicitly_wait(10)
driver.get(URL)
driver.maximize_window()


main_window = driver.current_window_handle

elements = driver.find_elements_by_class_name("block-collection")
# for el in elements:
#     el.click()
elements[0].click()

all_windows = driver.window_handles
if len(all_windows) != 2:
    print("Error!! More than 2 windows.")
    exit(1)
for win in all_windows:
    if win != main_window:
        driver.switch_to.window(win)
        break

icon_list = driver.find_element_by_class_name("collection-detail").find_element_by_class_name("block-icon-list").find_elements_by_tag_name("li")
for icon_wrap in icon_list:
    icon_name = icon_wrap.find_element_by_class_name("icon-name").text
    print(icon_name)
    icon = icon_wrap.find_element_by_class_name("icon-twrap").find_element_by_class_name("icon")
    icon.screenshot("png/" + icon_name + ".png")


# print(driver.find_element_by_id('magix_vf_main').get_attribute('innerHTML'))
# icons = driver.find_elements_by_css_selector('div.collection-detail > ul')
# print(len(icons))
# for icon in icon_list.find_elements():
#     print(icon.text)



time.sleep(2)
driver.quit()

#magix_vf_main > div.wrap > div.page-collection-detail-wrap > div.collection-detail > ul

