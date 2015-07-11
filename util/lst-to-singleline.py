__author__ = 'lws'

import os
import re
import logging
import StringIO
import io

logging.basicConfig(level=logging.DEBUG)

# src_dir = "C:\\Users\\lws\\Documents\\GitHub\\pcgen\\data\\35e\\wizards_of_the_coast\\rsrd\\basics"
# dest_dir = "../35e_rsrd_multiline/"
src_dir = "../src/"
dest_dir = "../dist/"

lst_files = [ f for f in os.listdir(src_dir) if f.endswith(".lst")]

for f in lst_files:
    src_file = os.path.join(src_dir, f)
    dest_file = os.path.join(dest_dir, f)

    if os.path.exists(dest_file):
        logging.warn("%s already exists. Skipping." % dest_file)
        continue

    w_fh = io.BytesIO()

    with open(src_file,"r") as r_fh, open(dest_file,"wb") as w_fh:
        for line in r_fh:
            if re.match("^\s*$", line):
                continue #Blank line

            if line.startswith("#"):
                # Leave comments alone. It doesn't matter if they're multi-line.
                w_fh.write(os.linesep + line.strip())
            elif not line.startswith("\t"):
                # It's a tag name
                w_fh.write(os.linesep + line.strip())
            else:
                # It's a sub-tag
                w_fh.write("\t"+line.strip())