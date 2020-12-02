# download iconfont
把阿里巴巴矢量库iconfont中的所有图表爬取到本地。
## require
- python3
- Chrome浏览器
- 在[Chrome Driver](http://chromedriver.storage.googleapis.com/index.html)中下载与自己操作系统及Chrome版本对应的Chrome driver
## run
进入项目目录，命令行下执行bootstrap.sh脚本：
```sh
$ sh bootstrap.sh
```
将下载的chromedriver.zip解压后的可执行文件移动到venv/bin/下(即和使用的python位于同一路径下)，然后进入虚拟环境：
```sh
$ source venv/bin/activate
```
爬取页面范围内的图标，在download.py中设置起始页面、终止页面和起始block序号：
```python
start_page = 1
end_page = 807
count_block = 1
```
执行download.py：
```sh
$ python download.py
```
若只想下载某个页面的所有图标，在download_page.py中设置目标url后执行download_page.py即可：
```sh
$ python download_page.py
```
可执行filter.py过滤掉文件名只包含数字的图片。