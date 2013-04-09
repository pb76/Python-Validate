import os
import sys
import zipfile
from functions import *

if len(sys.argv) != 2:
	print "Expected folder argument: '", sys.argv[0], " folder path '"
	sys.exit()

fileList = []
rootdir = sys.argv[1]
for root, subFolders, files in os.walk(rootdir):
	for file in files:
		fileList.append(os.path.join(root,file))
		#extension = os.path.splitext(file)[1]
		#fileList.append(extension)
		#if (extension == ".zip"):
		if zipfile.is_zipfile(os.path.join(root,file)):
			unzipFile(os.path.join(root,file), rootdir, file)

		
#DEBUG
print fileList