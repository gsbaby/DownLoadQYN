#!/usr/bin/env python
# coding: utf-8
# Autor GaoSong
# 分割视频中的音频成MP3

import os
from moviepy.editor import *

baseFile = r'J:/T'
localFileNames = os.listdir(baseFile)
for f in localFileNames:
    # print(f)
    if '.' in f:  # 判断是否是文件夹
        print('')
    else:
        path= baseFile + '/' + os.path.basename(f)
        if not os.path.exists(path+'/mp3'):
            os.mkdir(path+'/mp3')
        files = os.listdir(path)
        for file in files:  # 遍历文件夹
            if not os.path.isdir(file):  # 判断是否是文件夹
                moviesName = os.path.basename(file)
                if '.ts' in moviesName:
                    moviesFileName = path + '/' + moviesName
                    mp3Name = moviesName.split(".")[0] + ".mp3"
                    mp3FileName = path + '/mp3/' + mp3Name
                    print(moviesName)
                    if not os.path.exists(path + '/mp3/' + mp3Name):
                        video = VideoFileClip(moviesFileName)
                        video.audio.write_audiofile(mp3FileName)

# path = r'J:/T/33'
# files = os.listdir(path)
# for file in files:  # 遍历文件夹
#     if not os.path.isdir(file):  # 判断是否是文件夹
#         moviesName = os.path.basename(file)
#         if '.ts' in moviesName:
#             moviesFileName = path + '/' + moviesName
#             mp3Name = moviesName.split(".")[0] + ".mp3"
#             mp3FileName = path + '/mp3/' + mp3Name
#             print(moviesName)
#             video = VideoFileClip(moviesFileName)
#             video.audio.write_audiofile(mp3FileName)


