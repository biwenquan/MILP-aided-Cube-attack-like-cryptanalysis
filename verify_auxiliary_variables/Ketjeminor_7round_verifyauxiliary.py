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


state[6][0]=Keccak(k(24))
state[6][1]=Keccak(k(25))
state[6][2]=Keccak(k(26))
state[6][3]=Keccak(k(27))
state[6][4]=Keccak(k(28))
state[6][5]=Keccak(k(29))
state[6][6]=Keccak(k(30))
state[6][7]=Keccak(k(31))
state[6][8]=Keccak(k(32))
state[6][9]=Keccak(k(33))
state[6][10]=Keccak(k(34))
state[6][11]=Keccak(k(35))
state[6][12]=Keccak(k(36))
state[6][13]=Keccak(k(37))
state[6][14]=Keccak(k(38))
state[6][15]=Keccak(k(39))
state[6][16]=Keccak(k(40))
state[6][17]=Keccak(k(41))
state[6][18]=Keccak(k(42))
state[6][19]=Keccak(k(43))
state[6][20]=Keccak(k(44))
state[6][21]=Keccak(k(45))
state[6][22]=Keccak(k(46))
state[6][23]=Keccak(k(47))
state[6][24]=Keccak(k(48))
state[6][25]=Keccak(k(49))
state[6][26]=Keccak(k(50))
state[6][27]=Keccak(k(51))
state[6][28]=Keccak(k(52))
state[6][29]=Keccak(k(53))
state[6][30]=Keccak(k(54))
state[6][31]=Keccak(k(55))
state[18][0]=Keccak(k(56))
state[18][1]=Keccak(k(57))
state[18][2]=Keccak(k(58))
state[18][3]=Keccak(k(59))
state[18][4]=Keccak(k(60))
state[18][5]=Keccak(k(61))
state[18][6]=Keccak(k(62))
state[18][7]=Keccak(k(63))
state[18][8]=Keccak(k(64))
state[18][9]=Keccak(k(65))
state[18][10]=Keccak(k(66))
state[18][11]=Keccak(k(67))
state[18][12]=Keccak(k(68))
state[18][13]=Keccak(k(69))
state[18][14]=Keccak(k(70))
state[18][15]=Keccak(k(71))





state[16][0]=Keccak(k(24)+v(0))
state[16][1]=Keccak(k(25)+v(1))
state[16][2]=Keccak(k(26)+v(2))
state[16][3]=Keccak(k(27)+v(3))
state[16][4]=Keccak(k(28)+v(4))
state[16][5]=Keccak(k(29)+v(5))
state[16][6]=Keccak(k(30)+v(6))
state[16][7]=Keccak(k(31)+v(7))
state[16][8]=Keccak(k(32)+v(8))
state[16][9]=Keccak(k(33)+v(9))
state[16][10]=Keccak(k(34)+v(10))
state[16][11]=Keccak(k(35)+v(11))
state[16][12]=Keccak(k(36)+v(12))
state[16][13]=Keccak(k(37)+v(13))
state[16][14]=Keccak(k(38)+v(14))
state[16][15]=Keccak(k(39)+v(15))
state[16][16]=Keccak(k(40)+v(16))
state[16][17]=Keccak(k(41)+v(17))
state[16][18]=Keccak(k(42)+v(18))
state[16][19]=Keccak(k(43)+v(19))
state[16][20]=Keccak(k(44)+v(20))
state[16][21]=Keccak(k(45)+v(21))
state[16][22]=Keccak(k(46)+v(22))
state[16][23]=Keccak(k(47)+v(23))
state[16][24]=Keccak(k(48)+v(24))
state[16][25]=Keccak(k(49)+v(25))
state[16][26]=Keccak(k(50)+v(26))
state[16][27]=Keccak(k(51)+v(27))
state[16][28]=Keccak(k(52)+v(28))
state[16][29]=Keccak(k(53)+v(29))
state[16][30]=Keccak(k(54)+v(30))
state[16][31]=Keccak(k(55)+v(31))
state[3][0]=Keccak(k(56)+v(32))
state[3][1]=Keccak(k(57)+v(33))
state[3][2]=Keccak(k(58)+v(34))
state[3][3]=Keccak(k(59)+v(35))
state[3][4]=Keccak(k(60)+v(36))
state[3][5]=Keccak(k(61)+v(37))
state[3][6]=Keccak(k(62)+v(38))
state[3][7]=Keccak(k(63)+v(39))
state[3][8]=Keccak(k(64)+v(40))
state[3][9]=Keccak(k(65)+v(41))
state[3][10]=Keccak(k(66)+v(42))
state[3][11]=Keccak(k(67)+v(43))
state[3][12]=Keccak(k(68)+v(44))
state[3][13]=Keccak(k(69)+v(45))
state[3][14]=Keccak(k(70)+v(46))
state[3][15]=Keccak(k(71)+v(47))





state[1][0]=Keccak(v(0))
#state[16][0]=Keccak(v(0))
state[1][1]=Keccak(v(1))
#state[16][1]=Keccak(v(1))
state[1][2]=Keccak(v(2))
#state[16][2]=Keccak(v(2))
state[1][3]=Keccak(v(3))
#state[16][3]=Keccak(v(3))
state[1][4]=Keccak(v(4))
#state[16][4]=Keccak(v(4))
state[1][5]=Keccak(v(5))
#state[16][5]=Keccak(v(5))
state[1][6]=Keccak(v(6))
#state[16][6]=Keccak(v(6))
state[1][7]=Keccak(v(7))
#state[16][7]=Keccak(v(7))
state[1][8]=Keccak(v(8))
#state[16][8]=Keccak(v(8))
state[1][9]=Keccak(v(9))
#state[16][9]=Keccak(v(9))
state[1][10]=Keccak(v(10))
#state[16][10]=Keccak(v(10))
state[1][11]=Keccak(v(11))
#state[16][11]=Keccak(v(11))
state[1][12]=Keccak(v(12))
#state[16][12]=Keccak(v(12))
state[1][13]=Keccak(v(13))
#state[16][13]=Keccak(v(13))
state[1][14]=Keccak(v(14))
#state[16][14]=Keccak(v(14))
state[1][15]=Keccak(v(15))
#state[16][15]=Keccak(v(15))
state[1][16]=Keccak(v(16))
#state[16][16]=Keccak(v(16))
state[1][17]=Keccak(v(17))
#state[16][17]=Keccak(v(17))
state[1][18]=Keccak(v(18))
#state[16][18]=Keccak(v(18))
state[1][19]=Keccak(v(19))
#state[16][19]=Keccak(v(19))
state[1][20]=Keccak(v(20))
#state[16][20]=Keccak(v(20))
state[1][21]=Keccak(v(21))
#state[16][21]=Keccak(v(21))
state[1][22]=Keccak(v(22))
#state[16][22]=Keccak(v(22))
state[1][23]=Keccak(v(23))
#state[16][23]=Keccak(v(23))
state[1][24]=Keccak(v(24))
#state[16][24]=Keccak(v(24))
state[1][25]=Keccak(v(25))
#state[16][25]=Keccak(v(25))
state[1][26]=Keccak(v(26))
#state[16][26]=Keccak(v(26))
state[1][27]=Keccak(v(27))
#state[16][27]=Keccak(v(27))
state[1][28]=Keccak(v(28))
#state[16][28]=Keccak(v(28))
state[1][29]=Keccak(v(29))
#state[16][29]=Keccak(v(29))
state[1][30]=Keccak(v(30))
#state[16][30]=Keccak(v(30))
state[1][31]=Keccak(v(31))
#state[16][31]=Keccak(v(31))
#state[3][0]=Keccak(v(32))
state[13][0]=Keccak(v(32))
#state[3][1]=Keccak(v(33))
state[13][1]=Keccak(v(33))
#state[3][2]=Keccak(v(34))
state[13][2]=Keccak(v(34))
#state[3][3]=Keccak(v(35))
state[13][3]=Keccak(v(35))
#state[3][4]=Keccak(v(36))
state[13][4]=Keccak(v(36))
#state[3][5]=Keccak(v(37))
state[13][5]=Keccak(v(37))
#state[3][6]=Keccak(v(38))
state[13][6]=Keccak(v(38))
#state[3][7]=Keccak(v(39))
state[13][7]=Keccak(v(39))
#state[3][8]=Keccak(v(40))
state[13][8]=Keccak(v(40))
#state[3][9]=Keccak(v(41))
state[13][9]=Keccak(v(41))
#state[3][10]=Keccak(v(42))
state[13][10]=Keccak(v(42))
#state[3][11]=Keccak(v(43))
state[13][11]=Keccak(v(43))
#state[3][12]=Keccak(v(44))
state[13][12]=Keccak(v(44))
#state[3][13]=Keccak(v(45))
state[13][13]=Keccak(v(45))
#state[3][14]=Keccak(v(46))
state[13][14]=Keccak(v(46))
#state[3][15]=Keccak(v(47))
state[13][15]=Keccak(v(47))
state[3][16]=Keccak(v(48))
state[13][16]=Keccak(v(48))
state[3][17]=Keccak(v(49))
state[13][17]=Keccak(v(49))
state[3][18]=Keccak(v(50))
state[13][18]=Keccak(v(50))
state[3][19]=Keccak(v(51))
state[13][19]=Keccak(v(51))
state[3][20]=Keccak(v(52))
state[13][20]=Keccak(v(52))
state[3][21]=Keccak(v(53))
state[13][21]=Keccak(v(53))
state[3][22]=Keccak(v(54))
state[13][22]=Keccak(v(54))
state[3][23]=Keccak(v(55))
state[13][23]=Keccak(v(55))
state[3][24]=Keccak(v(56))
state[13][24]=Keccak(v(56))
state[3][25]=Keccak(v(57))
state[13][25]=Keccak(v(57))
state[3][26]=Keccak(v(58))
state[13][26]=Keccak(v(58))
state[3][27]=Keccak(v(59))
state[13][27]=Keccak(v(59))
state[3][28]=Keccak(v(60))
state[13][28]=Keccak(v(60))
state[3][29]=Keccak(v(61))
state[13][29]=Keccak(v(61))
state[3][30]=Keccak(v(62))
state[13][30]=Keccak(v(62))
state[3][31]=Keccak(v(63))
state[13][31]=Keccak(v(63))





theta(state)
rio(state)
pi(state)
chi(state)


n=0
for i in range(24,72):
	for j in range(64):
		for i0 in xrange(25):
			for j0 in xrange(32):
				if(state[i0][j0]/Keccak((k(i)*v(j)))):
					print 'k',i,'v',j
					n=n+1


print(n)



