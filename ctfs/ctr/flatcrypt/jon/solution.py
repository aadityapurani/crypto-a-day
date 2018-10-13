import string
from pwn import remote
char_choice = '\x00'
r = remote("localhost",8000)
padding = char_choice  * 10
padding2 = '\x00'* 10
# prev = 0
# r.recvline()
# r.sendline('a')
# print(r.recvline())
# #print(r.recvline())
# r.sendline("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
# print(r.recvline())
# #print(r.recvline())
# print(r.recvline())
# print("SUP BITCH")
def main():
    # cur = ''
    result = ''
    while(True):
        longestLen = -1
        lowestlen = 10000000
        bestchar = None
        L = string.ascii_lowercase+'_' 
        for i in range(len(L)):
            ch = L[i]
            r.recvuntil('service\n')
            r.sendline(padding+ch+result+padding2)
            first = r.readline()

            cur = ord(first[-2])
            if(cur<lowestlen):
                #print(lowestlen,cur)
                lowestlen = cur
                bestchar = ch
                #print(ch)
            longestLen = max(cur,longestLen)
        if(longestLen == lowestlen):
            break
        result = bestchar + result
    print(result)
    #for i in range(256):

    # first = convertToHexString(first)
    # print('hi')
    # for i in range(20,25):
    #     r.sendline(char_choice*20)
    #     test.recv
    #     test = r.recvline().strip()
    #     #test = convertToHexString(test)
    #     print(i,test)
    #     if(first==test):
    #         # q = test[-2:]
    #         print(i,len(test),test,ord(q[0]))
    #         # cur = test[-2:]
    #     r.recvline()


def convertToHexString(s):
    new_str = ""
    i = 0
    while(i<len(s)):
        if(s[i:i+2]=='\\x'):
            new_str+=chr(int(s[i+2:i+4],16))
            i+=4
        else:
            new_str+=s[i]
            i+=1
    new_str = new_str.replace('\\n','\n').replace('\\t','\t').replace('\\r','\r').replace('\\\\','\\')

    return new_str
    
if(__name__ == '__main__'):
    main()