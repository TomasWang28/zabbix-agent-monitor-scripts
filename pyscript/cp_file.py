#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os,shutil

#定义输入文件的位置
input_path="/root/my_python36/learnpy"
input_pathname, input_filename=os.path.split(input_path)
#定义输出文件夹的位置
output_path="/root/my_python36/testcp2/"+input_filename
output_pathname, output_filename = os.path.split(output_path)

if not os.path.exists(input_path):
    print("%s：指定文件夹或文件不存在！" % input_path)
elif not os.listdir(input_path):
    print("%s: 指定文件夹为空！" % input_path)
else:
    if not os.path.exists(output_pathname):
        print("%s文件夹不存在，正在为您创建%s文件夹" % (output_pathname,output_pathname))
        os.makedirs(output_pathname)
    else:
        if os.path.isdir(input_path):
            try:
                shutil.copytree(input_path,output_path)
            except FileExistsError:
                print("目标文件夹已存在，是否要覆盖？y/n")
                shutil.rmtree(output_path)
                shutil.copytree(input_path, output_path)
                print("目标文件夹已覆盖")
        elif os.path.isfile(output_path):
            shutil.copyfile(input_path,output_path)
        print("复制文件: %s ----------> %s" % (input_path, output_path))
