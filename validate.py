import os
import sys

if len(sys.argv) != 2:
	print "Expected folder argument: '", sys.argv[0], " folder path '"
	sys.exit()

fileList = []
rootdir = sys.argv[1]
for root, subFolders, files in os.walk(rootdir):
	for file in files:
		fileList.append(os.path.join(root,file))

print fileList