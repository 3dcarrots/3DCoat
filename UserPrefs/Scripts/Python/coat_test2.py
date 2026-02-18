import coat
print(coat.io.installPath())
print(coat.io.dataPath())
coat.io.dataPath()
files=coat.io.ListFiles(coat.io.dataPath(), "*.*", False)
for a in files:
	print(a)
