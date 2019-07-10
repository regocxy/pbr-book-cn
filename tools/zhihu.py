#!/usr/bin/python3

import os
import glob
import re

pattern = re.compile(r"\$(.+?)\$", re.M)
pattern2 = re.compile(r"\$\$(.+?)\$\$", re.M)

file_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.join(file_dir, "..")
dist_dir = os.path.join(root_dir, "dist")


def clear_dir(dir):
    for root, dirs, files in os.walk(dir):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))


def repl(match):
    group = match.group(1)
    return '<img src="https://www.zhihu.com/equation?tex=%s" alt="%s" class="ee_img tr_noresize" eeimg="1">' % (group, group)


def repl2(match):
    group = match.group(1)
    return '\n<img src="https://www.zhihu.com/equation?tex=%s" alt="%s" class="ee_img tr_noresize" eeimg="1">\n' % (group, group)


def main():
    if (not os.path.exists(dist_dir)):
        os.mkdir(dist_dir)

    clear_dir(dist_dir)

    for filename in glob.glob(os.path.join(root_dir, "docs/*")):
        with open(filename, "r", encoding="utf8") as fr:
            with open(os.path.join(dist_dir, os.path.basename(filename)), "w", encoding="utf8") as fw:
                fw.write(pattern.sub(repl, pattern2.sub(repl2, fr.read())))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
