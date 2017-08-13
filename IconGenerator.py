#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

'''
图片尺寸批量修改,用于Android开发中生成多种尺寸的Icon
运行环境 Python3
依赖包 pillow
'''

import sys
from PIL import Image

def load_sizes():
    result = []
    try:
        size_file = open("size_list")
        for file_line in size_file.readlines():
            content = file_line.strip('\n').split(',')
            line = (int(content[0]), int(content[1]))
            print(line)
            result.append(line)

    finally:
        size_file.close()
    
    return result

def main():
    path = ''
    path = sys.argv[1]

    if path != '':
        try:
            logo = Image.open(path)
            sizes = load_sizes()
            for size in sizes:
                logo.thumbnail(size)
                logo.save("logo_" + str(size[0]) + "X" + str(size[1]) + ".png")

        finally:
            logo.close()

    else:
        print("没有找到文件")

if __name__ == '__main__':
    main()
