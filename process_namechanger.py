##this file is to change ligand name and chain in the way of Batch processing
###修改ligand name和chain

import os
import os.path

rootdir = "/mnt/d/tx-tanshuoyan-project/onionnet/GPCRdata/DATA"

for parent,dirnames,filenames in os.walk(rootdir):

	for filename in filenames:
            if 'ligand' in filename:
                PDBID = filename.split('.')[1]
                pdbfile = PDBID + '_renamed.pdb'
                os.system('python lignamechanger.py ' +  filename + ' ' + pdbfile)

