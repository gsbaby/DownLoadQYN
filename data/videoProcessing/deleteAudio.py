#!/usr/bin/env python
# coding: utf-8
# Autor GaoSong
# 删除视频中的音频

import os
from moviepy.editor import *

baseFile = r'J:/T/33_00000.ts'
silenceFileName = r'J:/T/33_0000_无声音.mp4'
video = VideoFileClip(baseFile)

# 删除声音
video = video.without_audio()
video.write_videofile(silenceFileName)