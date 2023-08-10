import os



location = ""

command = input("Enter Your File pach:")
os.chdir(command)
remove1 = input("Enter Your file name:")
filename = remove1
os.remove(filename)
