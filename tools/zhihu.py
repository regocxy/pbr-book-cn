import os
import glob
import re

# <img src="https://www.zhihu.com/equation?tex=\1" alt="\1" class="ee_img tr_noresize" eeimg="1">
# \n<img src="https://www.zhihu.com/equation?tex=\1" alt="\1" class="ee_img tr_noresize" eeimg="1">\n
file_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.join(file_dir, "..")
dist_dir = os.path.join(root_dir, "dist")

def clear_dir(dir):
    for root, dirs, files in os.walk(dir):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

def main():
    if (not os.path.exists(dist_dir)):
        os.mkdir(dist_dir)

    clear_dir(dist_dir)

    for filename in glob.glob(os.path.join(root_dir, "docs/*")):
        with open(filename, "r") as fr:
            with open(os.path.join(dist_dir, os.path.basename(filename)), "w") as fw:
                # fw.write(fr.read())
                print(fr.read())

 
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
