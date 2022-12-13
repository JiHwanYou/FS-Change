import os
import sys
import glob
import shutil


def change_folder_structure(working_dir):
    image_dir = os.path.join(working_dir, 'images')
    label_dir = os.path.join(working_dir, 'labels')

    if os.path.isdir(image_dir):
        for file in os.listdir(image_dir):
            shutil.move(os.path.join(image_dir, file), os.path.join(working_dir, file))
        for file in os.listdir(label_dir):
            shutil.move(os.path.join(label_dir, file), os.path.join(working_dir, file))
        os.rmdir(image_dir)
        os.rmdir(label_dir)
    else:
        os.mkdir(image_dir)
        os.mkdir(label_dir)
        for file in os.listdir(working_dir):
            if file.endswith((".jpg", ".png")):
                shutil.move(os.path.join(working_dir,file), os.path.join(image_dir,file))
            elif file.endswith((".txt")):
                shutil.move(os.path.join(working_dir,file), os.path.join(label_dir,file))

# def change_folder_structure(working_dir):
#     image_dir = os.path.join(working_dir, 'images')
#     label_dir = os.path.join(working_dir, 'labels')

#     if os.path.isdir(image_dir):
#         os.system(f'move {image_dir}\*.jpg {working_dir}')
#         os.system(f'move {label_dir}\*.txt {working_dir}')
#         os.rmdir(image_dir)
#         os.rmdir(label_dir)
#     else:
#         os.mkdir(image_dir)
#         os.mkdir(label_dir)
#         os.system(f'move {working_dir}\*.jpg {image_dir}')
#         os.system(f'move {working_dir}\*.txt {label_dir}')

if __name__ =="__main__":
    # dir = "C:/Users/youjh/Downloads/01"
    dir = sys.argv[1]
    change_folder_structure(dir)
