# -*- coding: utf-8 -*

import subprocess
import os
import time

subprocess.call(["cd /Users/zhaoxiang/Desktop/InternDemo \n git diff > /Users/zhaoxiang/Desktop/name.diff"], shell=True)


file1 = "/Users/zhaoxiang/Desktop/name.diff"

file2 = "/Users/zhaoxiang/Desktop/name2.diff"

file3 = "/Users/zhaoxiang/Desktop/name2.diff"

f_diff = "/Users/zhaoxiang/Desktop/d1.diff"
# ----------
f1 = open(file1, "r")
f2 = open(file2, "r")
file1 = f1.readlines()
file2 = f2.readlines()

outfile = open(f_diff, "w")
flag = 0
outfile.write("file1：\n")
for i in file1:
    if i not in file2:
        outfile.write(i)
        flag = 1
        outfile.write("file2：\n")
for i in file2:
    if i not in file1:
        outfile.write(i)
        flag = 1

f2.close()

if flag == 1:
    outfile = open(f_diff, "r")
    str = ""
    for i in outfile:
        for ch in i.decode('utf-8'):
            if ch == "\n" or ch == " ":
                str = ""
                continue
            str += ch
            if(str == "NSLocalizedString"):
                print(str)
                subprocess.call(
                                ["xcodebuild -exportLocalizations -localizationPath /Users/zhaoxiang/Desktop/InternDemo/InternDemo/InternTrans -project /Users/zhaoxiang/Desktop/InternDemo/InternDemo/InternDemo.xcodeproj -exportLanguage ja"],
                                shell=True)

    f3 = open(file3, "w")
    for j in file1:
        f3.write(j)
    f3.close()

outfile.close()
#************************************************************************************************************************
#subprocess.call(["git reset --hard"], shell=True)



subprocess.call(["git pull"], shell=True)
subprocess.call(["xcodebuild -importLocalizations -localizationPath /Users/zhaoxiang/Desktop/InternDemo/InternDemo/InternTrans/ja.xliff -project /Users/zhaoxiang/Desktop/InternDemo/InternDemo/InternDemo.xcodeproj"], shell=True)

