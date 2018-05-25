# -*- coding: utf-8 -*
# !/usr/bin/env python

import subprocess
import os
import time
from xml.dom.minidom import parse
from lxml import etree
import xml.dom.minidom
import xlrd

# ************************************************************************************************************************
# subprocess.call(["git reset --hard"], shell=True)

xliffItemList = []  # 定义一个全局的item，保存需要翻译的xliff元素
excelItemList = []  # 定义一个全局的item，保存需要翻译的excel元素
is_push = False
Push = False


class item:
    def __init__(self):
        self.id = ""  # 翻译关键字的唯一标识符
        self.sourceStr = ""  # 需要翻译的关键字
        self.transStr = ""  # 翻译过后的关键字


# 文本保存
def saveText():
    for xliffItem in xliffItemList:
        for excelItem in excelItemList:
            if xliffItem.sourceStr == excelItem.sourceStr:
                xliffItem.transStr = excelItem.transStr
                changeText(xliffItem.sourceStr, xliffItem.transStr)
                break


# 修改xliff文件
def changeText(sourceStr, transStr):
    # 写入xliff
    # 1. 读取xml文件
    global is_push
    is_push = True
    tree = etree.parse("/Users/zhaoxiang/Desktop/myXliff/ja.xliff")
    root = tree.getroot()
    for child in root:
        for childs in child:
            for ch in childs:
                if ch.get('id') is not None:
                    #  cid = ch.get('id').encode("utf-8")
                    if ch[0].text == sourceStr:
                        is_target = False  # 标识是否由target标签
                        for cch in ch:
                            if getTatger(cch.tag):  # 找到标签为taget
                                is_target = True
                                cch.text = transStr

                        if is_target == False:  # 当把找到的id里面的节点遍历完后仍没有target值时，则增加
                            node = etree.Element('target')
                            node.text = transStr
                            ch.append(node)

    tree.write("/Users/zhaoxiang/Desktop/myXliff/ja.xliff", encoding="utf-8", xml_declaration=True)


def getTatger(tag):
    flag = 0
    str = ""
    for ch in tag:
        if cmp(ch, '}') == 0 and flag == 0:
            flag = 1
            continue
        if flag == 1:
            str += ch
    if cmp(str, 'target') == 0:
        return True
    return False


def rwLocalXLIFF():
    # 读取xliff的数据并与表格对比
    DomTree = xml.dom.minidom.parse("/Users/zhaoxiang/Desktop/myXliff/ja.xliff")
    collection = DomTree.documentElement

    trans_units = collection.getElementsByTagName("trans-unit")

    for trans_unit in trans_units:
        if trans_unit.hasAttribute("id"):
            idStr = trans_unit.getAttribute("id")
            source = trans_unit.getElementsByTagName('source')[0]
            sourceStr = source.childNodes[0].data

            targetStr = ""
            if trans_unit.getElementsByTagName('target'):
                target = trans_unit.getElementsByTagName('target')[0]
                targetStr = target.childNodes[0].data

            tempItem = item()
            tempItem.id = idStr
            tempItem.sourceStr = sourceStr
            tempItem.transStr = targetStr
            xliffItemList.append(tempItem)


def rwLocalEXCEL():  # 先读取原有的，在读取xliff里有excel里没有的，然后在重新写入Excel；
    b = os.path.exists(r'//Users/zhaoxiang/Desktop/myXliff/data.xls')
    if (b == False):
        print("当前程序本地没有数据表格")
    data = xlrd.open_workbook('/Users/zhaoxiang/Desktop/myXliff/data.xls')
    table = data.sheet_by_index(0)

    nrows = table.nrows
    for rowNum in range(0, nrows):
        colnames = table.row_values(rowNum)
        tempItem = item()
        tempItem.sourceStr = colnames[0]
        tempItem.transStr = colnames[1]
        excelItemList.append(tempItem)


def PushGit():
    subprocess.call(
        ["cd /Users/zhaoxiang/Desktop/myXliff \n git add . \n git commit -m 'zzz' \n git pull \n git push"],
        shell=True)


def check():
    file1 = "/Users/zhaoxiang/Desktop/name.diff"

    file2 = "/Users/zhaoxiang/Desktop/name2.diff"

    f_diff = "/Users/zhaoxiang/Desktop/d1.diff"

    # ---------- 对比文件内容，输出差异
    f1 = open(file1, "r")
    f2 = open(file2, "r")
    file1 = f1.readlines()
    file2 = f2.readlines()
    f1.close()
    f2.close()
    outfile = open(f_diff, "w")
    flag = 0
    outfile.write("file1独有的数据：\n")
    for i in file1:
        if i not in file2:
            outfile.write(i)
            flag = 1
    outfile.write("file2独有的数据：\n")
    for i in file2:
        if i not in file1:
            outfile.write(i)
            flag = 1
    outfile.close()
    is_push = False
    global Push
    if flag == 1:
        rfile = open(f_diff, "r")
        file3 = rfile.readlines()
        for i in file3:
            str = "NSLocalizedString"
            if str in i:
                is_push = True
                Push = True
            # for ch in i:
            #     if ch == "\n" or ch == " ":
            #         str = ""
            #         continue
            #     str += ch
            #     if str == "NSLocalizedString":
            #         is_push = True
            #         Push = True
        rfile.close()

    if is_push:
        subprocess.call([
            "xcodebuild -exportLocalizations -localizationPath /Users/zhaoxiang/Desktop/myXliff -project /Users/zhaoxiang/Desktop/InternDemo/InternDemo/InternDemo.xcodeproj -exportLanguage ja"],
            shell=True)

    f4 = open("/Users/zhaoxiang/Desktop/name.diff")
    r1 = f4.readlines()
    w1 = open("/Users/zhaoxiang/Desktop/name2.diff", "w")

    for i in r1:
        w1.write(i)


def main():
    subprocess.call(["cd /Users/zhaoxiang/Desktop/InternDemo \n git diff > /Users/zhaoxiang/Desktop/name.diff"],
                    shell=True)
    subprocess.call(["cd /Users/zhaoxiang/Desktop/myXliff \n git pull"], shell=True)

    check()

    global Push

    if Push == True:
        rwLocalXLIFF()
        rwLocalEXCEL()
        saveText()

        global is_push
        subprocess.call([
                            "xcodebuild -importLocalizations -localizationPath /Users/zhaoxiang/Desktop/myXliff/ja.xliff -project /Users/zhaoxiang/Desktop/InternDemo/InternDemo/InternDemo.xcodeproj"],
                        shell=True)
        PushGit()


if __name__ == "__main__":
    main()
    pass

