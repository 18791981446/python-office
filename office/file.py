#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: 文件.py
# Mail: 1957875073@qq.com
# Created Time:  2022-4-25 10:17:34
# Description: 有关 文件 的自动化操作
#############################################


import os


def replace4filename(path, del_content, replace_content=None):
    """
    :param path: 需要替换的文件夹路径
    :param del_content: 需要删除/替换的内容
    :param replace_content: 替换后的内容，可以不填 = 直接删除
    :return: 
    """
    # 获取该目录下所有文件，存入列表中；不包含子文件夹
    fileList = os.listdir(path)

    for old_file_name in fileList: #依次读取该路径下的文件名
        if del_content in old_file_name:
            if replace_content:
                new_file_name = old_file_name.replace(del_content, replace_content)
            else:
                new_file_name = old_file_name.replace(del_content, '')
            os.rename(path + os.sep + old_file_name, path + os.sep + new_file_name)

            print("原文件名是：{}，修改后为：{}".format(old_file_name, new_file_name))
