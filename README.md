# download iconfont
把阿里巴巴矢量库iconfont中的所有图表爬取到本地。
## require
python3
## run
进入项目目录，命令行下执行bootstrap.sh脚本：
```sh
$ sh bootstrap.sh
```
进入虚拟环境：
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