from brial import *
import copy
import pdb
import xdrlib ,sys
import random
import time

Keccak=declare_ring([Block('k',256),Block('v',1600)],globals())


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
state[0][14]=Keccak(k(2))
state[0][15]=Keccak(k(3))
state[0][17]=Keccak(k(4))
state[0][20]=Keccak(k(5))
state[0][21]=Keccak(k(6))
state[0][26]=Keccak(k(7))
state[0][27]=Keccak(k(8))





state[5][9]=Keccak(k(0))
state[5][10]=Keccak(k(1))
state[5][14]=Keccak(k(2))
state[5][15]=Keccak(k(3))
state[5][17]=Keccak(k(4))
state[5][20]=Keccak(k(5))
state[5][21]=Keccak(k(6))
state[5][26]=Keccak(k(7))
state[5][27]=Keccak(k(8))





state[5][2]=Keccak(v(0))
state[15][2]=Keccak(v(0))
state[5][6]=Keccak(v(1))
state[10][6]=Keccak(v(1)+v(2))
state[15][6]=Keccak(v(2))
state[5][12]=Keccak(v(3))
state[10][12]=Keccak(v(3))
state[5][13]=Keccak(v(4))
state[15][13]=Keccak(v(4))
state[5][19]=Keccak(v(31))
state[10][19]=Keccak(v(5)+v(31))
state[15][19]=Keccak(v(5))
state[10][57]=Keccak(v(6))
state[15][57]=Keccak(v(6))
state[5][59]=Keccak(v(7))
state[10][59]=Keccak(v(7))
state[10][63]=Keccak(v(8))
state[15][63]=Keccak(v(8))
state[12][1]=Keccak(v(9))
state[22][1]=Keccak(v(9))
state[17][4]=Keccak(v(10))
state[22][4]=Keccak(v(10))
state[17][5]=Keccak(v(11))
state[22][5]=Keccak(v(11))
state[12][10]=Keccak(v(12))
state[17][10]=Keccak(v(12)+v(13))
state[22][10]=Keccak(v(13))
state[12][11]=Keccak(v(14))
state[22][11]=Keccak(v(14))
state[17][12]=Keccak(v(15))
state[22][12]=Keccak(v(15))
state[12][15]=Keccak(v(16))
state[17][15]=Keccak(v(16))
state[12][16]=Keccak(v(30))
state[17][16]=Keccak(v(17)+v(30))
state[22][16]=Keccak(v(17))
state[12][18]=Keccak(v(18))
state[22][18]=Keccak(v(18))
state[12][21]=Keccak(v(19))
state[17][21]=Keccak(v(19))
state[12][22]=Keccak(v(20))
state[17][22]=Keccak(v(20)+v(21))
state[22][22]=Keccak(v(21))
state[17][23]=Keccak(v(22))
state[22][23]=Keccak(v(22))
state[12][27]=Keccak(v(23))
state[17][27]=Keccak(v(23))
state[12][29]=Keccak(v(29))
state[17][29]=Keccak(v(24)+v(29))
state[22][29]=Keccak(v(24))
state[12][33]=Keccak(v(25))
state[17][33]=Keccak(v(25))
state[12][40]=Keccak(v(26))
state[17][40]=Keccak(v(26))
state[12][53]=Keccak(v(27))
state[17][53]=Keccak(v(27))
state[12][59]=Keccak(v(28))
state[17][59]=Keccak(v(28))





theta(state)
rio(state)
pi(state)
chi(state)

n=0
for i in range(9):
	for j in range(32):
		for i0 in xrange(25):
			for j0 in xrange(64):
				if(state[i0][j0]/Keccak((k(i)*v(j)))):
					print 'k',i,'v',j
					n=n+1


print(n)











