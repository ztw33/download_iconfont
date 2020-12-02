### 过滤掉文件名只包含数字的图片

import os
from pathlib import Path
import shutil

def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        return True
    else:
        return False

def is_alphabet(uchar):
    """判断一个unicode是否是英文字母"""
    if (uchar >= u'\u0041' and uchar<=u'\u005a') or (uchar >= u'\u0061' and uchar<=u'\u007a'):
        return True
    else:
        return False


src_path = "icons"
Path("icons_with_label").mkdir(parents=True, exist_ok=True)
count = 0
for dirpath, dirnames, filenames in os.walk(src_path):
    for filename in filenames:
        count += 1
        name, suf = os.path.splitext(filename)
        filepath = os.path.join(dirpath, filename)
        for ch in name:
            if is_chinese(ch) or is_alphabet(ch):
                Path("icons_with_label/" + dirpath).mkdir(parents=True, exist_ok=True)
                shutil.copyfile(filepath, "icons_with_label/" + filepath)
                break

print("Total: ", count) 