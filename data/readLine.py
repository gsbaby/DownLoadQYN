#!/usr/bin/env python
# coding: utf-8

import os
import sys
import time
from subprocess import call

IDM = r'C:\Program Files (x86)\Internet Download Manager\IDMan.exe'
baseUrl = r'https://ll1.7639616.com'
str2 = "/hls"

def run():
    # 保存所有的txt文件
    saveAllFile = []
    path1 = "./"
    files = os.listdir(path1)
    for file in files:  # 遍历文件夹
        if not os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开
            f = os.path.basename(file)
            if '.txt' in f:
                fileNames = path1 + f[0:2] + "集.txt"
                print(fileNames)
                for line in open(fileNames):
                    if str2 in line:
                        print(line)
                        line=line.split('\n')[0]
                        DownPath = r'J:/T/' + fileNames.split('集')[0]
                        DownUrl = baseUrl + line
                        FileName = line.split('/')
                        OutPutFileName = fileNames.split('集')[0] + '_' + FileName[len(FileName) - 1].split('_')[1]
                        call([IDM, '/d', DownUrl, '/p', DownPath, '/f', OutPutFileName, '/n', '/a'])

if __name__ == '__main__':
    run()
