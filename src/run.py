# -*- coding: utf-8 -*-
# @Author: YangZhou
# @Date:   2017-06-21 01:41:49
# @Last Modified by:   YangZhou
# @Last Modified time: 2018-01-16 21:38:30
import os
if not os.path.exists("bin/"):
    os.mkdir("bin")
# copy files
os.system("cp bookcover chapter* bin/ -r")
os.system("cp *tex *.bib Makefile templates/* bin/")

os.chdir("bin")
os.system('make main.pdf')
