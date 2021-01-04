"""只下载iconfont某个页面的所有svg图标"""
from time import sleep

from selenium.webdriver import ActionChains

from selenium import webdriver
from pathlib import Path

url = "https://www.iconfont.cn/collections/detail?spm=a313x.7781069.1998910419.d9df05512&cid=23"
chrome_user_data_dir = "/Users/zhutingwei/Library/Application Support/Google/Chrome"
download_path = "/Users/zhutingwei/PycharmProjects/iconfont/download"

# 打开Chrome
opt = webdriver.ChromeOptions()
opt.add_argument(r"user-data-dir=" + chrome_user_data_dir)   # 添加本地Chrome用户数据文件夹，保持登录态
opt.add_experimental_option('excludeSwitches', ['enable-automation'])   # 防止网站发现使用模拟器
prefs = {'profile.default_content_settings.popups': 0,
         'download.default_directory': download_path,
         'download.prompt_for_download': False,
         'download.directory_upgrade': True,
         'safebrowsing.enabled': True}
opt.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(options=opt)
driver.implicitly_wait(10)
driver.get(url)
driver.maximize_window()

icon_list = driver.find_element_by_class_name("collection-detail").find_element_by_class_name("block-icon-list").find_elements_by_tag_name("li")
for icon_wrap in icon_list:
    icon_download = icon_wrap.find_element_by_class_name("icon-name")
    _ = icon_download.location_once_scrolled_into_view
    ActionChains(driver).move_to_element(icon_download).perform()  # 在name处悬停，显示下载按钮
    icon_wrap.find_element_by_class_name("icon-cover").find_element_by_class_name("icon-xiazai").click()  # 点击下载

    # svg下载按钮
    download_svg_btn = driver.find_element_by_class_name("download-dialog").find_element_by_class_name("download-btns").find_elements_by_tag_name("span")[0]
    download_svg_btn.click()
    driver.find_element_by_class_name("mp-e2e-dialog-close").click()  # close dialog


driver.quit()
