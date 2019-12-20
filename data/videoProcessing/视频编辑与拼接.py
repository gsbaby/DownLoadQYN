#!/usr/bin/env python
# coding: utf-8
# Autor GaoSong

import os
from moviepy.editor import *

# 保存所有的视频
saveAllFiles = []

baseFile = r'J:/T'
saveFile = r'J:/T/庆余年'
localFileNames = os.listdir(baseFile)
for f in localFileNames:
    saveAllFiles = []  # 清理一下数据
    # 就不写剔除重复集数了
    if '.' in f:
        print('')
    elif f == '28':
        print('28集已处理')
    elif f == '29':
        print('29集已处理')
    elif f == '30':
        print('30集已处理')
    elif f == '31':
        print('31集已处理')
    else:
        path = baseFile + '/' + os.path.basename(f)
        print(path)
        files = os.listdir(path)
        saveLocalMovies = saveFile + "/" + os.path.basename(f)
        # 文件太吃内存，先解决前250个文件
        for i in range(251):
            file = files[i]
            if not os.path.isdir(file):  # 判断是否是文件夹
                moviesName = os.path.basename(file)
                if '.ts' in moviesName:
                    saveAllFiles.append(VideoFileClip(path + "/" + moviesName))
                    # 如果需要截取部分的话：
                    # VideoFileClip(os.path.abspath(file))).subclip(t_start=8,t_end=(6,51)) 从8秒开始，剪到6分51秒
                    # VideoFileClip(os.path.abspath(file))).cutout(0,5) 减掉0到5秒
        # 先拼接成第一个视频
        video_1 = concatenate_videoclips(saveAllFiles)
        print("video_1处理结束")
        # 将视频1保存
        video_1.write_videofile(saveLocalMovies + "集1.mp4")
        saveAllFiles = []
        # 然后解决剩下的，并拼接成第二个视频
        for i in range(251, len(files)):
            file = files[i]
            if not os.path.isdir(file):  # 判断是否是文件夹
                moviesName = os.path.basename(file)
                if '.ts' in moviesName:
                    saveAllFiles.append(VideoFileClip(path + "/" + moviesName))
        video_2 = concatenate_videoclips(saveAllFiles)
        print("video_2处理结束")
        # 将视频2保存
        video_2.write_videofile(saveLocalMovies + "集2.mp4")
        saveAllFiles = []
        # 将以上两集进行拼接后输出
        # 拼接视频
        video = concatenate_videoclips([video_1, video_2])
        video_1 = ''
        video_2 = ''
        # 保存
        video.write_videofile("J:/T/庆余年/" + os.path.basename(f) + "集.mp4")
        video = ''

        # # 方法二，比较耗时间
        # # 此处是遍历所有的文件
        # for file in files:  # 遍历文件夹
        #     if not os.path.isdir(file):  # 判断是否是文件夹
        #         moviesName = os.path.basename(file)
        #         if '.ts' in moviesName:
        #             saveAllFiles.append(VideoFileClip(path+"/"+moviesName))
        #             # 如果需要截取部分的话：
        #             # VideoFileClip(os.path.abspath(file))).subclip(t_start=8,t_end=(6,51)) 从8秒开始，剪到6分51秒
        #             # VideoFileClip(os.path.abspath(file))).cutout(0,5) 减掉0到5秒
        # # 拼接视频
        # video_before = concatenate_videoclips(saveAllFiles)
        # print(video_before)
        # print(path+"/"+os.path.basename(f)+"集.mp4")
        # # 创建并添加、合成字幕
        # text_clip = TextClip('视频文字',
        #                      fontsize=50,
        #                      font=r'C:\Windows\fonts\STXINGKA.TTF',
        #                      color='black',
        #                      bg_color='transparent',
        #                      transparent=True
        #                      ).set_position(('right','top')).set_duration(1200).set_start(0)
        # video = CompositeVideoClip([video_before,text_clip])
