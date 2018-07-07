#!/usr/bin/python
#coding:utf-8
'''
使用方式：从全站仪导出数据后，删除文件头两行，并把测站信息（BKB、BS开头的行，较少，可手动删除）、角度信息（此次不需要，较多，编程删除或忽略）删除
再清除数据噪声，如不小心重复记录的站点，此次实习中我们组HVD数据产生了几行冗余，可手动剔除。之后就可以使用此脚本完成格式转换，导入南方cass了
'''
import csv
space_lst = []
with open('20180706.TXT') as f:
    reader = csv.reader(f)
    lst = list(reader)

for sub_lst in lst:
    strs = sub_lst[0]
    tmp_lst = strs.split("     ")
    sub_lst[0] = tmp_lst[1]
    space_lst.append(sub_lst)

# end_lst = []
# print space_lst         #space_lst是经过处理的二维数据列表
print len(space_lst)
with open('backup.TXT','w+') as ff:
    for i in range(0,len(space_lst),3):
        ff.write((space_lst[i][0]).lstrip())
        ff.write(',,')
        ff.write(space_lst[i+2][1])
        ff.write(',')
        ff.write(space_lst[i+2][0])
        ff.write(',')
        ff.write(space_lst[i+2][2])
        ff.write('\n')
