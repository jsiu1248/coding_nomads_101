# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.
import pathlib

#current=pathlib.Path().cwd() # how to get the cwd
#print(current)


#filter for screenshots meaning move all files with .png

path=pathlib.Path('C:\\Users\\jsiu\\Documents\\codingnomads\\python-101-main_jsiu\\python-101-main')

"""
#iterdir - iterates over the files in directory
for filepath in path.iterdir():
    if filepath.is_dir(): # testing if it is a directory
        print(f"    {filepath.name}")

        for file_name in filepath.iterdir():
            if file_name.suffix =='.py':
                print(f"        {file_name.name}")
        print('\n')

        #look for function different than iterdir

                #if folder.is_dir():
                 #   for folder in filepath.iterdir():
                  #      if filepath.suffix == '.py':
                   #         print(filepath.name)
"""



"""
for p in path.rglob("*"): # recursively iterate through all subdirectories
     print(p.name)
"""
from pprint import pprint
for p in path.rglob("*"): # iterate through all subdirectories
    if p.is_dir():
        pprint(p.name)
    if p.suffix == '.py':
        pprint(f'    {p.name}')