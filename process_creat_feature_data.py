##this file is to creat *.dat to the generate_feature.py
##将准备好的许多complex.pdb写入到一个dat文件里

import os
import os.path
rootdir = "D:\\tx-tanshuoyan-project\\onionnet\\GPCRdata\\DATA"

file_object = open('D:\\tx-tanshuoyan-project\\onionnet\\GPCRdata\\input_PDB_gpcr_testing.dat','w')


for parent,dirnames,filenames in os.walk(rootdir):

	for filename in filenames:

		print (filename)

		if "_complex.pdb" in filename:

                 file_object.write('DATA' + '/' + str(filename) + '\n')

file_object.close()

