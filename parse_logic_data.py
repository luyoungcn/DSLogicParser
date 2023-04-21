#!/usr/bin/python3
#-- coding: UTF-8 --

import sys

if (len(sys.argv) != 2):
    print("usage: python3 xxx.py xxx.txt")

# TODO 检测文件是否存在


loop = 0
index = 0
output_file_name = ""


class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "w+")
        #可以选择"w"
        self.log = open(filename, "w+", encoding="utf-8")  # 防止编码错误
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
    def flush(self):
        pass
    def reset(self):
        self.log.close()
        sys.stdout=self.terminal


def parse_header(str):
    list = str.split(":")
    output_file_name = list[2].strip().replace(" ", "_")
    output_file_name = output_file_name+".txt"
    return output_file_name


f = open(sys.argv[1]) # 返回一个文件对象


line = f.readline()

# 文件第一行是标题：Id,Time[ns],0:SPI: MISO data
output_file_name=parse_header(line)
sys.stdout = Logger(output_file_name)


# 有效数据格式：0,2072560.00000000000000000000,FD
line = f.readline().split(",")[-1]

while line:
    if index >= 256:
        index = 0

    if index == 0:
        #print("\n")
        print("\nindex:  01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16")

    #if index%16 == 0:
    if loop%16 == 0:
        print("0X{:04X}".format(index),end=": ")


    line = line.strip('\n')
    if loop < 16:
        print(line,end=" ")
        if loop == 15:
            print()
            loop = 0
        else:
            loop+=1

    index+=1
    #line = f.readline()
    line = f.readline().split(",")[-1]

sys.stdout.reset()
f.close()
