import os
import sys
import os.path
import re

args = sys.argv[1]


d = re.search(r'\d{4}-\d{2}-\d{2}', args)
if d is None:
	print("-----")
	exit()

for dirpath, dirnames, filenames in os.walk(".\\板块"):

	for filename in filenames:
		if re.search(r'\d{4}-\d{2}-\d{2}',filename) is None:
			print(os.path.join(dirpath,filename) )
			os.rename(os.path.join(dirpath,filename) ,os.path.join(dirpath,d.group(0)+".png") )

