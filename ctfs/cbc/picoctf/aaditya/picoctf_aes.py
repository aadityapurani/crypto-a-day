import requests
import base64
import re
import sys
from pwn import *

'''
Solved by @aaditya_purani during the ctf
When json input length is 63, then cookie length is 80 (16 IV + 1 Padding)
When json input length is 64, then cookie length is 96 (16 IV + 16 Padding)
When json input length is 80, then cookie length is 112 (16 IV + 16 Padding)
sort_key will put admin first in JSON
'''


header={'Content-Type':'application/x-www-form-urlencoded'}
session = requests.Session()

if sys.argv[1] == "enum":
	for i in xrange(3, 37):
		tosend = 'p'*i
		print "[+] Sending "+tosend
		data = {'user':'ppp', 'password':tosend}
		r = session.post("http://2018shell2.picoctf.com:12004/login", headers=header, data=data)
		print session.cookies.get_dict()

def splitString(str1,split_by=16):
        return [str1[i:i+split_by] for i in range(0,len(str1),split_by)]

def get_cookie(user):
	data = {'user':'ppp', 'password':tosend}
	r = session.post("http://2018shell2.picoctf.com:12004/login", headers=header, data=data)
	get_sess_encoded = session.cookies.get_dict()
	get_sess = base64.b64decode(get_sess_encoded['cookie'])
	iv = get_sess[:16]
	cipher = get_sess[16:]
	return iv, cipher

def get_message(iv, cipher):
	cookie = base64.b64encode(iv+cipher)
	print len(iv+cipher)
	header1 = {'Connection':'keep-alive' ,'Cookie': 'cookie='+cookie}
	r = requests.get("http://2018shell2.picoctf.com:12004/flag", headers=header1)
	if r.status_code == 500:
		return "Broke!"
	elif 'pico' in r.text:
		print r.text
	else:
		cook = re.findall("Cookie:.*", r.text)[0].replace("&#39;", "'").strip("</p>")
		return cook

iv, cipher= get_cookie("ppppppppppppppppp")
print get_message(iv, cipher)
block_1_real = '{"admin": 0, "pa'
block_1_goal = '{"admin": 1, "pa'
xored = xor(block_1_real, block_1_goal)
xored_iv = xor(iv, xored)
print get_message(xored_iv, cipher)

'''
# Brute method. very bad
for i in range(256):
	iv_list[0] = iv_list[0][:10]+chr(i)+iv_list[0][11]+iv_list[0][12]+iv_list[0][13]+iv_list[0][14]+iv_list[0][15]
	#saved_list[2] = saved_list[2][:14]+chr(i)+saved_list[2][15]
	finale = ''.join(iv_list)
	print get_message(finale, cipher)
'''
# picoCTF{fl1p_4ll_th3_bit3_a41d2782}
