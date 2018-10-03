import string
from pwn import remote
char_choice = 'b'
r = remote("localhost",8000)
r.sendline(char_choice*18)
begining=r.recvline()[64:]
first = begining
#len_beg = len(begining)
#print(len_beg)
final_flag = ""
for i in range(100):
    dif = 99-i
    static_payload =char_choice *dif            
    r.sendline(static_payload)
    begining = r.recvline()
    for test in string.printable:
        test_payload =   test + (char_choice * dif)# +final_flag + test 
        r.sendline(test_payload)
        test_output = r.recvline()
        if(test_output==begining):
            print("successful send ",test_payload)
            final_flag =  final_flag+test#+test #test + final_flag[::-1]
            print(i,final_flag, string.printable.find(final_flag[0]))
            if(begining == first):
                print("Still the same")
            break
    print(i)
#lenth of 6 is 129 compared to 97 for everything else
'''
for i in range(100):
    payload = 'a'*i
    r.sendline(payload)
    test = r.recvline()
    if(len(test)!=len_beg):
        print(i,len(test))

'''
#as each divides it changes from right to left
'''
for i in range(1,100):
    payload = 'a'*i
    r.sendline(payload)
    test = r.recvline()[:64]
    if(test!=begining):
        print(i)
        break
begining = test[:32]
for i in range(1,100):
    payload = 'a'*i
    r.sendline(payload)
    test = r.recvline()[:32]
    if(test!=begining):
        print(i)
        break
print("done")
'''