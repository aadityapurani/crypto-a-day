import string
from pwn import remote
final_result= ""

r = remote('localhost',8000)

#for every line send a signal 
for k in range(2):
    for i in range(16):
        num_payload = 15-i
        #send a signal with an a certain number of characters and wait for a responce
        send_payload = 'a' * num_payload

        #first wait for the info to come my way to a point
        final_characters = "hitespace):"
        r.recvuntil(final_characters)
        r.sendline(send_payload)
        correct_line = r.recvline()
        #need to remove the "Your cookie is: " junk
        correct_line = correct_line[17:]
        #now with the payload only use the readable stuff
        correct_line = correct_line[:32*(k+1)]        #32 because 16 will convert into hex so  16 * 2 = 32
        #add on a char for every time this works
        for test_char in string.printable:
            #simulate a send and recieve
            r.recvuntil(final_characters)
            test_payload = send_payload + final_result + test_char
            #send it
            r.sendline(test_payload)
            guess_line = r.recvline()[17:]
            guess_line = guess_line[:32*(k+1)]
            #check it
            if(guess_line == correct_line):
                final_result += test_char
                break
        print(final_result)