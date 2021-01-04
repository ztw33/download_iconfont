from selenium import webdriver
from pathlib import Path

# 设置
home_page = "https://www.iconfont.cn/collections/index?spm=a313x.7781069.1998910419.4"
start_page = 1
end_page = 807
URL = home_page if start_page == 1 else (home_page + "&page=" + str(start_page))
count_block = 1
count_icons = 0


def download_block_icons(driver):
    global count_block
    global count_icons
    title = driver.find_element_by_css_selector("#magix_vf_main>div.block-sub-banner>div.block-sub-banner-container.wrap>div>span.title.ml10>span").text
    title.replace("/", "-")  # 有些title中包含分隔符
    print("[Title] ", title)
    dirpath = "icons/" + str(count_block) + "_" + title
    Path(dirpath).mkdir(parents=True, exist_ok=True)
    icon_list = driver.find_element_by_class_name("collection-detail").find_element_by_class_name("block-icon-list").find_elements_by_tag_name("li")
    for icon_wrap in icon_list:
        icon_name = icon_wrap.find_element_by_class_name("icon-name").text
        icon_name.replace("/", "-")
        print("icon_name: ", icon_name)
        icon = icon_wrap.find_element_by_class_name("icon-twrap").find_element_by_class_name("icon")
        _ = icon.location_once_scrolled_into_view
        icon.screenshot(dirpath + "/" + icon_name + ".png")
        count_icons += 1


def download_onepage(driver, main_window):
    global count_block
    icon_blocks = driver.find_elements_by_class_name("block-collection")
    for block in icon_blocks:
        _ = block.location_once_scrolled_into_view
        block.click()
        all_windows = driver.window_handles
        if len(all_windows) != 2:
            print("Error!! More than 2 windows.")
            exit(1)
        for win in all_windows:
            if win != main_window:
                driver.switch_to.window(win)
                break
        download_block_icons(driver)
        driver.close()
        driver.switch_to.window(main_window)
        count_block += 1


def has_nextpage(driver):
    tmp = driver.find_element_by_css_selector(".wrap.block-pagination.mt20.pr40.light-theme.simple-pagination").find_element_by_tag_name("ul")
    els = tmp.find_elements_by_tag_name("li")
    if els[-1].get_attribute("class") == "disabled":
        print("no more pages")
        return False
    return True


if __name__ == "__main__":
    # 打开Chrome
    opt = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(10)
    driver.get(URL)
    driver.maximize_window()

    main_window = driver.current_window_handle
    cur_page = start_page
    while has_nextpage(driver) and cur_page <= end_page:
        print("Download page ", cur_page, "...")
        download_onepage(driver, main_window)
        # 点击下一页
        next_page = driver.find_element_by_css_selector(".wrap.block-pagination.mt20.pr40.light-theme.simple-pagination").find_element_by_tag_name("ul").find_element_by_css_selector(".page-link.next")
        next_page.click()
        cur_page += 1
    
    print("Total icons: ", count_icons)

    driver.quit()
