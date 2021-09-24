import os
import pandas as pd
import shutil

refined_set_dir = '/mnt/c/Users/lurq/pdbbind/refined-set/'
file = pd.read_csv('160-KINASE-MD.txt', delim_whitespace=True,
                   names=['ID', 'PDB', 'SDF', 'MOL2'])
if not os.path.exists('sdf_dir/'):
    os.makedirs('sdf_dir/')
for i in file['PDB']:
    sdf_file = refined_set_dir+i+'/'+i+'_ligand.sdf'
    if os.path.isfile(sdf_file):
        shutil.copy(sdf_file, 'sdf_dir/')

