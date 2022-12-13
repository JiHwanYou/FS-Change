import os
import sys
import glob
import shutil



def change_folder_structure_recursive(working_dir):
    

    for path, dirs, files in os.walk(working_dir):
        b_rm_folder = False

        for file in files:
            if file.endswith((".jpg", ".png")):
                if path.endswith('images'):
                    shutil.move(os.path.join(path, file), os.path.join(path, os.pardir, file))
                    b_rm_folder = True
                else:
                    os.makedirs(os.path.join(path, 'images'), exist_ok=True)
                    shutil.move(os.path.join(path,file), os.path.join(path, 'images', file))

            elif file.endswith((".txt")):
                if path.endswith('labels'):
                    shutil.move(os.path.join(path, file), os.path.join(path, os.pardir, file))
                    b_rm_folder = True
                else:
                    os.makedirs(os.path.join(path, 'labels'), exist_ok=True)
                    shutil.move(os.path.join(path,file), os.path.join(path, 'labels', file))

        if b_rm_folder:
            os.rmdir(path)

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


if __name__ =="__main__":
    # dir = "C:/Users/youjh/Downloads/ddae"
    dir = sys.argv[1]
    change_folder_structure_recursive(dir)
