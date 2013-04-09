import zipfile
import os

def unzipFile( filePath, rootDir, archiveName ):
	print "Packar upp: ", filePath
	dest_folder = os.path.join(rootDir, os.path.splitext(archiveName)[0])
	print "Dest_folder:", dest_folder
	
	if not os.path.exists(dest_folder):
		os.makedirs(dest_folder)
		
	zfile = zipfile.ZipFile( filePath, "r" )
	
	for info in zfile.infolist():
		fname = info.filename
		# decompress each file's data
		data = zfile.read(fname)
		#print "FNAME", fname
		zfile.extract(fname, dest_folder)

	os.remove(filePath)