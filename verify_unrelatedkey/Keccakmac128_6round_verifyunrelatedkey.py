from brial import *
import copy
import pdb
import xdrlib ,sys
import random
import time

Keccak=declare_ring([Block('k',128),Block('v',1600)],globals())


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

state[0][0]=Keccak(k(0))
state[0][1]=Keccak(k(1))
state[0][2]=Keccak(k(2))
state[0][3]=Keccak(k(3))
state[0][4]=Keccak(k(4))
state[0][5]=Keccak(k(5))
state[0][6]=Keccak(k(6))
state[0][7]=Keccak(k(7))
state[0][9]=Keccak(k(8))
state[0][10]=Keccak(k(9))
state[0][12]=Keccak(k(10))
state[0][13]=Keccak(k(11))
state[0][15]=Keccak(k(12))
state[0][16]=Keccak(k(13))
state[0][18]=Keccak(k(14))
state[0][19]=Keccak(k(15))
state[0][21]=Keccak(k(16))
state[0][22]=Keccak(k(17))
state[0][24]=Keccak(k(18))
state[0][25]=Keccak(k(19))
state[0][27]=Keccak(k(20))
state[0][28]=Keccak(k(21))
state[0][30]=Keccak(k(22))
state[0][31]=Keccak(k(23))
state[0][33]=Keccak(k(24))
state[0][34]=Keccak(k(25))
state[0][36]=Keccak(k(26))
state[0][37]=Keccak(k(27))
state[0][39]=Keccak(k(28))
state[0][40]=Keccak(k(29))
state[0][42]=Keccak(k(30))
state[0][43]=Keccak(k(31))
state[0][45]=Keccak(k(32))
state[0][46]=Keccak(k(33))
state[0][48]=Keccak(k(34))
state[0][49]=Keccak(k(35))
state[0][51]=Keccak(k(36))
state[0][52]=Keccak(k(37))
state[0][54]=Keccak(k(38))
state[0][55]=Keccak(k(39))
state[0][57]=Keccak(k(40))
state[0][58]=Keccak(k(41))
state[0][59]=Keccak(k(42))
state[0][60]=Keccak(k(43))
state[0][61]=Keccak(k(44))
state[0][63]=Keccak(k(45))


state[1][0]=Keccak(k(46))
state[1][1]=Keccak(k(47))
state[1][2]=Keccak(k(48))
state[1][3]=Keccak(k(49))
state[1][4]=Keccak(k(50))
state[1][5]=Keccak(k(51))
state[1][6]=Keccak(k(52))
state[1][7]=Keccak(k(53))
state[1][8]=Keccak(k(54))
state[1][9]=Keccak(k(55))
state[1][10]=Keccak(k(56))
state[1][11]=Keccak(k(57))
state[1][12]=Keccak(k(58))
state[1][13]=Keccak(k(59))
state[1][14]=Keccak(k(60))
state[1][15]=Keccak(k(61))
state[1][16]=Keccak(k(62))
state[1][17]=Keccak(k(63))
state[1][18]=Keccak(k(64))
state[1][19]=Keccak(k(65))
state[1][20]=Keccak(k(66))
state[1][21]=Keccak(k(67))
state[1][22]=Keccak(k(68))
state[1][23]=Keccak(k(69))
state[1][24]=Keccak(k(70))
state[1][25]=Keccak(k(71))
state[1][26]=Keccak(k(72))
state[1][27]=Keccak(k(73))
state[1][28]=Keccak(k(74))
state[1][29]=Keccak(k(75))
state[1][30]=Keccak(k(76))
state[1][31]=Keccak(k(77))
state[1][32]=Keccak(k(78))
state[1][33]=Keccak(k(79))
state[1][34]=Keccak(k(80))
state[1][35]=Keccak(k(81))
state[1][36]=Keccak(k(82))
state[1][37]=Keccak(k(83))
state[1][38]=Keccak(k(84))
state[1][39]=Keccak(k(85))
state[1][40]=Keccak(k(86))
state[1][41]=Keccak(k(87))
state[1][42]=Keccak(k(88))
state[1][43]=Keccak(k(89))
state[1][44]=Keccak(k(90))
state[1][45]=Keccak(k(91))
state[1][46]=Keccak(k(92))
state[1][47]=Keccak(k(93))
state[1][48]=Keccak(k(94))
state[1][49]=Keccak(k(95))
state[1][50]=Keccak(k(96))
state[1][51]=Keccak(k(97))
state[1][52]=Keccak(k(98))
state[1][53]=Keccak(k(99))
state[1][54]=Keccak(k(100))
state[1][55]=Keccak(k(101))
state[1][56]=Keccak(k(102))
state[1][57]=Keccak(k(103))
state[1][58]=Keccak(k(104))
state[1][59]=Keccak(k(105))
state[1][60]=Keccak(k(106))
state[1][61]=Keccak(k(107))
state[1][62]=Keccak(k(108))
state[1][63]=Keccak(k(109))




state[12][9]=Keccak(v(0))
state[17][9]=Keccak(v(0))
state[2][12]=Keccak(v(1))
state[12][12]=Keccak(v(1)+v(2))
state[17][12]=Keccak(v(2))
state[2][15]=Keccak(v(31))
state[12][15]=Keccak(v(3)+v(31))
state[17][15]=Keccak(v(3))
state[2][18]=Keccak(v(4))
state[12][18]=Keccak(v(4)+v(5))
state[17][18]=Keccak(v(5))
state[2][21]=Keccak(v(30))
state[12][21]=Keccak(v(6)+v(30))
state[17][21]=Keccak(v(6))
state[2][24]=Keccak(v(7))
state[12][24]=Keccak(v(7)+v(8))
state[17][24]=Keccak(v(8))
state[2][27]=Keccak(v(29))
state[12][27]=Keccak(v(9)+v(29))
state[17][27]=Keccak(v(9))
state[2][30]=Keccak(v(10))
state[12][30]=Keccak(v(10)+v(11))
state[17][30]=Keccak(v(11))
state[2][33]=Keccak(v(28))
state[12][33]=Keccak(v(12)+v(28))
state[17][33]=Keccak(v(12))
state[2][36]=Keccak(v(13))
state[12][36]=Keccak(v(13)+v(14))
state[17][36]=Keccak(v(14))
state[2][39]=Keccak(v(27))
state[12][39]=Keccak(v(15)+v(27))
state[17][39]=Keccak(v(15))
state[2][42]=Keccak(v(16))
state[12][42]=Keccak(v(16)+v(17))
state[17][42]=Keccak(v(17))
state[2][45]=Keccak(v(26))
state[12][45]=Keccak(v(18)+v(26))
state[17][45]=Keccak(v(18))
state[2][48]=Keccak(v(19))
state[12][48]=Keccak(v(19)+v(20))
state[17][48]=Keccak(v(20))
state[2][51]=Keccak(v(25))
state[12][51]=Keccak(v(21)+v(25))
state[17][51]=Keccak(v(21))
state[2][54]=Keccak(v(22))
state[12][54]=Keccak(v(22))
state[2][57]=Keccak(v(23))
state[12][57]=Keccak(v(23)+v(24))
state[17][57]=Keccak(v(24))




theta(state)
rio(state)
pi(state)
chi(state)

n=0
for i in range(110):
	for j in range(32):
		for i0 in xrange(25):
			for j0 in xrange(64):
				if(state[i0][j0]/Keccak((k(i)*v(j)))):
					print i,j
					n=n+1


print(n)











