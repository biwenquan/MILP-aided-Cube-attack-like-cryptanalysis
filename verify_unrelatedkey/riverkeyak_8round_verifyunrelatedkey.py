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


state[0][8]=Keccak(k(0))
state[0][9]=Keccak(k(1))
state[0][10]=Keccak(k(2))
state[0][11]=Keccak(k(3))
state[0][12]=Keccak(k(4))
state[0][13]=Keccak(k(5))
state[0][14]=Keccak(k(6))
state[0][15]=Keccak(k(7))
state[0][16]=Keccak(k(8))
state[0][17]=Keccak(k(9))
state[0][18]=Keccak(k(10))
state[0][19]=Keccak(k(11))
state[0][20]=Keccak(k(12))
state[0][21]=Keccak(k(13))
state[0][22]=Keccak(k(14))
state[0][23]=Keccak(k(15))
state[0][24]=Keccak(k(16))
state[0][25]=Keccak(k(17))
state[0][26]=Keccak(k(18))
state[0][27]=Keccak(k(19))
state[0][28]=Keccak(k(20))
state[0][29]=Keccak(k(21))
state[0][30]=Keccak(k(22))
state[0][31]=Keccak(k(23))
state[1][0]=Keccak(k(24))
state[1][1]=Keccak(k(25))
state[1][2]=Keccak(k(26))
state[2][1]=Keccak(k(27))
state[2][2]=Keccak(k(28))
state[2][3]=Keccak(k(29))
state[2][4]=Keccak(k(30))
state[2][21]=Keccak(k(31))
state[2][22]=Keccak(k(32))
state[2][30]=Keccak(k(33))
state[3][0]=Keccak(k(34))
state[3][1]=Keccak(k(35))
state[3][3]=Keccak(k(36))
state[3][8]=Keccak(k(37))
state[3][9]=Keccak(k(38))
state[3][10]=Keccak(k(39))
state[3][11]=Keccak(k(40))
state[3][12]=Keccak(k(41))
state[3][20]=Keccak(k(42))
state[3][21]=Keccak(k(43))
state[3][22]=Keccak(k(44))
state[3][30]=Keccak(k(45))
state[3][31]=Keccak(k(46))
state[4][1]=Keccak(k(47))
state[4][2]=Keccak(k(48))
state[4][3]=Keccak(k(49))




state[11][0]=Keccak(v(0))
state[16][0]=Keccak(v(0))
state[11][1]=Keccak(v(1))
state[16][1]=Keccak(v(1)+v(2))
state[21][1]=Keccak(v(2))
state[11][2]=Keccak(v(4))
state[16][2]=Keccak(v(3))
state[21][2]=Keccak(v(3)+v(4))
state[11][3]=Keccak(v(6))
state[16][3]=Keccak(v(6)+v(5))
state[21][3]=Keccak(v(5))
state[16][4]=Keccak(v(63))
state[21][4]=Keccak(v(63))
state[11][8]=Keccak(v(62))
state[16][8]=Keccak(v(62))
state[11][10]=Keccak(v(7))
state[16][10]=Keccak(v(7))
state[11][11]=Keccak(v(8))
state[16][11]=Keccak(v(9))
state[21][11]=Keccak(v(9)+v(8))
state[11][12]=Keccak(v(10))
state[16][12]=Keccak(v(10)+v(11))
state[21][12]=Keccak(v(11))
state[11][13]=Keccak(v(61))
state[16][13]=Keccak(v(12))
state[21][13]=Keccak(v(12)+v(61))
state[16][14]=Keccak(v(13))
state[21][14]=Keccak(v(13))
state[11][19]=Keccak(v(14))
state[16][19]=Keccak(v(14))
state[11][20]=Keccak(v(15))
state[21][20]=Keccak(v(15))
state[11][21]=Keccak(v(16))
state[16][21]=Keccak(v(16)+v(17))
state[21][21]=Keccak(v(17))
state[11][22]=Keccak(v(60))
state[16][22]=Keccak(v(18))
state[21][22]=Keccak(v(18)+v(60))
state[11][23]=Keccak(v(19))
state[21][23]=Keccak(v(19))
state[11][24]=Keccak(v(20))
state[21][24]=Keccak(v(20))
state[11][25]=Keccak(v(21))
state[21][25]=Keccak(v(21))
state[11][30]=Keccak(v(22))
state[16][30]=Keccak(v(22))
state[11][31]=Keccak(v(23))
state[16][31]=Keccak(v(23))
state[12][1]=Keccak(v(24))
state[17][1]=Keccak(v(24))
state[12][2]=Keccak(v(25))
state[17][2]=Keccak(v(25))
state[9][0]=Keccak(v(26))
state[14][0]=Keccak(v(26)+v(27))
state[19][0]=Keccak(v(27))
state[9][1]=Keccak(v(29))
state[14][1]=Keccak(v(28)+v(29))
state[19][1]=Keccak(v(28))
state[9][2]=Keccak(v(59))
state[14][2]=Keccak(v(59)+v(30))
state[19][2]=Keccak(v(30))
state[9][3]=Keccak(v(31))
state[19][3]=Keccak(v(31))
state[9][4]=Keccak(v(32))
state[19][4]=Keccak(v(32))
state[9][5]=Keccak(v(33))
state[19][5]=Keccak(v(33))
state[14][8]=Keccak(v(34))
state[19][8]=Keccak(v(34))
state[14][9]=Keccak(v(35))
state[19][9]=Keccak(v(35))
state[14][10]=Keccak(v(36))
state[19][10]=Keccak(v(36))
state[9][13]=Keccak(v(37))
state[14][13]=Keccak(v(37))
state[9][14]=Keccak(v(38))
state[19][14]=Keccak(v(38))
state[9][15]=Keccak(v(39))
state[14][15]=Keccak(v(39))
state[14][16]=Keccak(v(40))
state[19][16]=Keccak(v(40))
state[9][21]=Keccak(v(41))
state[14][21]=Keccak(v(41))
state[9][22]=Keccak(v(58))
state[14][22]=Keccak(v(42))
state[19][22]=Keccak(v(42)+v(58))
state[9][23]=Keccak(v(43))
state[14][23]=Keccak(v(43)+v(44))
state[19][23]=Keccak(v(44))
state[9][24]=Keccak(v(57))
state[14][24]=Keccak(v(56))
state[19][24]=Keccak(v(57)+v(56))
state[9][25]=Keccak(v(46))
state[14][25]=Keccak(v(46)+v(47))
state[19][25]=Keccak(v(47))
state[9][26]=Keccak(v(45))
state[14][26]=Keccak(v(48))
state[19][26]=Keccak(v(48)+v(45))
state[9][27]=Keccak(v(49)+v(50))
state[14][27]=Keccak(v(49))
state[19][27]=Keccak(v(50))
state[14][28]=Keccak(v(55))
state[19][28]=Keccak(v(55))
state[14][29]=Keccak(v(51))
state[19][29]=Keccak(v(51))
state[14][30]=Keccak(v(52))
state[19][30]=Keccak(v(52))
state[9][31]=Keccak(v(53))
state[14][31]=Keccak(v(54)+v(53))
state[19][31]=Keccak(v(54))






theta(state)
rio(state)
pi(state)
chi(state)


n=0
for i in range(50):
	for j in range(64):
		for i0 in xrange(25):
			for j0 in xrange(32):
				if(state[i0][j0]/Keccak((k(i)*v(j)))):
					print 'k',i,'v',j
					n=n+1


print(n)



