__author__ = 'lws'

import os
import re
import logging

logging.basicConfig(level=logging.DEBUG)

# src_dir = "C:\\Users\\lws\\Documents\\GitHub\\pcgen\\data\\35e\\wizards_of_the_coast\\rsrd\\basics"
# dest_dir = "../35e_rsrd_multiline/"
src_dir = "../dist/"
dest_dir = "../src/"

lst_files = [ f for f in os.listdir(src_dir) if f.endswith(".lst")]

for f in lst_files:
    src_file = os.path.join(src_dir, f)
    dest_file = os.path.join(dest_dir, f)

    if os.path.exists(dest_file):
        logging.warn("%s already exists. Skipping." % dest_file)
        continue


    with open(src_file,"r") as r_fh, open(dest_file,"wb") as w_fh:
        for line in r_fh:
            if re.match("^\s*$", line):
                continue #Blank line
            comment = "#" if re.match("^\s*#", line) else ""
            # Remove newline, split by tabs, and remove empty strings.
            tags = [tag for tag in line.strip().split("\t") if tag is not ""]
            w_fh.write(tags[0] + os.linesep)
            for tag in tags[1:]:
                w_fh.write(comment + '\t' + tag + os.linesep)
            w_fh.write(os.linesep)