###this file is to merge ligand_new.pdb and protein_new.pdb to cat.pdb（onionnet）

# !/usr/bin/python
# -*- coding:utf-8 -*-

import os



rootdir = r"G:\文件\周报\coda\03 onionnet-master\tools"


for parent,dirnames,filenames in os.walk(rootdir):

	for filename in filenames:
            if '_ligand_new.pdb' in filename:
                PDBID = filename.split('_')[0]

                file1 = open(PDBID + '_protein_new.pdb', 'r+')
                #os.system('mkdir ' + PDBID + '_new.pdb')
                new_file = PDBID + '_cat.pdb'###Linux上会自动新建pdb文件？不会报错

                #if not os.path.exists(new_file):
                    #os.system(r"touch {}".format(new_file))
                #file2 = open(new_file,'a+')
                with open(new_file, 'a+') as file2:

                    with open(filename) as lines:
                        for line in lines:
                            if len(line):
                                file2.write(line)



                    for line in file1.readlines():
                        if len(line):
                            file2.write(line)




                file1.close()
                #rename filename
                #os.rename("new_test.txt","test.txt")



