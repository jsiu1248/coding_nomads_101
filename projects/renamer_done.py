# Move and rename all .png files on your Desktop

# Identify all screenshots on your Desktop

# Create a new directory

# Move and rename all screenshots
import pathlib

pic_path=pathlib.Path('C:/Users/jsiu/Desktop/screenshots_folder') #path of where the pictures are

new_path=pathlib.Path('C:/Users/jsiu/Desktop/screenshots_renamed') # path where I want the pngs to go
new_path.mkdir(exist_ok=True)

for filepath in pic_path.iterdir(): #looking over where the pictures are and iterating over them
    if filepath.suffix =='.png':
        new_file_name="new"+filepath.name
        new_filepath = new_path.joinpath(new_file_name) # concat the names of the path where I want the pngs to go and the names of the pictures
        #move files to new directory
        filepath.replace(new_filepath) # for the files iterated replace the old name with new names
