###this file is to delect the protein.pdb's last conect information before cating the protein-ligand file 
###
# !/usr/bin/python
# -*- coding:utf-8 -*-

import re
import os

rootdir = "D:/tx-tanshuoyan-project/onionnet/GPCRdata/DATA"

for parent,dirnames,filenames in os.walk(rootdir):

	for filename in filenames:
            if '_protein.pdb' in filename:
                PDBID = filename.split('.')[0]

                file1 = open(PDBID + '.pdb', 'r+')
                #os.system('mkdir ' + PDBID + '_new.pdb')
                new_file = PDBID + '_new.pdb'   ###Linux上会自动新建pdb文件？不会报错

                if not os.path.exists(new_file):
                    os.system(r"touch {}".format(new_file))
                file2 = open(new_file,'r+')
                istxt = re.compile(r'.*ANISOU*',re.I)
                for line in file1.readlines():
                   line = line.strip()
                   ifstr = re.findall(istxt,line)
                   if ifstr:
                     line = []
                   else:
                     file2.write(line  + '\n')

                file1.close()
                file2.close()
                #rename filename
                os.rename("new_test.txt","test.txt")
