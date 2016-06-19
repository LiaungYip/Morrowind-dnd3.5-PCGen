import easygui
import os
import re
import shutil


def find_lst_files():
    src_dir = easygui.diropenbox(default=r"C:\Users\lws\Desktop\pcgen installers\pcgen\data")
    lst_files = []
    for root, dirs, files in os.walk(src_dir):
        for f in files:
            fn, ext = os.path.splitext(f)
            if ext == ".lst":
                full_name = os.path.join(root, f)
                lst_files.append(full_name)
    return lst_files

def convert_line(line):
    line = line.rstrip()
    elements = re.split("\t+",line)

    is_comment = True if re.match("\s*#", line) else False
    if is_comment == False:
        output = "\n\t".join(elements)
    else:
        output = "\n#\t".join(elements)
    return output

def convert_file(lst_file_name, backup = True):
    if not os.path.exists(lst_file_name + ".bak"):
        shutil.copy(lst_file_name, lst_file_name + ".bak")

    with open(lst_file_name + ".bak","r") as f1:
        with open(lst_file_name,"w") as f2:
            f2.write("\n".join([convert_line(l) for l in f1]))


lst_files = find_lst_files()
for f in lst_files:
    print f
    convert_file(f)