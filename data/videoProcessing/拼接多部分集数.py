#!/usr/bin/env python
# coding: utf-8
# Autor GaoSong
# 把视频拼接起来，并且还可以添加字幕

import os
from moviepy.editor import *

# 保存所有的视频
saveAllFiles = []

baseFile = r'J:/T/庆余年/31'

files = os.listdir(baseFile)
for file in files:  # 遍历文件夹
    if not os.path.isdir(file):  # 判断是否是文件夹
        moviesName = os.path.basename(file)
        if '.mp4' in moviesName:
            saveAllFiles.append(VideoFileClip(baseFile + "/" + moviesName))
    # 拼接视频
video = concatenate_videoclips(saveAllFiles)
video.write_videofile("J:/T/庆余年/31集.mp4")
