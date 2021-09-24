
import os
import pandas as pd
#
afile = pd.read_csv('a.txt',
                   names=['PDB'])
bfile = pd.read_csv('b.txt',
                   names=['PDB'])
f1 = open('c.txt','w')
f2 = open('d.txt','w')

#####提取a文本所有在b文本中出现的行,保存到c.txt
write = []
for i in afile['PDB']:
    i = i.strip()
    for j in bfile['PDB']:
        if i == j:
            write.append(i)
            f1.writelines(i+"\n")

#####提取a文本没在b文本中出现的行,保存到d.txt
b = []
a = []
for i in bfile['PDB']:
    b.append(i.strip())

for j in afile['PDB']:
    a.append(j.strip())

a_ = set(a + b) - set(b)

for i in a_:
    f2.writelines(i+'\n')

