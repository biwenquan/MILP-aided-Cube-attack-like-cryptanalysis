all_the_text = open('keccakmac51264cube_min_key.sol').read().split('\n')

key_value0 = []
for i in range(1,129):
    if(all_the_text[i][len(all_the_text[i])-1]=='0'):
        key_value0.append(all_the_text[i][0:-2])


key0_index = []
for i in range(len(key_value0)):
    if(len(key_value0[i])>5):
        index_xy = int(key_value0[i][1])+int(key_value0[i][3])*5
        index_z  = int(key_value0[i][5:])
        key0_index.append([index_xy,index_z])



cube_value1 = []
for i in range(129,len(all_the_text)-1):
    if(all_the_text[i][len(all_the_text[i])-1]=='1'):
        cube_value1.append(all_the_text[i][0:-2])


cube1_index = []
for i in range(len(cube_value1)):
    if(len(cube_value1[i])>5):
        index_xy = int(cube_value1[i][1])+int(cube_value1[i][3])*5
        index_z  = int(cube_value1[i][5:])
        cube1_index.append([index_xy,index_z])
cube1_index_final = []
for i in range(len(cube1_index)):
    cube1_index_final.append(cube1_index[i])

#======================
#key0_index存储key 0的索引 cube1_index_final存储cube variable 1的索引


n=0
for i in range(len(key0_index)):
    print "state[%d][%d]=Keccak(k(%d))"%(key0_index[i][0],key0_index[i][1],n)
    n=n+1

print('\n\n\n')
m=0
t=0
for i in range(len(cube1_index_final)):
    print "state[%d][%d]=Keccak(v(%d))"%(cube1_index_final[i][0],cube1_index_final[i][1],m)
    if(t%2==1):    
	m=m+1
    t=t+1
