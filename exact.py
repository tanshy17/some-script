
####提取a文本所有在b文本中出现的行  OK
a = [f1 for f1 in open('core.txt').readlines()]
b=[f2 for f2 in open('INDEX_refined_name-2019.txt').readlines()]

write = []
for i in a:
    i = i.strip()
    for j in b:
        if i == j.split(' ')[0]:
            write.append(j)

with open('core-name.txt','w') as f:
        f.writelines(write)


##查找 还不行
# b=[x for x in open('core-name.txt').readlines() ]
# if x.find('kinase')>-1:
#     write.append(j)
# with open('core-kinase.txt','w') as f:
#     f.writelines(write)