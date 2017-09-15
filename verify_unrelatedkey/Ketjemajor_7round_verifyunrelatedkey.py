from brial import *
import copy
import pdb
import xdrlib ,sys
import random
import time

Keccak=declare_ring([Block('k',1600),Block('v',1600)],globals())


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



state=[[] for i in range(25)]
for i in range(25):
	for j in range(64):
		state[i].append(Keccak(0))



state[0][9]=Keccak(k(0))
state[0][10]=Keccak(k(1))
state[0][11]=Keccak(k(2))
state[0][12]=Keccak(k(3))
state[0][13]=Keccak(k(4))
state[0][14]=Keccak(k(5))
state[0][15]=Keccak(k(6))
state[0][16]=Keccak(k(7))
state[0][17]=Keccak(k(8))
state[0][18]=Keccak(k(9))
state[0][19]=Keccak(k(10))
state[0][20]=Keccak(k(11))
state[0][21]=Keccak(k(12))
state[0][22]=Keccak(k(13))
state[0][23]=Keccak(k(14))
state[0][24]=Keccak(k(15))
state[0][25]=Keccak(k(16))
state[0][26]=Keccak(k(17))
state[0][27]=Keccak(k(18))
state[0][28]=Keccak(k(19))
state[0][29]=Keccak(k(20))
state[0][30]=Keccak(k(21))
state[0][31]=Keccak(k(22))
state[0][32]=Keccak(k(23))
state[0][33]=Keccak(k(24))
state[0][34]=Keccak(k(25))
state[0][35]=Keccak(k(26))
state[0][36]=Keccak(k(27))
state[0][37]=Keccak(k(28))
state[0][40]=Keccak(k(29))
state[0][41]=Keccak(k(30))
state[0][42]=Keccak(k(31))
state[0][43]=Keccak(k(32))
state[0][44]=Keccak(k(33))
state[0][45]=Keccak(k(34))
state[0][46]=Keccak(k(35))
state[0][47]=Keccak(k(36))
state[0][48]=Keccak(k(37))
state[0][49]=Keccak(k(38))
state[0][50]=Keccak(k(39))
state[0][51]=Keccak(k(40))
state[0][52]=Keccak(k(41))
state[0][53]=Keccak(k(42))
state[0][54]=Keccak(k(43))
state[0][55]=Keccak(k(44))
state[0][56]=Keccak(k(45))
state[0][57]=Keccak(k(46))
state[0][58]=Keccak(k(47))
state[0][59]=Keccak(k(48))
state[0][60]=Keccak(k(49))
state[0][61]=Keccak(k(50))
state[0][62]=Keccak(k(51))
state[0][63]=Keccak(k(52))
state[6][31]=Keccak(k(53))
state[6][42]=Keccak(k(54))
state[6][44]=Keccak(k(55))
state[6][49]=Keccak(k(56))
state[6][53]=Keccak(k(57))
state[6][55]=Keccak(k(58))
state[6][57]=Keccak(k(59))
state[6][60]=Keccak(k(60))
state[6][62]=Keccak(k(61))
state[12][0]=Keccak(k(62))
state[12][1]=Keccak(k(63))
state[12][2]=Keccak(k(64))
state[12][3]=Keccak(k(65))
state[12][4]=Keccak(k(66))
state[12][5]=Keccak(k(67))
state[12][6]=Keccak(k(68))
state[12][7]=Keccak(k(69))




state[3][1]=Keccak(v(0))
state[18][1]=Keccak(v(0))
state[3][32]=Keccak(v(1))
state[18][32]=Keccak(v(1))
state[3][58]=Keccak(v(2))
state[18][58]=Keccak(v(2))
state[3][59]=Keccak(v(3))
state[18][59]=Keccak(v(3))
state[3][60]=Keccak(v(4))
state[18][60]=Keccak(v(4))
state[3][61]=Keccak(v(5))
state[18][61]=Keccak(v(5))
state[3][62]=Keccak(v(6))
state[18][62]=Keccak(v(6))
state[3][63]=Keccak(v(7))
state[18][63]=Keccak(v(7))
state[9][24]=Keccak(v(8))
state[24][24]=Keccak(v(8))
state[9][25]=Keccak(v(9))
state[24][25]=Keccak(v(9))
state[9][50]=Keccak(v(10))
state[24][50]=Keccak(v(10))
state[9][51]=Keccak(v(11))
state[24][51]=Keccak(v(11))
state[9][52]=Keccak(v(12))
state[24][52]=Keccak(v(12))
state[9][53]=Keccak(v(13))
state[24][53]=Keccak(v(13))
state[9][54]=Keccak(v(14))
state[24][54]=Keccak(v(14))
state[9][55]=Keccak(v(15))
state[24][55]=Keccak(v(15))
state[9][56]=Keccak(v(16))
state[24][56]=Keccak(v(16))
state[9][57]=Keccak(v(17))
state[24][57]=Keccak(v(17))
state[9][58]=Keccak(v(18))
state[24][58]=Keccak(v(18))
state[1][0]=Keccak(v(19))
state[16][0]=Keccak(v(19))
state[1][2]=Keccak(v(20))
state[16][2]=Keccak(v(20))
state[1][4]=Keccak(v(21))
state[16][4]=Keccak(v(21))
state[1][6]=Keccak(v(22))
state[16][6]=Keccak(v(22))
state[1][10]=Keccak(v(23))
state[16][10]=Keccak(v(23))
state[1][13]=Keccak(v(24))
state[16][13]=Keccak(v(24))
state[1][15]=Keccak(v(25))
state[16][15]=Keccak(v(25))
state[1][17]=Keccak(v(26))
state[16][17]=Keccak(v(26))
state[1][18]=Keccak(v(27))
state[16][18]=Keccak(v(27))
state[1][20]=Keccak(v(28))
state[16][20]=Keccak(v(28))
state[1][22]=Keccak(v(29))
state[16][22]=Keccak(v(29))
state[1][23]=Keccak(v(30))
state[16][23]=Keccak(v(30))
state[1][24]=Keccak(v(31))
state[16][24]=Keccak(v(31))
state[1][25]=Keccak(v(32))
state[16][25]=Keccak(v(32))
state[1][26]=Keccak(v(33))
state[16][26]=Keccak(v(33))
state[1][27]=Keccak(v(34))
state[16][27]=Keccak(v(34))
state[1][28]=Keccak(v(35))
state[16][28]=Keccak(v(35))
state[1][29]=Keccak(v(36))
state[16][29]=Keccak(v(36))
state[1][30]=Keccak(v(37))
state[16][30]=Keccak(v(37))
state[1][31]=Keccak(v(38))
state[16][31]=Keccak(v(38))
state[1][32]=Keccak(v(39))
state[16][32]=Keccak(v(39))
state[1][33]=Keccak(v(40))
state[16][33]=Keccak(v(40))
state[1][34]=Keccak(v(41))
state[16][34]=Keccak(v(41))
state[1][35]=Keccak(v(42))
state[16][35]=Keccak(v(42))
state[1][37]=Keccak(v(43))
state[16][37]=Keccak(v(43))
state[1][38]=Keccak(v(44))
state[16][38]=Keccak(v(44))
state[1][39]=Keccak(v(45))
state[16][39]=Keccak(v(45))
state[1][40]=Keccak(v(46))
state[16][40]=Keccak(v(46))
state[1][41]=Keccak(v(47))
state[16][41]=Keccak(v(47))
state[1][42]=Keccak(v(48))
state[16][42]=Keccak(v(48))
state[1][43]=Keccak(v(49))
state[16][43]=Keccak(v(49))
state[1][44]=Keccak(v(50))
state[16][44]=Keccak(v(50))
state[1][45]=Keccak(v(51))
state[16][45]=Keccak(v(51))
state[1][46]=Keccak(v(52))
state[16][46]=Keccak(v(52))
state[1][48]=Keccak(v(53))
state[16][48]=Keccak(v(53))
state[1][50]=Keccak(v(54))
state[16][50]=Keccak(v(54))
state[1][51]=Keccak(v(55))
state[16][51]=Keccak(v(55))
state[1][52]=Keccak(v(56))
state[16][52]=Keccak(v(56))
state[1][53]=Keccak(v(57))
state[16][53]=Keccak(v(57))
state[1][55]=Keccak(v(58))
state[16][55]=Keccak(v(58))
state[1][56]=Keccak(v(59))
state[16][56]=Keccak(v(59))
state[1][57]=Keccak(v(60))
state[16][57]=Keccak(v(60))
state[1][59]=Keccak(v(61))
state[16][59]=Keccak(v(61))
state[1][61]=Keccak(v(62))
state[16][61]=Keccak(v(62))
state[1][63]=Keccak(v(63))
state[16][63]=Keccak(v(63))





theta(state)
rio(state)
pi(state)
chi(state)


n=0
for i in range(70):
	for j in range(64):
		for i0 in xrange(25):
			for j0 in xrange(64):
				if(state[i0][j0]/Keccak((k(i)*v(j)))):
					print 'k',i,'v',j
					n=n+1


print(n)



