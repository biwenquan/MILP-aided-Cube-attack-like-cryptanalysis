# MILP-aided-Cube-attack-like-cryptanalysis
For Keccak-MAC-512, whose capacity is 1024-bit.
	  1. Using SageMath, run file "Keccak51264_genlp.py" and obtain file "lpkeccak51264.lp" as a model in Gurobi.
	  	 In this step we obtain the constrians in forms of inequations used by the MILP model.
	  2. Using Gurobi, read and optimize the model file "lpkeccak51264.lp", 
		then obtain the result file "keccakmac51264cube_min_key.sol",
		i.e. the minimum of related key bits with 64-dimension linear cube is 95.
		In this step we obtain the minimum of related key bits of our model/
	  3. Using SageMath, run file "read.py" and print the unrelated key and the cube variables.
	  4. Using SageMath, run file "Keccakmac512_verify_unrelatedkey.py" 
	  	and verify the unrelated key bits do not multiply the 64-dimension cubes in the first round.
		In this step we verify our solution of related key is right if output "0".
	  5. Using SageMath, run file "Keccakmac512_verifyauxiliary.py" and verify the 48-bit related key bits with
	    auxiliary variables do not multiply with the linear cubes in the first round.
		 In this step we verify the auxiliary variables are right if output "0", if output"ki,vj" it means 
		 the auxiliary variable for ki is multiplied with the cube variable vj.
		 
		 
		
For Keccak-Mac-128, 
Program "verifycube.cpp" tests that using the 18-bit related key and the 64-dimension linear cubes in Table 6 
could recovery the right key when appling the MILP-aided cube-attack-like cryptanalysis on 6-round Keccak-MAC-128
in Section 6, it would print "right key is the right key" when the cubes sums computed by the right guessed key
in the preprocessing phase equal to the cube sums computed by the auxiliary variables which are equal to the related key
in the online phase.
That is, it verifies our MILP-aid cube-attack-like cryptanalysis works (it would print "right key is the right key" 
when reovery the 18-bit related key). 
In a PC using a single core (Intel(R)Core(TM)i7-4790 CPU@3.60GHz 3.60GHz) with Visual studio 2010 Release x64
platform, it cost about several hours(within a day) to test our programs.
  
