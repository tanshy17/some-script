##pymol除PDB中的水

from pymol import cmd
import os

file_path = '/mnt/c/Users/lurq/pdbbind/refined-set'
file = os.listdir(file_path)
for i in file:
    print('processing', i)
    filename = file_path + '/' + i + '/' + i + '_protein.pdb'
    remove_solvent_file = file_path + '/' + i + '/' + i + '_rms.pdb'
    f = open(filename)
    cmd.load(filename)
    cmd.remove('solvent')
    cmd.save(remove_solvent_file, i)
    cmd.delete('all')
