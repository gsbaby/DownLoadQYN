#!/usr/bin/env python
# coding: utf-8
# Autor GaoSong

import os
from moviepy.editor import *

# 保存所有的视频
saveAllFiles = []

baseFile = r'J:/T/31'
saveFile = r'J:/T/庆余年/31'
saveAllFiles = []  # 清理一下数据
files = os.listdir(baseFile)

# 文件太大，先解决前100
for i in range(101):
    file = files[i]
    if not os.path.isdir(file):  # 判断是否是文件夹
        moviesName = os.path.basename(file)
        if '.ts' in moviesName:
            saveAllFiles.append(VideoFileClip(baseFile + "/" + moviesName))
# 拼接视频
video_1 = concatenate_videoclips(saveAllFiles)
print("video_1")
video_1.write_videofile(saveFile + "/31集1.mp4")
saveAllFiles = []
video_1 = ''

# 解决101-200
for i in range(101, 201) :
    if i ==len(files):
        print('')
    file = files[i]
    if not os.path.isdir(file):  # 判断是否是文件夹
        moviesName = os.path.basename(file)
        if '.ts' in moviesName:
            saveAllFiles.append(VideoFileClip(baseFile + "/" + moviesName))
video_2 = concatenate_videoclips(saveAllFiles)
print("video_2")
video_2.write_videofile(saveFile + "/31集2.mp4")
saveAllFiles = []
video_2 = ''

# 解决201-300
for i in range(201, 301) :
    if i ==len(files):
        print('')
    file = files[i]
    if not os.path.isdir(file):  # 判断是否是文件夹
        moviesName = os.path.basename(file)
        if '.ts' in moviesName:
            saveAllFiles.append(VideoFileClip(baseFile + "/" + moviesName))
video_3 = concatenate_videoclips(saveAllFiles)
print("video_3")
video_3.write_videofile(saveFile + "/31集3.mp4")
saveAllFiles = []
video_3 = ''

# 解决301-400
for i in range(301, 401) :
    if i ==len(files):
        print('')
    file = files[i]
    if not os.path.isdir(file):  # 判断是否是文件夹
        moviesName = os.path.basename(file)
        if '.ts' in moviesName:
            saveAllFiles.append(VideoFileClip(baseFile + "/" + moviesName))
video_4 = concatenate_videoclips(saveAllFiles)
print("video_4")
video_4.write_videofile(saveFile + "/31集4.mp4")
saveAllFiles = []
video_4 = ''

# 然后解决剩下的
for i in range(401, len(files)) :
    if i ==len(files):
        print('')
    file = files[i]
    if not os.path.isdir(file):  # 判断是否是文件夹
        moviesName = os.path.basename(file)
        if '.ts' in moviesName:
            saveAllFiles.append(VideoFileClip(baseFile + "/" + moviesName))
video_5 = concatenate_videoclips(saveAllFiles)
print("video_5")
video_5.write_videofile(saveFile + "/31集5.mp4")
saveAllFiles = []
video_5 = ''
