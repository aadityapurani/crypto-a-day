# With Jon :)
# Detects ECB
import collections

def solution():
        f=open("8.txt")
        code = f.read()
        f.close()
        arrr = code.split('\n')
        split_arrr= [splitString(x) for x in arrr]
        split_new = split_arrr[:len(split_arrr)-2]
        print [arrr[i] for i in xrange(0, len(split_new)) if collections.Counter(split_new[i]).most_common(1)[0][1]>1][0]


def splitString(str1,split_by=32):
        return [str1[i:i+split_by] for i in range(0,len(str1),split_by)]

solution()
# d880619740a8a19b7840a8a31c810a3d08649af70dc06f4fd5d2d69c744cd283e2dd052f6b641dbf9d11b0348542bb5708649af70dc06f4fd5d2d69c744cd2839475c9dfdbc1d46597949d9c7e82bf5a08649af70dc06f4fd5d2d69c744cd28397a93eab8d6aecd566489154789a6b0308649af70dc06f4fd5d2d69c744cd283d403180c98c8f6db1f2a3f9c4040deb0ab51b29933f2c123c58386b06fba186a
