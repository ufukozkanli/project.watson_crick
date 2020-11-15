


## Naming
$x$:input
$k$:key
$f_{DNA}(x)$:Function Watson-Crick
$f_{DES}(x)$:DES

## Fact
**İnvolutory function**
$f_{DES}(f_{DES}(x))=x$
$f_{DNA}(f_{DNA}(x))=x$

## Implementation
### 1.DES
|Function/Input|ENC|DEC|
|---|---|---|
|-|$x$|$f_{DES}(x)$
|1.FN_DES|$f_{DES}(x)$|$x$|

### 2.DES+Watson

|Function/Input|ENC|DEC|
|---|---|---|
|-|$x$|$f_{DNA}(f_{DES}(f_{DNA}(x)))$
|1.FN_DNA|$f_{DNA}(x)$|$f_{DES}(f_{DNA}(x))$
|2.FN_DES|$f_{DES}(f_{DNA}(x))$|$f_{DNA}(x)$
|3.FN_DNA|$f_{DNA}(f_{DES}(f_{DNA}(x)))$|$x$


AB-CD
CD-(AB+CD)
(AB+CD)-(AB+CD)+CD
(AB+CD)+CD-((AB+CD)+CD)+(AB*CD)
AB-CD

$$
x_{n}-y_{n} \\
\ \ \ \ \ \ \ \ \ \ \ \ y_{n}-(x_{n}\oplus y_{n})\\
\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ (x_{n}\oplus y_{n}) -(x_{n}\oplus y_{n})\oplus y_{n}=x_{n}\\
\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ x_{n}-x_{n}\oplus (x_{n}\oplus y_{n})=y_{n}\\
$$

11-11
11-00
00-11
11-11

10-01
01-11
11-10
10-01

## Watson-Crick
00-A
01-C
10-G
11-T

---



Length of EB’ is 16
Therefore, ssDNA key (Kdna) sequence length becomes: EB’ * 5 => 16*5 => 80

Kdna: 80 bytes
TAATCCCCGGTTTCACACACAGCGAAGGGGCGTAAGACAATATTAACGAAAGACTGCCTATCCCACACGAGTCGTATAAA

EB':0100100101010011
EB'':0101001100011010


1100001101



10110110
GTCGTTCCCAACGAATATTAAGCGACACACCCCGG

## Implementation
**BlowFish**
https://github.com/AdityaMalani/Blowfish-algorithm-python/blob/master/blowfish.py

**DES**
https://github.com/RobinDavid/pydes/blob/master/pydes.py

**Feistel_cipher**

https://en.wikipedia.org/wiki/Feistel_cipher


### TestCase
1000 iteration

**DES**
KeySize:64bit
TextSize:8192bit
RAM:>3.5MB
Time: 0.12661891078948975 sn

**DES+WATSON**
Time:0.3475011245270917 sn

**BlowFish**
KeySize:448bit
TextSize:8192bit
RAM:>3.0MB
Time:0.045853614807128906 sn

**BlowFish+WATSON**
Time:2.1446536101546942 sn
