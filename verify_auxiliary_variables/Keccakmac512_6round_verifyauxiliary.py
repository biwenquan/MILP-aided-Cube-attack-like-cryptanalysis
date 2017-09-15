from brial import *
import copy
import pdb
import xdrlib ,sys
import random
import time

Keccak=declare_ring([Block('k',128),Block('v',960)],globals())


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
state[0][5]=Keccak(k(1))
state[0][6]=Keccak(k(2))
state[0][7]=Keccak(k(3))
state[0][8]=Keccak(k(4))
state[0][13]=Keccak(k(5))
state[0][14]=Keccak(k(6))
state[0][15]=Keccak(k(7))
state[0][16]=Keccak(k(8))
state[0][22]=Keccak(k(9))
state[0][24]=Keccak(k(10))
state[0][25]=Keccak(k(11))
state[0][31]=Keccak(k(12))
state[0][32]=Keccak(k(13))
state[0][33]=Keccak(k(14))
state[0][34]=Keccak(k(15))
state[0][39]=Keccak(k(16))
state[0][40]=Keccak(k(17))
state[0][41]=Keccak(k(18))
state[0][42]=Keccak(k(19))
state[0][47]=Keccak(k(20))
state[0][48]=Keccak(k(21))
state[0][50]=Keccak(k(22))
state[0][54]=Keccak(k(23))
state[0][55]=Keccak(k(24))
state[0][56]=Keccak(k(25))





state[10][0]=Keccak(k(0))
state[10][5]=Keccak(k(1))
state[10][6]=Keccak(k(2))
state[10][7]=Keccak(k(3))
state[10][8]=Keccak(k(4))
state[10][13]=Keccak(k(5))
state[10][14]=Keccak(k(6))
state[10][15]=Keccak(k(7))
state[10][16]=Keccak(k(8))
state[10][22]=Keccak(k(9))
state[10][24]=Keccak(k(10))
state[10][25]=Keccak(k(11))
state[10][31]=Keccak(k(12))
state[10][32]=Keccak(k(13))
state[10][33]=Keccak(k(14))
state[10][34]=Keccak(k(15))
state[10][39]=Keccak(k(16))
state[10][40]=Keccak(k(17))
state[10][41]=Keccak(k(18))
state[10][42]=Keccak(k(19))
state[10][47]=Keccak(k(20))
state[10][48]=Keccak(k(21))
state[10][50]=Keccak(k(22))
state[10][54]=Keccak(k(23))
state[10][55]=Keccak(k(24))
state[10][56]=Keccak(k(25))






state[2][2]=Keccak(v(0))
state[7][2]=Keccak(v(0))
state[2][3]=Keccak(v(1))
state[7][3]=Keccak(v(1))
state[2][9]=Keccak(v(2))
state[7][9]=Keccak(v(2))
state[2][10]=Keccak(v(3))
state[7][10]=Keccak(v(3))
state[2][11]=Keccak(v(4))
state[7][11]=Keccak(v(4))
state[2][17]=Keccak(v(5))
state[7][17]=Keccak(v(5))
state[2][19]=Keccak(v(6))
state[7][19]=Keccak(v(6))
state[2][20]=Keccak(v(7))
state[7][20]=Keccak(v(7))
state[2][26]=Keccak(v(8))
state[7][26]=Keccak(v(8))
state[2][28]=Keccak(v(9))
state[7][28]=Keccak(v(9))
state[2][29]=Keccak(v(10))
state[7][29]=Keccak(v(10))
state[2][35]=Keccak(v(11))
state[7][35]=Keccak(v(11))
state[2][36]=Keccak(v(12))
state[7][36]=Keccak(v(12))
state[2][37]=Keccak(v(13))
state[7][37]=Keccak(v(13))
state[2][43]=Keccak(v(14))
state[7][43]=Keccak(v(14))
state[2][45]=Keccak(v(15))
state[7][45]=Keccak(v(15))
state[2][51]=Keccak(v(16))
state[7][51]=Keccak(v(16))
state[2][52]=Keccak(v(17))
state[7][52]=Keccak(v(17))
state[2][58]=Keccak(v(18))
state[7][58]=Keccak(v(18))
state[2][59]=Keccak(v(19))
state[7][59]=Keccak(v(19))
state[3][0]=Keccak(v(20))
state[8][0]=Keccak(v(20))
state[3][7]=Keccak(v(21))
state[8][7]=Keccak(v(21))
state[3][25]=Keccak(v(22))
state[8][25]=Keccak(v(22))
state[3][32]=Keccak(v(23))
state[8][32]=Keccak(v(23))
state[3][40]=Keccak(v(24))
state[8][40]=Keccak(v(24))
state[3][41]=Keccak(v(25))
state[8][41]=Keccak(v(25))
state[3][47]=Keccak(v(26))
state[8][47]=Keccak(v(26))
state[3][48]=Keccak(v(27))
state[8][48]=Keccak(v(27))
state[3][49]=Keccak(v(28))
state[8][49]=Keccak(v(28))
state[3][55]=Keccak(v(29))
state[8][55]=Keccak(v(29))
state[3][57]=Keccak(v(30))
state[8][57]=Keccak(v(30))
state[3][63]=Keccak(v(31))
state[8][63]=Keccak(v(31))



theta(state)
rio(state)
pi(state)
chi(state)

n=0
for i in range(26):
	for j in range(32):
		for i0 in xrange(25):
			for j0 in xrange(64):
				if(state[i0][j0]/Keccak((k(i)*v(j)))):
					print 'k',i,'v',j
					n=n+1


print(n)











