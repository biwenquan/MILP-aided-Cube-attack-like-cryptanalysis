#include <stdio.h>
#include <conio.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>

typedef unsigned char UINT8;
typedef unsigned long int UINT32;
typedef unsigned long long int UINT64;
typedef signed long long int INT64;

#define random(x) (rand())%x;
#define nrRounds 6
UINT64 KeccakRoundConstants[nrRounds];//these are constant,
#define nrLanes 25
unsigned int KeccakRhoOffsets[nrLanes];//these are constant,
#define nrMessage 0x8000
#define index(x, y) (((x)%5)+5*((y)%5))
#define ROL64(a, offset) ((offset != 0) ? ((((UINT64)a) << offset) ^ (((UINT64)a) >> (64-offset))) : a)


void KeccakPermutationOnWords(UINT64 *state);
void theta(UINT64 *A);
void rho(UINT64 *A);
void pi(UINT64 *A);
void chi(UINT64 *A);
void iota(UINT64 *A, unsigned int indexRound);


void KeccakPermutationOnWords(UINT64 *state)
{
    unsigned int i;


    for(i=0; i<nrRounds; i++) {
        theta(state);
        rho(state);
        pi(state);
        chi(state);
        iota(state, i);
    }
}


void theta(UINT64 *A)
{
    unsigned int x, y;
    UINT64 C[5], D[5];//C are the Xors of the five bits in every column. D are the Xors of the ten bits in right-behind column and right column

    for(x=0; x<5; x++) {
        C[x] = 0;
        for(y=0; y<5; y++)
            C[x] ^= A[index(x, y)];
    }
    for(x=0; x<5; x++)
        D[x] = ROL64(C[(x+1)%5], 1) ^ C[(x+4)%5];
    for(x=0; x<5; x++)
        for(y=0; y<5; y++)
            A[index(x, y)] ^= D[x];
}

void rho(UINT64 *A)
{
    unsigned int x, y;

    for(x=0; x<5; x++) for(y=0; y<5; y++)
        A[index(x, y)] = ROL64(A[index(x, y)], KeccakRhoOffsets[index(x, y)]);
}

void pi(UINT64 *A)
{
    unsigned int x, y;
    UINT64 tempA[25];

    for(x=0; x<5; x++) for(y=0; y<5; y++)
        tempA[index(x, y)] = A[index(x, y)];
    for(x=0; x<5; x++) for(y=0; y<5; y++)
        A[index(0*x+1*y, 2*x+3*y)] = tempA[index(x, y)];//learn from this!
}

void chi(UINT64 *A)
{
    unsigned int x, y;
    UINT64 C[5];

    for(y=0; y<5; y++) {
        for(x=0; x<5; x++)
            C[x] = A[index(x, y)] ^ ((~A[index(x+1, y)]) & A[index(x+2, y)]);
        for(x=0; x<5; x++)
            A[index(x, y)] = C[x];
    }
}

void iota(UINT64 *A, unsigned int indexRound)
{
    A[index(0, 0)] ^= KeccakRoundConstants[indexRound];
}



int LFSR86540(UINT8 *LFSR)
{
    int result = ((*LFSR) & 0x01) != 0;
    if (((*LFSR) & 0x80) != 0)
        // Primitive polynomial over GF(2): x^8+x^6+x^5+x^4+1
        (*LFSR) = ((*LFSR) << 1) ^ 0x71;
    else
        (*LFSR) <<= 1;
    return result;
}

void KeccakInitializeRoundConstants()
{
    UINT8 LFSRstate = 0x01;
    unsigned int i, j, bitPosition;

    for(i=0; i<nrRounds; i++) {
        KeccakRoundConstants[i] = 0;
        for(j=0; j<7; j++) {
            bitPosition = (1<<j)-1; //2^j-1
            if (LFSR86540(&LFSRstate))
                KeccakRoundConstants[i] ^= (UINT64)1<<bitPosition;
        }
    }
}

void KeccakInitializeRhoOffsets()
{
    unsigned int x, y, t, newX, newY;

    KeccakRhoOffsets[index(0, 0)] = 0;
    x = 1;
    y = 0;
    for(t=0; t<24; t++) {
        KeccakRhoOffsets[index(x, y)] = ((t+1)*(t+2)/2) % 64;
        newX = (0*x+1*y) % 5;
        newY = (2*x+3*y) % 5;
        x = newX;
        y = newY;
    }
}

void KeccakInitialize()
{
    KeccakInitializeRoundConstants();
    KeccakInitializeRhoOffsets();
}

void displaystate(UINT64 *state)
{
	unsigned int i;
	for(i=0;i<nrLanes;i++)
	{
		printf("%08x ",(unsigned int)(state[i]));
		if((i+1)%5==0) printf("\n");
	}
	printf("\n");
}
void verify_6rounds()
{

	clock_t start,finish;
	start = clock();

	UINT64 InitialState[25]={0};
	UINT64 TempState[25]={0};
	UINT64 FinalState[25]={0};
	UINT64 GuessedCubesum[512][25]={0};
	UINT64 GuessedCubesum1[25]={0};
	UINT64 Cubesum[25]={0};
	UINT64 Key[2]={0};
	int tempkey[9]={0};
	int guessedkey[9]={0};
	int auxkey[9]={0};

	KeccakInitialize();
	int mm,nn,tt;
	UINT64 i,j,k,temp,temp1,temp2,counter,a;
	unsigned int rightkey[9]={0};

	int tempposition[9]={35,38,41,44,47,50,53,56,62};
	int rightposition[9]={8,11,14,17,20,23,26,29,32};

	unsigned int indexk[2][9];

	indexk[0][0]=0;indexk[1][0]=35;  
	indexk[0][1]=0;indexk[1][1]=38;  
	indexk[0][2]=0;indexk[1][2]=41;  
	indexk[0][3]=0;indexk[1][3]=44; 
	indexk[0][4]=0;indexk[1][4]=47; 
	indexk[0][5]=0;indexk[1][5]=50; 
	indexk[0][6]=0;indexk[1][6]=53; 
	indexk[0][7]=0;indexk[1][7]=56; 
	indexk[0][8]=0;indexk[1][8]=62;

	unsigned int indexa[2][9];
	indexa[0][0]=0;indexa[1][0]=8;  
	indexa[0][1]=0;indexa[1][1]=11;  
	indexa[0][2]=0;indexa[1][2]=14;  
	indexa[0][3]=0;indexa[1][3]=17; 
	indexa[0][4]=0;indexa[1][4]=20; 
	indexa[0][5]=0;indexa[1][5]=23; 
	indexa[0][6]=0;indexa[1][6]=26; 
	indexa[0][7]=0;indexa[1][7]=29; 
	indexa[0][8]=0;indexa[1][8]=32; 

	unsigned int indexv[2][32];
	indexv[0][0]=12;indexv[1][0]=9;  
	indexv[0][1]=2;indexv[1][1]=12;  
	indexv[0][2]=2;indexv[1][2]=15;  
	indexv[0][3]=2;indexv[1][3]=18; 
	indexv[0][4]=2;indexv[1][4]=21; 
	indexv[0][5]=2;indexv[1][5]=24; 
	indexv[0][6]=2;indexv[1][6]=27; 
	indexv[0][7]=2;indexv[1][7]=30; 
	indexv[0][8]=2;indexv[1][8]=33; 
	indexv[0][9]=2;indexv[1][9]=36;  
	indexv[0][10]=2;indexv[1][10]=39;  
	indexv[0][11]=2;indexv[1][11]=42; 
	indexv[0][12]=2;indexv[1][12]=45; 
	indexv[0][13]=2;indexv[1][13]=48; 
	indexv[0][14]=2;indexv[1][14]=51; 
	indexv[0][15]=2;indexv[1][15]=54;
	indexv[0][16]=2;indexv[1][16]=57;



	indexv[0][17]=14;indexv[1][17]=1;  
	indexv[0][18]=14;indexv[1][18]=2;  
	indexv[0][19]=14;indexv[1][19]=3; 
	indexv[0][20]=14;indexv[1][20]=4; 
	indexv[0][21]=14;indexv[1][21]=5; 
	indexv[0][22]=14;indexv[1][22]=6; 
	indexv[0][23]=14;indexv[1][23]=7; 
	indexv[0][24]=19;indexv[1][24]=0; 
	indexv[0][25]=19;indexv[1][25]=1;  
	indexv[0][26]=19;indexv[1][26]=2;  
	indexv[0][27]=19;indexv[1][27]=3; 
	indexv[0][28]=19;indexv[1][28]=4; 
	indexv[0][29]=19;indexv[1][29]=5; 
	indexv[0][30]=19;indexv[1][30]=6; 
	indexv[0][31]=19;indexv[1][31]=7;

	FILE *f;
	f=fopen("cubesum.txt","w+");
	srand(time(NULL));
	fprintf(f,"start\n");
	for(i=0;i<25;i++){
		InitialState[i]=0;
	}
	printf("1\n");
	for(i=0;i<2;i++){
		for(j=0;j<64;j++){
			temp=random(2);
			if(temp)
			{
				Key[i]^=((UINT64)0x1<<j);
			}
		}
	}
	
	
	 rightkey[0]=((Key[0]>>8)&1);      
	 rightkey[1]=((Key[0]>>11)&1);    
	 rightkey[2]=((Key[0]>>14)&1);    
	 rightkey[3]=((Key[0]>>17)&1);    
	 rightkey[4]=((Key[0]>>20)&1);     
	 rightkey[5]=((Key[0]>>23)&1);      
	 rightkey[6]=((Key[0]>>26)&1);   
	 rightkey[7]=((Key[0]>>29)&1);    
	 rightkey[8]=((Key[0]>>32)&1); 
	 fprintf(f,"right key:");
	 printf("right key:");
	for(i=0;i<9;i++)
	{
		if(rightkey[i])
		{
			fprintf(f,"1");
			printf("1");
		}
		else
		{
			fprintf(f,"0");
			printf("0");
		}
	}
	fprintf(f,"\n");
	printf("\n");

	 tempkey[0]=((Key[0]>>35)&1);      
	 tempkey[1]=((Key[0]>>38)&1);    
	 tempkey[2]=((Key[0]>>41)&1);    
	 tempkey[3]=((Key[0]>>44)&1);    
	 tempkey[4]=((Key[0]>>47)&1);     
	 tempkey[5]=((Key[0]>>50)&1);      
	 tempkey[6]=((Key[0]>>53)&1);   
	 tempkey[7]=((Key[0]>>56)&1);    
	 tempkey[8]=((Key[0]>>62)&1);

	//preprocess phase
	 for(i=0;i<25;i++){
		InitialState[i]=0;
	}

	 for(i=0;i<9;i++)
	 {
		 InitialState[0] |= ((UINT64)(tempkey[i]&1)) << tempposition[i];
	 }


	for(j=0;j<(UINT64(1)<<32);j++)//initialize tempstate
	{
		for(k=0;k<25;k++)//fresh the tempstate for the key and initial value
		{
			TempState[k]=InitialState[k];
		}
		mm=0;
		for(k=0;k<17;k++)
		{
			
			temp1=(j>>mm)&1;
			temp2=(j>>(mm+1))&1;
			
			if(mm==0)
			{
				if(temp1){
				TempState[indexv[0][k]]|=UINT64(1)<<indexv[1][k];
				TempState[indexv[0][k]+5]|=UINT64(1)<<indexv[1][k];
				}
				else{
				TempState[indexv[0][k]]&=(~(UINT64(1)<<indexv[1][k]));
				TempState[indexv[0][k]+5]&=(~(UINT64(1)<<indexv[1][k]));
				}
				mm++;

			}
			else if(mm==29)
			{
				if(temp1){
				TempState[indexv[0][k]]|=UINT64(1)<<indexv[1][k];
				TempState[indexv[0][k]+10]|=UINT64(1)<<indexv[1][k];
				}
				else{
				TempState[indexv[0][k]]&=(~(UINT64(1)<<indexv[1][k]));
				TempState[indexv[0][k]+10]&=(~(UINT64(1)<<indexv[1][k]));
				}
				mm++;


			}

			else
			{
				if(temp1){
				TempState[indexv[0][k]]|=UINT64(1)<<indexv[1][k];
				}
				else{
				TempState[indexv[0][k]]&=(~(UINT64(1)<<indexv[1][k]));
				}
				mm++;
				if(temp2){
				TempState[indexv[0][k]+10]|=UINT64(1)<<indexv[1][k];
				}
				else{
				TempState[indexv[0][k]+10]&=(~(UINT64(1)<<indexv[1][k]));
				}
				mm++;
				if(temp1^temp2)
				{
				TempState[indexv[0][k]+15]|=UINT64(1)<<indexv[1][k];
				}
				else{
				TempState[indexv[0][k]+15]&=(~(UINT64(1)<<indexv[1][k]));
				}

			}

		}
		KeccakPermutationOnWords((UINT64 *)TempState);
			
		for(k=0;k<25;k++){
			GuessedCubesum1[k]^=TempState[k];
		}


	}

	printf("Cubesum1\n");
	fprintf(f,"Cubesum1\n");
	for(int k=0;k<25;k++)
	{
		printf("%08x ",GuessedCubesum1[k]);
		fprintf(f,"%08x ",GuessedCubesum1[k]);
		if(k%5==4){ printf("\n");fprintf(f,"\n");}
	}
	//online phase
	for(i=0;i<25;i++){
		if(i<2)
			InitialState[i]=Key[i];
		else
			InitialState[i]=0;
	}

	 for(i=0;i<9;i++)
	 {
		 InitialState[5] |= ((UINT64)(rightkey[i]&1)) << rightposition[i];
	 }


	for(j=0;j<(UINT64(1)<<32);j++)//initialize tempstate
	{
		for(k=0;k<25;k++)//fresh the tempstate for the key and initial value
		{
			TempState[k]=InitialState[k];
		}
		mm=0;
		for(k=0;k<17;k++)
		{
			
			temp1=(j>>mm)&1;
			temp2=(j>>(mm+1))&1;
			
			if(mm==0)
			{
				if(temp1){
				TempState[indexv[0][k]]|=UINT64(1)<<indexv[1][k];
				TempState[indexv[0][k]+5]|=UINT64(1)<<indexv[1][k];
				}
				else{
				TempState[indexv[0][k]]&=(~(UINT64(1)<<indexv[1][k]));
				TempState[indexv[0][k]+5]&=(~(UINT64(1)<<indexv[1][k]));
				}
				mm++;

			}
			else if(mm==29)
			{
				if(temp1){
				TempState[indexv[0][k]]|=UINT64(1)<<indexv[1][k];
				TempState[indexv[0][k]+10]|=UINT64(1)<<indexv[1][k];
				}
				else{
				TempState[indexv[0][k]]&=(~(UINT64(1)<<indexv[1][k]));
				TempState[indexv[0][k]+10]&=(~(UINT64(1)<<indexv[1][k]));
				}
				mm++;


			}

			else
			{
				if(temp1){
				TempState[indexv[0][k]]|=UINT64(1)<<indexv[1][k];
				}
				else{
				TempState[indexv[0][k]]&=(~(UINT64(1)<<indexv[1][k]));
				}
				mm++;
				if(temp2){
				TempState[indexv[0][k]+10]|=UINT64(1)<<indexv[1][k];
				}
				else{
				TempState[indexv[0][k]+10]&=(~(UINT64(1)<<indexv[1][k]));
				}
				mm++;
				if(temp1^temp2)
				{
				TempState[indexv[0][k]+15]|=UINT64(1)<<indexv[1][k];
				}
				else{
				TempState[indexv[0][k]+15]&=(~(UINT64(1)<<indexv[1][k]));
				}

			}

		}
		KeccakPermutationOnWords((UINT64 *)TempState);
			
		for(k=0;k<25;k++){
			FinalState[k]^=TempState[k];
		}


	}
	printf("Cubesum2\n");
	fprintf(f,"Cubesum2\n");
	for(int k=0;k<25;k++)
	{
		printf("%08x ",FinalState[k]);
		fprintf(f,"%08x ",FinalState[k]);
		if(k%5==4) {printf("\n"); fprintf(f,"\n");}
	}
	bool flag1=0;
	for(k=0;k<25;k++)
	{
		if(FinalState[k]==GuessedCubesum1[k])
		{	printf(" euqal\n");
			fprintf(f," euqal\n");
			
		}
		else{
			flag1=1;
		}
	}
	if(flag1==0)
	{
		printf(" right key is the right key\n");
		fprintf(f," right key is the right key\n");
	}
	fprintf(f,"finish\n");
	
	finish = clock();
	fprintf(f,"time=%f\n",(double)(finish-start)/CLK_TCK);
	fprintf(f,"Done!\n");
	fclose(f);
	printf("time=%f\n",(double)(finish-start)/CLK_TCK);
	printf("Done!\n");
    getch();

}

int main()
{

	verify_6rounds();
	return 0;
}