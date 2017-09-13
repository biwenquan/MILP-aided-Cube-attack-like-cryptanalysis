from brial import *
import copy
import pdb
import xdrlib ,sys
import random
import time


Keccak=declare_ring([Block('v',1472),Block('k',128)],globals())

def theta(state):
	tempstate=[[] for i in range(25)]
	for i in range(25):
		for j in range(64):
			tempstate[i].append(state[i][j])
			for k in range(5):
				tempstate[i][j]+=state[(i%5+5-1)%5+5*k][j]+state[(i%5+1+5)%5+5*k][(j-1+64)%64]

	for i in range(25):
		for j in range(64):
			state[i][j]=tempstate[i][j]



def rio(state):
	rot=[0,1,62,28,27,36,44,6,55,20,3,10,43,25,39,41,45,15,21,8,18,2,61,56,14]
	tempstate=[[] for i in range(25)]
	for i in range(25):
		for j in range(64):
			tempstate[i].append(state[i][(j-rot[i]+64)%64])

	for i in range(25):
		for j in range(64):
			state[i][j]=tempstate[i][j]

def pi(state):
	tempstate=[[] for i in range(25)]
	for i in range(25):
		y=floor(i/5)
		x=i%5
		x1=y
		y1=(2*x+3*y)%5
		temp=5*y1+x1
		for j in range(64):
			tempstate[temp].append(state[i][j])
	for i in range(25):
		for j in range(64):
			state[i][j]=tempstate[i][j]

def chi(state):
	tempstate=[[] for i in range(25)]
	for i in range(5):
		for j in range(5):
			for k in range(64):
				tempstate[5*i+j].append(state[5*i+j][k]+(state[5*i+(j+1)%5][k]+1)*state[5*i+(j+2)%5][k])

	for i in range(25):
		for j in range(64):
			state[i][j]=tempstate[i][j]


lane=[2,7,3,8]
lane1=[2,7]
lane2=[3,8]
keylane=[0,1]


state=[[] for i in range(25)]

for i in range(25):
	for j in range(64):
		state[i].append(Keccak(0))

for i1 in range(len(lane)):
	for j in range(64):
		state[lane[i1]][j] = v(lane[i1]*64+j)



state1=[[] for i in range(25)]
for i in range(25):
	for j in range(64):
		state1[i].append(Keccak(0))
		
for i1 in range(len(keylane)):
	for j in range(64):
		state1[keylane[i1]][j] = k(keylane[i1]*64+j)





f=open('lpkeccak51264.lp','w')


f.write('Minimize\n')

for x in range(len(keylane)-1):
	for z in range(64):
		f.write('X'+str(keylane[x]%5)+'Y'+str(keylane[x]/5)+'Z'+str(z)+' + ')
for z in range(63):
	f.write('X'+str(keylane[len(keylane)-1]%5)+'Y'+str(keylane[len(keylane)-1]/5)+'Z'+str(z)+' + ')
f.write('X'+str(keylane[len(keylane)-1]%5)+'Y'+str(keylane[len(keylane)-1]/5)+'Z63')	

f.write('\n')



f.write('Subject to\n')



#lane1
for z in range(64):
	for i1 in range(len(lane1)):
		f.write('X'+str(lane1[i1]%5)+'Z'+str(z)+' - X'+str(lane1[i1]%5)+'Y'+str(lane1[i1]/5)+'Z'+str(z)+' >= 0\n')	
	for i1 in range(len(lane1)-1):	
		f.write('X'+str(lane1[i1]%5)+'Y'+str(lane1[i1]/5)+'Z'+str(z)+' + ')
	f.write('X'+str(lane1[len(lane1)-1]%5)+'Y'+str(lane1[len(lane1)-1]/5)+'Z'+str(z))
	f.write(' - X'+str(lane1[0]%5)+'Z'+str(z)+' - X'+str(lane1[0]%5)+'Z'+str(z)+' >= 0\n')
#lane2
for z in range(64):
	for i1 in range(len(lane2)):
		f.write('X'+str(lane2[i1]%5)+'Z'+str(z)+' - X'+str(lane2[i1]%5)+'Y'+str(lane2[i1]/5)+'Z'+str(z)+' >= 0\n')	
	for i1 in range(len(lane2)-1):	
		f.write('X'+str(lane2[i1]%5)+'Y'+str(lane2[i1]/5)+'Z'+str(z)+' + ')
	f.write('X'+str(lane2[len(lane2)-1]%5)+'Y'+str(lane2[len(lane2)-1]/5)+'Z'+str(z))
	f.write(' - X'+str(lane2[0]%5)+'Z'+str(z)+' - X'+str(lane2[0]%5)+'Z'+str(z)+' >= 0\n')




#the dimension of variables
for i in range(len(lane)-1):
	for j in range(64):
		f.write('X'+str(lane[i]%5)+'Y'+str(lane[i]/5)+'Z'+str(j)+' + ')
for i in range(63):
	f.write('X'+str(lane[len(lane)-1]%5)+'Y'+str(lane[len(lane)-1]/5)+'Z'+str(i)+' + ')
f.write('X'+str(lane[len(lane)-1]%5)+'Y'+str(lane[len(lane)-1]/5)+'Z63')

###可能需要改动lane1,lane2
for z in range(64):
	f.write(' - X'+str(lane1[0]%5)+'Z'+str(z))
	f.write(' - X'+str(lane2[0]%5)+'Z'+str(z))
f.write(' = 64\n')
#####			


theta(state1)
for i in range(25):
	for j in range(64):
		state[i][j]+=state1[i][j]


rio(state)
pi(state)
chi(state)

for i1 in range(len(lane)):
	for j1 in range(64):
		for i2 in range(len(lane)):
			for j2 in range(64):
				if((i1!=i2) or (j1!=j2)):		
					for i0 in range(25):
						for j0 in range(64):
							if((state[i0][j0]/Keccak(v(lane[i1]*64+j1)*v(lane[i2]*64+j2)))!=0):
								f.write('X'+str(lane[i1]%5)+'Y'+str(lane[i1]/5)+'Z'+str(j1)+' + '+'X'+str(lane[i2]%5)+'Y'+str(lane[i2]/5)+'Z'+str(j2)+' <= 1\n')
								break
								break

for i in range(len(keylane)):
	for i1 in range(len(lane)):
		for j1 in range(64):	
			for j2 in range(64):		
				for i0 in range(25):
					for j0 in range(64):
						if((state[i0][j0]/Keccak(k(keylane[i]*64+j2)*v(lane[i1]*64+j1)))!=0):
							f.write('X'+str(keylane[i]%5)+'Y'+str(keylane[i]/5)+'Z'+str(j2)+' - '+'X'+str(lane[i1]%5)+'Y'+str(lane[i1]/5)+'Z'+str(j1)+' >= 0\n')
							break
							break



			

f.write('Binary\n')
for i in range(len(lane)):
		for z in range(64):
			f.write('X'+str(lane[i]%5)+'Y'+str(lane[i]/5)+'Z'+str(z)+'\n')

for i in range(len(keylane)):
		for z in range(64):
			f.write('X'+str(keylane[i]%5)+'Y'+str(keylane[i]/5)+'Z'+str(z)+'\n')





###可能需要改动lane1,lane2
for z in range(64):
	f.write('X'+str(lane1[0]%5)+'Z'+str(z)+'\n')
	f.write('X'+str(lane2[0]%5)+'Z'+str(z)+'\n')
#####	
	

f.close()




























