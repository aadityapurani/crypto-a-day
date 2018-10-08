from Crypto.Cipher import AES
import os
import sys
sys.path.insert(0,os.getcwd()+'/src')
import useful_functions

import requests
#send and recieve
def sr_request(text,url):
    data = {'username':text[0],"nickname":text[:-1],"hobbies":""}
    #print("plain_text: ",len(str(data)))
    str_data = str(data)[:-1]+"',is_admin': 0}"
    str_data = str_data.replace(" ","")
    #print(str_data[64:64+26])
    block_size = 32
    for x in [str_data[i:i+block_size] for i in range(0,len(str_data),block_size)]:
        print(x,len(x),x[26])
    r = requests.post(url,data=data)
    #print("sent: "+text)
    #print(r.url)
    result = r.url[r.url.find("data=")+5:]
    #print(len(result))
    return bytearray(result.encode('utf-8'))

def find_difference():
    url = "http://demo.sjoerdlangkemper.nl/bitflip.php?data=b86c1c94acc93136799e536a244f7ed03c85ca1c53ea10c6299b1684dadef6f61256e0f3674ef8a14bdad427210cb6b1fea35ff9a741363f4264a2f1f092659cf3507f9acbd3069b9581ba8aa340b3978bc4b7725398e89c150ab440e509c0b4"
    for i in range(2,256):
        cur = len(sr_request("a",url))
        cipher_text = sr_request('a'*i,url)
        test = len(cipher_text)
        #print(len(req))
        if(test != cur):
            return test-cur,i

def get_stuff():
    #block_size,char_size = find_difference()
    block_size,char_size = 32,10
    text = '0'*(3*block_size-char_size+15)
    url = "http://demo.sjoerdlangkemper.nl/bitflip.php?data=b86c1c94acc93136799e536a244f7ed03c85ca1c53ea10c6299b1684dadef6f61256e0f3674ef8a14bdad427210cb6b1fea35ff9a741363f4264a2f1f092659cf3507f9acbd3069b9581ba8aa340b3978bc4b7725398e89c150ab440e509c0b4"
    cipher_text = sr_request(text,url)
    print("cipher_text: ",len(cipher_text))
    offset = 2*(block_size+13)
    cipher_list = [cipher_text[i*(2*block_size):(i+1)*(2*block_size)] for i in range(0,len(cipher_text),64)]
    print(len(cipher_list))
    xo1 = useful_functions.xor(bytearray("0"),bytearray("1"))
    cipher_text[offset] = bytes(
        useful_functions.xor(
            bytearray(chr(cipher_text[offset])),xo1
            )
    )
    return cipher_text

if(__name__ == '__main__'):
    print(get_stuff())
