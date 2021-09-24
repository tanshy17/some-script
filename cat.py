###此文件为了cat一个蛋白和多个ligand

import os
import os.path

rootdir = "/mnt/d/tx-tanshuoyan-project/onionnet/GPCRdata/DATA"

for parent,dirnames,filenames in os.walk(rootdir):

	for filename in filenames:
            if 'renamed' in filename:
                ID = filename.split('_')[0]
                ligandfile = ID + '_renamed.pdb'
                complexfile = ID + '_complex.pdb'
                os.system('cat 5ee7_protein.pdb ' +  ligandfile + '>' + complexfile)



