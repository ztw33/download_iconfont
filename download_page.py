"""只下载iconfont某个页面的所有图标"""

from selenium import webdriver
from pathlib import Path

url = "https://www.iconfont.cn/collections/detail?spm=a313x.7781069.1998910419.d9df05512&cid=23"

# 打开Chrome
opt = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=opt)
driver.implicitly_wait(10)
driver.get(url)
driver.maximize_window()

title = driver.find_element_by_css_selector("#magix_vf_main>div.block-sub-banner>div.block-sub-banner-container.wrap>div>span.title.ml10>span").text
title.replace("/", "-")  # 有些title中包含分隔符
print("[Title] ", title)
Path(title).mkdir(parents=True, exist_ok=True)

icon_list = driver.find_element_by_class_name("collection-detail").find_element_by_class_name("block-icon-list").find_elements_by_tag_name("li")
for icon_wrap in icon_list:
    icon_name = icon_wrap.find_element_by_class_name("icon-name").text
    print("icon name: ", icon_name)
    icon = icon_wrap.find_element_by_class_name("icon-twrap").find_element_by_class_name("icon")
    _ = icon.location_once_scrolled_into_view
    icon.screenshot("./" + title + "/" + icon_name + ".png")
    count += 1

driver.quit()
