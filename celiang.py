#!/usr/bin/python
#coding:utf-8
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
