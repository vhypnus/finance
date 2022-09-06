import sys
import os
import shutil

if sys.argv is None or len(sys.argv) != 2:
	print("----输入参数错误------")
	exit()

c = sys.argv[1]
print("输入参数:",c,sep=" ",end="\n")

absp = os.path.abspath(".")

#src path
spath = absp+"\\分时" 
print("src path:",spath,end="\n")
#dirs
ds = os.listdir(spath)

#target path
tpath = absp +"\\"+c
if os.path.exists(tpath):
	print(tpath,"目录已存在，执行删除操作。",sep=" ",end="\n")
	shutil.rmtree(tpath)

os.mkdir(tpath)
print("创建目录:",tpath,"成功",end="\n")

for d in ds:
	#tmp path
	stpath =  spath+"\\"+d+"\\"+c+".png"
	ttpath = tpath+"\\"+d+".png"
	shutil.copy(stpath,ttpath)
	print("拷贝",stpath,"->",ttpath,"成功",end="\n")

