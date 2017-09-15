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

state[0][1]=Keccak(k(0))
state[0][2]=Keccak(k(1))
state[0][4]=Keccak(k(2))
state[0][7]=Keccak(k(3))
state[0][9]=Keccak(k(4))
state[0][10]=Keccak(k(5))
state[0][11]=Keccak(k(6))
state[0][13]=Keccak(k(7))
state[0][15]=Keccak(k(8))
state[0][16]=Keccak(k(9))
state[0][18]=Keccak(k(10))
state[0][22]=Keccak(k(11))
state[0][24]=Keccak(k(12))
state[0][26]=Keccak(k(13))
state[0][27]=Keccak(k(14))
state[0][28]=Keccak(k(15))
state[0][29]=Keccak(k(16))
state[0][31]=Keccak(k(17))
state[0][32]=Keccak(k(18))
state[0][33]=Keccak(k(19))
state[0][35]=Keccak(k(20))
state[0][36]=Keccak(k(21))
state[0][37]=Keccak(k(22))
state[0][38]=Keccak(k(23))
state[0][41]=Keccak(k(24))
state[0][42]=Keccak(k(25))
state[0][44]=Keccak(k(26))
state[0][47]=Keccak(k(27))
state[0][50]=Keccak(k(28))
state[0][53]=Keccak(k(29))
state[0][55]=Keccak(k(30))
state[0][56]=Keccak(k(31))
state[0][59]=Keccak(k(32))
state[0][62]=Keccak(k(33))




state[1][0]=Keccak(k(34))
state[1][1]=Keccak(k(35))
state[1][2]=Keccak(k(36))
state[1][3]=Keccak(k(37))
state[1][4]=Keccak(k(38))
state[1][5]=Keccak(k(39))
state[1][6]=Keccak(k(40))
state[1][7]=Keccak(k(41))
state[1][8]=Keccak(k(42))
state[1][9]=Keccak(k(43))
state[1][10]=Keccak(k(44))
state[1][11]=Keccak(k(45))
state[1][12]=Keccak(k(46))
state[1][13]=Keccak(k(47))
state[1][14]=Keccak(k(48))
state[1][15]=Keccak(k(49))
state[1][16]=Keccak(k(50))
state[1][17]=Keccak(k(51))
state[1][18]=Keccak(k(52))
state[1][19]=Keccak(k(53))
state[1][20]=Keccak(k(54))
state[1][21]=Keccak(k(55))
state[1][22]=Keccak(k(56))
state[1][23]=Keccak(k(57))
state[1][24]=Keccak(k(58))
state[1][25]=Keccak(k(59))
state[1][26]=Keccak(k(60))
state[1][27]=Keccak(k(61))
state[1][28]=Keccak(k(62))
state[1][29]=Keccak(k(63))
state[1][30]=Keccak(k(64))
state[1][31]=Keccak(k(65))
state[1][32]=Keccak(k(66))
state[1][33]=Keccak(k(67))
state[1][34]=Keccak(k(68))
state[1][35]=Keccak(k(69))
state[1][36]=Keccak(k(70))
state[1][37]=Keccak(k(71))
state[1][38]=Keccak(k(72))
state[1][39]=Keccak(k(73))
state[1][40]=Keccak(k(74))
state[1][41]=Keccak(k(75))
state[1][42]=Keccak(k(76))
state[1][43]=Keccak(k(77))
state[1][44]=Keccak(k(78))
state[1][45]=Keccak(k(79))
state[1][46]=Keccak(k(80))
state[1][47]=Keccak(k(81))
state[1][48]=Keccak(k(82))
state[1][49]=Keccak(k(83))
state[1][50]=Keccak(k(84))
state[1][51]=Keccak(k(85))
state[1][52]=Keccak(k(86))
state[1][53]=Keccak(k(87))
state[1][54]=Keccak(k(88))
state[1][55]=Keccak(k(89))
state[1][56]=Keccak(k(90))
state[1][57]=Keccak(k(91))
state[1][58]=Keccak(k(92))
state[1][59]=Keccak(k(93))
state[1][60]=Keccak(k(94))
state[1][61]=Keccak(k(95))
state[1][62]=Keccak(k(96))
state[1][63]=Keccak(k(97))







state[5][4]=Keccak(v(0))
state[15][4]=Keccak(v(0))
state[5][13]=Keccak(v(1))
state[15][13]=Keccak(v(1))
state[5][17]=Keccak(v(2))
state[10][17]=Keccak(v(2))
state[10][18]=Keccak(v(3))
state[15][18]=Keccak(v(3))
state[5][22]=Keccak(v(4))
state[15][22]=Keccak(v(4))
state[10][24]=Keccak(v(5))
state[15][24]=Keccak(v(5))
state[5][26]=Keccak(v(6))
state[10][26]=Keccak(v(6))
state[5][32]=Keccak(v(7))
state[10][32]=Keccak(v(7))
state[5][35]=Keccak(v(8))
state[10][35]=Keccak(v(8))
state[5][38]=Keccak(v(9))
state[10][38]=Keccak(v(9))
state[10][39]=Keccak(v(10))
state[15][39]=Keccak(v(10))
state[5][41]=Keccak(v(11))
state[10][41]=Keccak(v(11))
state[5][44]=Keccak(v(12))
state[15][44]=Keccak(v(12))
state[10][48]=Keccak(v(13))
state[15][48]=Keccak(v(13))
state[5][50]=Keccak(v(14))
state[15][50]=Keccak(v(14))
state[5][59]=Keccak(v(15))
state[15][59]=Keccak(v(15))
state[5][61]=Keccak(v(16))
state[10][61]=Keccak(v(16))
state[2][0]=Keccak(v(17))
state[12][0]=Keccak(v(18))
state[17][0]=Keccak(v(18)+v(17))
state[2][1]=Keccak(v(63))
state[12][1]=Keccak(v(19))
state[17][1]=Keccak(v(19)+v(63))
state[2][3]=Keccak(v(20))
state[17][3]=Keccak(v(20))
state[2][4]=Keccak(v(21))
state[12][4]=Keccak(v(21))
state[2][7]=Keccak(v(22))
state[12][7]=Keccak(v(22)+v(23))
state[17][7]=Keccak(v(23))
state[2][9]=Keccak(v(62))
state[12][9]=Keccak(v(24)+v(62))
state[17][9]=Keccak(v(24))
state[2][12]=Keccak(v(25))
state[17][12]=Keccak(v(25))
state[12][15]=Keccak(v(26))
state[17][15]=Keccak(v(26))
state[2][16]=Keccak(v(27))
state[17][16]=Keccak(v(27))
state[2][18]=Keccak(v(28))
state[12][18]=Keccak(v(28)+v(29))
state[17][18]=Keccak(v(29))
state[12][20]=Keccak(v(30))
state[17][20]=Keccak(v(30))
state[2][21]=Keccak(v(31))
state[12][21]=Keccak(v(31))
state[2][24]=Keccak(v(32))
state[12][24]=Keccak(v(32))
state[2][25]=Keccak(v(33))
state[17][25]=Keccak(v(33))
state[2][29]=Keccak(v(34))
state[17][29]=Keccak(v(34))
state[2][34]=Keccak(v(35))
state[17][34]=Keccak(v(35))
state[12][35]=Keccak(v(36))
state[17][35]=Keccak(v(36))
state[2][38]=Keccak(v(37))
state[17][38]=Keccak(v(37))
state[12][40]=Keccak(v(38))
state[17][40]=Keccak(v(38))
state[12][41]=Keccak(v(39))
state[17][41]=Keccak(v(39))
state[2][43]=Keccak(v(40))
state[17][43]=Keccak(v(40))
state[2][44]=Keccak(v(61))
state[12][44]=Keccak(v(41))
state[17][44]=Keccak(v(41)+v(61))
state[12][46]=Keccak(v(42))
state[17][46]=Keccak(v(42))
state[2][47]=Keccak(v(43))
state[12][47]=Keccak(v(43)+v(44))
state[17][47]=Keccak(v(44))
state[2][49]=Keccak(v(60))
state[12][49]=Keccak(v(45))
state[17][49]=Keccak(v(45)+v(60))
state[2][50]=Keccak(v(46))
state[12][50]=Keccak(v(46))
state[2][52]=Keccak(v(47))
state[12][52]=Keccak(v(47)+v(48))
state[17][52]=Keccak(v(48))
state[2][53]=Keccak(v(59))
state[12][53]=Keccak(v(49)+v(59))
state[17][53]=Keccak(v(49))
state[2][55]=Keccak(v(50))
state[12][55]=Keccak(v(50)+v(51))
state[17][55]=Keccak(v(51))
state[2][56]=Keccak(v(52))
state[17][56]=Keccak(v(52))
state[2][58]=Keccak(v(58))
state[12][58]=Keccak(v(53)+v(58))
state[17][58]=Keccak(v(53))
state[12][59]=Keccak(v(54))
state[17][59]=Keccak(v(54))
state[2][61]=Keccak(v(55))
state[12][61]=Keccak(v(55))
state[2][62]=Keccak(v(56))
state[12][62]=Keccak(v(56)+v(57))
state[17][62]=Keccak(v(57))




theta(state)
rio(state)
pi(state)
chi(state)

n=0
for i in range(98):
	for j in range(64):
		for i0 in xrange(25):
			for j0 in xrange(64):
				if(state[i0][j0]/Keccak((k(i)*v(j)))):
					print "mul"
					n=n+1


print(n)











