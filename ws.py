###---------- WATSON-CRICK------------------

dna_transform_map={
	"00":"A",
	"01":"C",
	"10":"G",
	"11":"T"
}
dnaWatson_transform_map={
	"A":"T",
	"T":"A",
	"C":"G",
	"G":"C"
}
def trans_bit2dna(ar_bit):
	return [dna_transform_map[''.join(map(str,ar_bit[i:i+2]))] for i in range(0,len(ar_bit),2)]

def trans_dna2bit(ar_dna):
	bit_transform_map = {value : key for (key, value) in dna_transform_map.items()}
	ar_str_bits= [bit_transform_map[ar_dna[i]] for i in range(0,len(ar_dna),1)]
	ar= list(map(int,''.join(ar_str_bits)))
	return ar

def trans_watson(ar_dna):
	return [dnaWatson_transform_map[n] for n in ar_dna]
	
def util_xor_bitarrays(bit1,bit2):
	return [int(bool(a) != bool(b)) for a,b in zip(bit1,bit2)]
#48 bits split into two 
# right to bottom left and xor right and left to bottom_right
#x1,x2
#x2,x1+x2
#...
def op_f(bits):
	sz=len(bits)//2
	l,r=bits[0:sz],bits[sz:]
	for i in range(3):	
		r_temp=r
		r=util_xor_bitarrays(l,r)
		l=r_temp
	n_bits=l+r
	assert n_bits==bits,"OPERATION FESITEL FAILS"
	return n_bits
		
#expand=array of bits length=48 Ex:[1,0,.....] 
def F_watson(expand):
	##---IN---##	
	#2.Block
	dna=trans_bit2dna(expand)
	#3.Block
	dna_watson=trans_watson(dna)
	#4.Block
	dna_bits=trans_dna2bit(dna_watson)
	#5.Block
	bits=op_f(dna_bits)	
	##---OUT---##
	dna=trans_bit2dna(bits)
	dna_watson=trans_watson(dna)
	dna_bits=trans_dna2bit(dna_watson)
	assert expand==dna_bits,"OPERATION FAILS"
	return dna_bits

