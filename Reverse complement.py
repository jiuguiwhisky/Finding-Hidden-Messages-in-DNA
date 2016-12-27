# 第一次用biophython！

data = open("c:\sample.txt")# 数据量太大不适合直接拷贝到python中，读取txt文件效率高很多
seq=data.read()# 读取数据后格式并不是string,但Seq函数需要读取string格式
seq=str(seq)# string化
from Bio.Seq import Seq# Biopython的包
reverse = Seq(seq) 
print (reverse.reverse_complement())#reverse_complement的函数将配对碱基，并从3'到5'重新排列
