import os

os.system("touch bcreds.json")

os.system("mkdir code")
os.system("mkdir code/sandbox")
os.system("mkdir data")
os.system("mkdir notes")
os.system("mkdir work")
os.system("mkdir work/notes")
os.system("mkdir work/code")

os.system("git clone https://github.com/brandontkessler/notes.git ./notes/")
os.system("git clone https://github.com/brandontkessler/GenData.git ./code/data_generator/")
os.system("git clone https://github.com/brandontkessler/decorators.git ./code/decorators/")
os.system("git clone https://github.com/brandontkessler/data_structures.git ./code/data_structures/")

