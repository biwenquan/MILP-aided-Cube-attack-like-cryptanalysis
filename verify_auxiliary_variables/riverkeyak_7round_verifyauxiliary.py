from brial import *
import copy
import pdb
import xdrlib ,sys
import random
import time

Keccak=declare_ring([Block('k',1600),Block('v',1600)],globals())

lanesize=32



def theta(state):
	tempstate=[[] for i in range(25)]
	for i in range(25):
		for j in range(lanesize):
			tempstate[i].append(state[i][j])
			for k in range(5):
				tempstate[i][j]+=state[(i%5+5-1)%5+5*k][j]+state[(i%5+1+5)%5+5*k][(j-1+lanesize)%lanesize]

	for i in range(25):
		for j in range(lanesize):
			state[i][j]=tempstate[i][j]



def rio(state):
	rot=[0,1,62,28,27,36,44,6,55,20,3,10,43,25,39,41,45,15,21,8,18,2,61,56,14]
	tempstate=[[] for i in range(25)]
	for i in range(25):
		for j in range(lanesize):
			tempstate[i].append(state[i][(j-rot[i]+4*lanesize)%lanesize])

	for i in range(25):
		for j in range(lanesize):
			state[i][j]=tempstate[i][j]

def pi(state):
	tempstate=[[] for i in range(25)]
	for i in range(25):
		y=floor(i/5)
		x=i%5
		x1=y
		y1=(2*x+3*y)%5
		temp=5*y1+x1
		for j in range(lanesize):
			tempstate[temp].append(state[i][j])
	for i in range(25):
		for j in range(lanesize):
			state[i][j]=tempstate[i][j]

def chi(state):
	tempstate=[[] for i in range(25)]
	for i in range(5):
		for j in range(5):
			for k in range(lanesize):
				tempstate[5*i+j].append(state[5*i+j][k]+(state[5*i+(j+1)%5][k]+1)*state[5*i+(j+2)%5][k])

	for i in range(25):
		for j in range(lanesize):
			state[i][j]=tempstate[i][j]




state=[[] for i in range(25)]
for i in range(25):
	for j in range(32):
		state[i].append(Keccak(0))


state[1][6]=Keccak(k(0))
state[1][7]=Keccak(k(1))
state[1][8]=Keccak(k(2))
state[1][9]=Keccak(k(3))
state[1][10]=Keccak(k(4))
state[1][11]=Keccak(k(5))
state[1][16]=Keccak(k(6))
state[1][17]=Keccak(k(7))
state[1][18]=Keccak(k(8))
state[1][19]=Keccak(k(9))
state[1][20]=Keccak(k(10))
state[1][21]=Keccak(k(11))
state[1][22]=Keccak(k(12))
state[1][28]=Keccak(k(13))
state[1][29]=Keccak(k(14))
state[1][30]=Keccak(k(15))
state[2][0]=Keccak(k(16))
state[2][7]=Keccak(k(17))
state[2][10]=Keccak(k(18))
state[2][21]=Keccak(k(19))
state[2][27]=Keccak(k(20))
state[2][31]=Keccak(k(21))
state[3][6]=Keccak(k(22))
state[3][16]=Keccak(k(23))
state[4][1]=Keccak(k(24))
state[4][2]=Keccak(k(25))
state[4][3]=Keccak(k(26))
state[4][6]=Keccak(k(27))
state[4][7]=Keccak(k(28))




state[11][6]=Keccak(k(0))
state[11][7]=Keccak(k(1))
state[11][8]=Keccak(k(2))
state[11][9]=Keccak(k(3))
state[11][10]=Keccak(k(4))
state[11][11]=Keccak(k(5))
state[11][16]=Keccak(k(6))
state[11][17]=Keccak(k(7))
state[11][18]=Keccak(k(8))
state[11][19]=Keccak(k(9))
state[11][20]=Keccak(k(10))
state[11][21]=Keccak(k(11))
state[11][22]=Keccak(k(12))
state[11][28]=Keccak(k(13))
state[11][29]=Keccak(k(14))
state[11][30]=Keccak(k(15))
state[12][0]=Keccak(k(16))
state[12][7]=Keccak(k(17))
state[12][10]=Keccak(k(18))
state[12][21]=Keccak(k(19))
state[12][27]=Keccak(k(20))
state[12][31]=Keccak(k(21))
state[13][6]=Keccak(k(22))
state[13][16]=Keccak(k(23))
state[14][1]=Keccak(k(24))
state[14][2]=Keccak(k(25))
state[14][3]=Keccak(k(26)+v(15)+v(16))
state[14][6]=Keccak(k(27))
state[14][7]=Keccak(k(28))






state[11][1]=Keccak(v(0))
state[16][1]=Keccak(v(0))
state[11][2]=Keccak(v(1))
state[16][2]=Keccak(v(1))
state[16][4]=Keccak(v(2))
state[21][4]=Keccak(v(2))
state[11][5]=Keccak(v(3))
state[21][5]=Keccak(v(3))
state[11][12]=Keccak(v(4))
state[16][12]=Keccak(v(4))
state[11][13]=Keccak(v(5))
state[16][13]=Keccak(v(5)+v(6))
state[21][13]=Keccak(v(6))
state[11][14]=Keccak(v(31))
state[16][14]=Keccak(v(7)+v(31))
state[21][14]=Keccak(v(7))
state[11][15]=Keccak(v(8))
state[21][15]=Keccak(v(8))
state[16][16]=Keccak(v(9))
state[21][16]=Keccak(v(9))
state[11][23]=Keccak(v(10))
state[16][23]=Keccak(v(10))
state[11][24]=Keccak(v(11))
state[16][24]=Keccak(v(11)+v(12))
state[21][24]=Keccak(v(12))
state[11][25]=Keccak(v(30))
state[16][25]=Keccak(v(13)+v(30))
state[21][25]=Keccak(v(13))
state[17][27]=Keccak(v(14))
state[22][27]=Keccak(v(14))
state[9][3]=Keccak(v(15))

state[19][3]=Keccak(v(16))
state[9][4]=Keccak(v(29))
state[14][4]=Keccak(v(17))+v(29)
state[19][4]=Keccak(v(17))
state[9][5]=Keccak(v(18))
state[14][5]=Keccak(v(18))
state[14][12]=Keccak(v(19))
state[19][12]=Keccak(v(19))
state[14][13]=Keccak(v(20))
state[19][13]=Keccak(v(20))
state[9][16]=Keccak(v(21))
state[14][16]=Keccak(v(21)+v(22))
state[19][16]=Keccak(v(22))
state[9][17]=Keccak(v(23))
state[19][17]=Keccak(v(23))
state[14][24]=Keccak(v(24))
state[19][24]=Keccak(v(24))
state[9][25]=Keccak(v(28))
state[14][25]=Keccak(v(25)+v(28))
state[19][25]=Keccak(v(25))
state[9][26]=Keccak(v(26))
state[14][26]=Keccak(v(26))
state[9][27]=Keccak(v(27))
state[19][27]=Keccak(v(27))






theta(state)
rio(state)
pi(state)
chi(state)


n=0
for i in range(29):
	for j in range(32):
		for i0 in xrange(25):
			for j0 in xrange(32):
				if(state[i0][j0]/Keccak((k(i)*v(j)))):
					print 'k',i,'v',j
					n=n+1


print(n)



